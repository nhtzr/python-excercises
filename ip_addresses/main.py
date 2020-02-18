import fileinput


def ip_partititons(ip_line: str):
    if len(ip_line) < 4:
        raise ValueError(f"Expected at least 4 digits, got {ip_line}")
    i = 0
    j = 1
    k = 2
    l = 3

    while True:
        ip_str = f"{ip_line[i:j]}.{ip_line[j:k]}.{ip_line[k:l]}.{ip_line[l:]}"
        yield ip_str

        if l + 1 < len(ip_line):
            l += 1
            continue
        if k + 1 < l:
            k += 1
            l = k + 1
            continue
        if j + 1 < k:
            j += 1
            k = j + 1
            continue
        break


def is_valid_ip(ip_str: str):
    octets_str = ip_str.split('.')
    try:
        octets_int = tuple(int(o) for o in octets_str)
    except ValueError:
        return False

    for octet_int in octets_int:
        if octet_int < 0:
            return False
        if octet_int > 255:
            return False
    return True


def main(ip_line):
    print(f"< Input line: {ip_line}")
    possible_ips = ip_partititons(ip_line)

    for i, ip in enumerate(filter(is_valid_ip, possible_ips)):
        print(f"possible output {i + 1}: {ip}")


if __name__ == '__main__':
    for line in fileinput.input():
        main(line)

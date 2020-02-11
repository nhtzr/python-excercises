import fileinput
import sys
from typing import Iterator

from .op import generate_receipt, receipt_repr
from .parse import parse_good_item_line


def main(line_input: Iterator[str], output=sys.stdout):
    items = (parse_good_item_line(line) for line in line_input)
    receipt = generate_receipt(items)
    print(receipt_repr(receipt), file=output)


if __name__ == '__main__':
    main(fileinput.input())

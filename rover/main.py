import fileinput
from typing import Iterator

from rover.op import execute_instructions
from .data import Coordinate
from .parse import parse_landscape_topright_coordinate, parse_rover_state, \
    parse_instruction_line


def main(line_input: Iterator[str], output=None, stderr=None):
    landscape_bottomleft = Coordinate(0, 0)
    landscape_topright = parse_landscape_topright_coordinate(next(line_input))
    # Todo? Validate rover coordinates using ^

    try:
        while True:
            rover_state = parse_rover_state(next(line_input))
            rover_instructions = parse_instruction_line(next(line_input))
            print(f"rover_state={rover_state}", file=stderr)
            print(f"rover_instructions={rover_instructions}", file=stderr)

            final_rover_state = execute_instructions(rover_state, rover_instructions, stderr=stderr)
            print(
                f"{final_rover_state.coordinate.x} "
                f"{final_rover_state.coordinate.y} "
                f"{final_rover_state.direction.flag}",
                file=output)
    except StopIteration:
        pass


if __name__ == "__main__":
    main(fileinput.input())

from .data import Instruction, Coordinate, RoverState, Direction, VALID_INSTRUCTIONS, \
    VALID_DIRECTIONS


class InvalidInstructionError(Exception):
    pass


def validate_instruction(i: Instruction):
    if i.flag not in VALID_INSTRUCTIONS:
        raise InvalidInstructionError(f"Only valid instructions are {VALID_INSTRUCTIONS}, instead "
                                      f"got {i.flag}")
    return i


def parse_instruction_line(line: str):
    instructions = (Instruction(flag) for flag in line)
    # instructions = list(instructions)
    # print(f"instructions={instructions}", file=stderr)
    valid_instructions = (validate_instruction(instruction) for instruction in instructions)
    # valid_instructions = list(valid_instructions)
    return valid_instructions


class InvalidLandscapeLine(Exception):
    pass


class InvalidRoverState(Exception):
    pass


def parse_landscape_topright_coordinate(line: str):
    tokens = line.split(' ')
    if len(tokens) != 2:
        raise InvalidLandscapeLine(
            f"Expected two integer coordinates (x y). Got \"{repr(line)}\"")
    try:
        return Coordinate(
            int(tokens[0], base=10),
            int(tokens[1], base=10))
    except ValueError as e:
        raise InvalidLandscapeLine(
            f"Expected two integer coordinates (x y). Got \"{repr(line)}\"") from e


def parse_rover_state(line: str):
    tokens = line.split(' ')
    if len(tokens) != 3:
        raise InvalidRoverState(
            f"Expected two integers and a direction (x y direction). Got \"{repr(line)}\"")
    if tokens[2] not in VALID_DIRECTIONS:
        raise InvalidLandscapeLine(
            f"Expected valid direction ({VALID_DIRECTIONS}). Got {tokens[2]}")
    try:
        return RoverState(
            Coordinate(
                int(tokens[0], base=10),
                int(tokens[1], base=10)),
            Direction(tokens[2]))
    except ValueError as e:
        raise InvalidRoverState(
            f"Expected two integers and a direction (x y direction). Got \"{repr(line)}\"") from e

from typing import NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int


class Direction(NamedTuple):
    flag: str


class Instruction(NamedTuple):
    flag: str


class RoverState(NamedTuple):
    coordinate: Coordinate
    direction: Direction


VALID_INSTRUCTIONS = ('M', 'L', 'R')
VALID_DIRECTIONS = ('N', 'E', 'S', 'W')  # In R instruction order
DIRECTION_TO_COORDINATE_ID = {
    'N': Coordinate(0, 1),
    'E': Coordinate(1, 0),
    'S': Coordinate(0, -1),
    'W': Coordinate(-1, 0),
}

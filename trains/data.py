from typing import NamedTuple, List


class Hop(NamedTuple):
    origin: str
    dest: str


class Edge(NamedTuple):
    origin: str
    dest: str
    distance: int


class Route(NamedTuple):
    edges: List[Edge]
    distance: int
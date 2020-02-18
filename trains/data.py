from typing import NamedTuple, List, Dict


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


class Graph(NamedTuple):
    by_hop: Dict[Hop, Edge]
    by_origin: Dict[str, List[Edge]]

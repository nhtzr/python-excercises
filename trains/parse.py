from collections import defaultdict
from typing import Dict, List

from trains.data import Hop, Edge, Graph


def parse_graph(graph_line: str):
    graph: Dict[Hop, Edge] = dict()
    by_origin: Dict[str, List[Edge]] = defaultdict(list)
    graph_line = graph_line
    edge_tokens = graph_line.split(', ')
    for token in edge_tokens:
        origin, dest, *distance = list(token)
        edge = Edge(origin, dest, int(str.join('', distance)))

        graph[Hop(origin, dest)] = edge
        by_origin[origin].append(edge)
    return Graph(graph, by_origin)

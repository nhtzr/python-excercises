import sys
from typing import Dict, Iterable

from trains.data import Hop, Route
from trains.route import has_duplicate_stops


def distance_of(*nodes, graph):
    if len(nodes) < 2:
        return 'NO SUCH ROUTE'

    route_distance = 0
    curr_node, *remaining_nodes = nodes
    for next_node in remaining_nodes:
        edge = graph.get(Hop(curr_node, next_node), None)
        if edge is None:
            return 'NO SUCH ROUTE'
        route_distance += edge.distance
        curr_node = next_node
    return str(route_distance)


def shortest_route_length(first_origin, final_dest, graph: Dict):
    raise NotImplementedError()

    distance_from_origin = dict((node, sys.maxsize)
                                for hop in graph.keys()
                                for node in hop)
    # Distance to each node in graph from origin
    distance_from_origin[first_origin] = 0


def all_routes(origin: str, final_stop: str, by_origin=None) -> Iterable[Route]:
    next_routes = list(
        Route([edge], edge.distance)
        for edge in (by_origin[origin]))

    while len(next_routes) > 0:
        curr_routes = next_routes
        next_routes = list()
        for curr_route in curr_routes:
            latest_stop = curr_route.edges[-1].dest
            curr_options = by_origin[latest_stop]
            for next_edge in curr_options:
                next_route = Route(
                    [*curr_route.edges, next_edge],
                    curr_route.distance + next_edge.distance)
                if next_edge.dest == final_stop:
                    yield next_route
                if not has_duplicate_stops(next_route):
                    next_routes.append(next_route)
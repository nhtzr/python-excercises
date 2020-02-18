import fileinput
from typing import Iterator, Iterable, Dict

import sys

from trains.data import Hop, Route, Graph
from trains.parse import parse_graph
from trains.route import has_duplicate_stops, max_3_stops, has_4_stops


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


def main(line_input: Iterator[str], output=sys.stdout):
    graph: Graph = parse_graph(next(line_input))

    print(distance_of('A', 'B', 'C', graph=graph.by_hop), file=output)
    print(distance_of('A', 'D', graph=graph.by_hop), file=output)
    print(distance_of('A', 'D', 'C', graph=graph.by_hop), file=output)
    print(distance_of('A', 'E', 'B', 'C', 'D', graph=graph.by_hop), file=output)
    print(distance_of('A', 'E', 'D', graph=graph.by_hop), file=output)

    # The number of trips starting at C and ending at C with a maximum of 3 stops.
    # In the sample data below,
    # there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
    print(len(list(filter(max_3_stops, all_routes(
        'C', 'C', by_origin=graph.by_origin
    )))), file=output)

    # The number of trips starting at A and ending at C with exactly 4 stops.
    # In the sample data below,
    # there are three such trips: A to C (via B,C,D);
    #   A to C (via D,C,D); and A to C (via D,E,B).
    print(len(list(filter(has_4_stops, all_routes(
        'A', 'C', by_origin=graph.by_origin
    )))), file=output)

    # print(shortest_route_length('A', 'C', graph=graph), file=output)
    # print(shortest_route_length('B', 'B', graph=graph), file=output)
    # print(len(list(filter(is_shorter_than_30, all_routes(
    #     'C', 'C', graph=graph
    # )))), file=output)


if __name__ == '__main__':
    main(fileinput.input())

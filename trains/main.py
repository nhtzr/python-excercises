import fileinput
from collections import defaultdict
from typing import Iterator, Dict, Iterable, List

import sys

from trains.data import Hop, Edge, Route
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


def shortest_route_length(*nodes, graph):
    raise NotImplementedError()
    curr_node, *remaining_nodes = nodes
    for next_node in remaining_nodes:
        edge = graph.get(Hop(curr_node, next_node), None)
        if edge is None:
            return 'NO SUCH ROUTE'


def all_routes(origin: str, final_stop: str, graph: Dict[Hop, Edge],
               edges_by_origin=None) -> Iterable[Route]:
    edges_by_origin = gen_edges_by_origin(graph) if edges_by_origin is None else edges_by_origin
    next_routes = list(
        Route([edge], edge.distance)
        for edge in (edges_by_origin[origin]))

    while len(next_routes) > 0:
        curr_routes = next_routes
        next_routes = list()
        for curr_route in curr_routes:
            latest_stop = curr_route.edges[-1].dest
            curr_options = edges_by_origin[latest_stop]
            for next_edge in curr_options:
                next_route = Route(
                    [*curr_route.edges, next_edge],
                    curr_route.distance + next_edge.distance)
                if next_edge.dest == final_stop:
                    yield next_route
                if not has_duplicate_stops(next_route):
                    next_routes.append(next_route)


def gen_edges_by_origin(graph: Dict[Hop, Edge]) -> Dict[str, List[Edge]]:
    routes_by_origin: Dict[str, List[Edge]] = defaultdict(list)
    for (hop, edge) in graph.items():
        routes_by_origin[hop.origin].append(edge)
    return routes_by_origin


def main(line_input: Iterator[str], output=sys.stdout):
    graph: Dict[Hop, Edge] = dict()
    graph_line = next(line_input)
    edge_tokens = graph_line.split(', ')
    for token in edge_tokens:
        origin, dest, *distance = list(token)
        graph[Hop(origin, dest)] = Edge(origin, dest, int(str.join('', distance)))

    print(distance_of('A', 'B', 'C', graph=graph), file=output)
    print(distance_of('A', 'D', graph=graph), file=output)
    print(distance_of('A', 'D', 'C', graph=graph), file=output)
    print(distance_of('A', 'E', 'B', 'C', 'D', graph=graph), file=output)
    print(distance_of('A', 'E', 'D', graph=graph), file=output)

    by_origin = gen_edges_by_origin(graph)
    # The number of trips starting at C and ending at C with a maximum of 3 stops.
    # In the sample data below,
    # there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
    print(len(list(filter(max_3_stops, all_routes(
        'C', 'C', graph=graph, edges_by_origin=by_origin
    )))), file=output)

    # The number of trips starting at A and ending at C with exactly 4 stops.
    # In the sample data below,
    # there are three such trips: A to C (via B,C,D);
    #   A to C (via D,C,D); and A to C (via D,E,B).
    print(len(list(filter(has_4_stops, all_routes(
        'A', 'C', graph=graph, edges_by_origin=by_origin
    )))), file=output)

    # print(shortest_route_length('A', 'C', graph=graph), file=output)
    # print(shortest_route_length('B', 'B', graph=graph), file=output)
    # print(len(list(filter(is_shorter_than_30, all_routes(
    #     'C', 'C', graph=graph
    # )))), file=output)


if __name__ == '__main__':
    main(fileinput.input())

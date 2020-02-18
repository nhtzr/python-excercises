import fileinput
from typing import Iterator

import sys

from trains.data import Graph
from trains.graph import distance_of, all_routes
from trains.parse import parse_graph
from trains.route import max_3_stops, has_4_stops


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

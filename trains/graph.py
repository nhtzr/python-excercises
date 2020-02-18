from queue import PriorityQueue
from typing import Iterable, Tuple

import sys

from trains.data import Hop, Route, Graph
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


def shortest_route_length(first_origin: str, final_dest: str, graph: Graph):
    distances = dict((node, sys.maxsize)
                     for hop in graph.by_hop.keys()
                     for node in hop)

    visited = set()
    queue: PriorityQueue[Tuple[int, str]] = PriorityQueue()
    # distances[first_origin] = 0  # Distance to each node in graph from origin
    #                              However we are expected to give the route with one hop at least
    #                              So we are leaving distance from output as infinity
    #                              And still seed the queue with the origin.
    #                              (Seed distance / Priority number <0> can be ignored)
    queue.put((0, first_origin))
    while not queue.empty():
        curr_distance, curr_origin = queue.get()
        if curr_origin in visited:
            continue
        next_edges = graph.by_origin[curr_origin]
        for next_edge in next_edges:
            next_dest = next_edge.dest
            new_distance = curr_distance + next_edge.distance
            old_distance = distances[next_dest]
            if new_distance < old_distance:
                distances[next_dest] = new_distance
                queue.put((new_distance, next_edge.dest))
        visited.add(curr_origin)

    route_length = distances.get(final_dest, None)
    if route_length is None:
        return 'NO SUCH ROUTE'
    return route_length


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

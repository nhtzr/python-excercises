from typing import List

from trains.data import Route, Edge


def has_duplicate_stops(route: Route):
    edges = route.edges
    if len(edges) < 2:
        return False
    hops = [edges[0].origin, *(hop.dest for hop in edges)]
    return len(set(hops)) != len(hops)


def is_shorter_than_30(route: Route):
    return route.distance < 30


def max_3_stops(route: Route):
    return len(route.edges) <= 3


def has_4_stops(route: Route):
    return len(route.edges) == 4

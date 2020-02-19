import unittest

from trains.data import Route, Edge
from trains.graph import shortest_route_length, all_routes
from trains.parse import parse_graph


class GraphTestCase(unittest.TestCase):
    def test_shortest_path_1(self):
        graph = parse_graph('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
        actual = shortest_route_length('B', 'B', graph=graph)
        expected = 9
        self.assertEqual(expected, actual)

    def test_shortest_path_2(self):
        graph = parse_graph('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
        actual = shortest_route_length('A', 'C', graph=graph)
        expected = 9
        self.assertEqual(expected, actual)

    def test_all_routes_1(self):
        graph = parse_graph('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
        actual = all_routes('C', 'C', graph.by_origin)
        actual_ = [*actual]
        # there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
        self.assertIn(
            Route(edges=[
                Edge('C', 'D', 8),
                Edge('D', 'C', 8)
            ], distance=16),
            actual_)
        self.assertIn(
            Route(edges=[
                Edge('C', 'E', 2),
                Edge('E', 'B', 3),
                Edge('B', 'C', 4)
            ], distance=9),
            actual_)

    def test_all_routes_2(self):
        graph = parse_graph('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
        actual = all_routes('A', 'C', graph.by_origin)
        # there are three such trips: A to C (via B,C,D);
        #   A to C (via D,C,D); and A to C (via D,E,B).
        actual_ = [*actual]
        self.assertIn(
            Route(edges=[
                Edge('A', 'B', 5),
                Edge('B', 'C', 4),
                Edge('C', 'D', 8),
                Edge('D', 'C', 8),
            ], distance=25),
            actual_)
        self.assertIn(
            Route(edges=[
                Edge('A', 'D', 5),
                Edge('D', 'C', 8),
                Edge('C', 'D', 8),
                Edge('D', 'C', 8),
            ], distance=29),
            actual_)
        self.assertIn(
            Route(edges=[
                Edge('A', 'D', 5),
                Edge('D', 'E', 6),
                Edge('E', 'B', 3),
                Edge('B', 'C', 4),
            ], distance=18),
            actual_)


if __name__ == '__main__':
    unittest.main()

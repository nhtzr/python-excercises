import unittest

from trains.graph import shortest_route_length
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


if __name__ == '__main__':
    unittest.main()

import unittest
from io import StringIO

from trains.main import main


class TrainsTestCase(unittest.TestCase):
    def test_main_1(self):
        output_io = StringIO()
        given = iter(['AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'])
        main(given, output=output_io)
        output = output_io.getvalue()
        self.assertEqual(
            output,
            '9\n'
            '5\n'
            '13\n'
            '22\n'
            'NO SUCH ROUTE\n'
            '2\n'
            '3\n'
            '9\n'
            '9\n'
            '7\n'
        )


if __name__ == '__main__':
    unittest.main()

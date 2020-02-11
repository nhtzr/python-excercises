import unittest
from io import StringIO

from rover.main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        given = ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']
        expected = '1 3 N\n5 1 E\n'
        output = StringIO()

        main(iter(given), output=output)

        self.assertEqual(output.getvalue(), expected)
        output.close()


if __name__ == '__main__':
    unittest.main()

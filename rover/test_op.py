import unittest

from rover.data import RoverState, Coordinate, Direction, Instruction
from rover.op import rotate


class TestOp(unittest.TestCase):
    def test_rotate_r(self):
        output = rotate(
            RoverState(Coordinate(0, 0),
                       Direction('N')),
            Instruction('R'))
        self.assertEqual(output, Direction('E'))

    def test_rotate_l(self):
        output = rotate(
            RoverState(Coordinate(0, 0),
                       Direction('N')),
            Instruction('L'))
        self.assertEqual(output, Direction('W'))

    def test_rotate_3(self):
        given_state = RoverState(Coordinate(0, 0), Direction('N'))

        output = rotate(given_state,
                        Instruction('L'))
        self.assertEqual(output, Direction('W'))

        output = rotate(given_state._replace(direction=Direction('W')),
                        Instruction('L'))
        self.assertEqual(
            output,
            Direction('S'))

        output = rotate(given_state._replace(direction=Direction('S')),
                        Instruction('L'))
        self.assertEqual(
            output,
            Direction('E'))

        output = rotate(given_state._replace(direction=Direction('E')),
                        Instruction('L'))
        self.assertEqual(
            output,
            Direction('N'))


if __name__ == '__main__':
    unittest.main()

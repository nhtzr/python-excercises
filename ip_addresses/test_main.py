import unittest

from ip_addresses.main import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        main("1921681254")
        main('1111')


if __name__ == '__main__':
    unittest.main()

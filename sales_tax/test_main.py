import unittest
from io import StringIO

from sales_tax.main import main


class MainTestCase(unittest.TestCase):
    def test1(self):
        output_io = StringIO()
        given = iter(['1 book at 12.49',
                      '1 music CD at 14.99',
                      '1 chocolate bar at 0.85'])
        main(given, output=output_io)
        output = output_io.getvalue()
        output_io.close()

        self.assertEqual(
            output,
            '1 book: 12.49\n'
            '1 music CD: 16.49\n'
            '1 chocolate bar: 0.85\n'
            'Sales Taxes: 1.50\n'
            'Total: 29.83\n'
        )

    def test2(self):
        output_io = StringIO()
        given = iter(['1 imported box of chocolates at 10.00',
                      '1 imported bottle of perfume at 47.50'])
        main(given, output=output_io)
        output = output_io.getvalue()
        output_io.close()
        self.assertEqual(
            output,
            '1 imported box of chocolates: 10.50\n'
            '1 imported bottle of perfume: 54.65\n'
            'Sales Taxes: 7.65\n'
            'Total: 65.15\n'
        )

    def test3(self):
        output_io = StringIO()
        given = iter(['1 imported bottle of perfume at 27.99',
                      '1 bottle of perfume at 18.99',
                      '1 packet of headache pills at 9.75',
                      '1 imported box of chocolates at 11.25'])
        main(given, output=output_io)
        output = output_io.getvalue()
        output_io.close()
        self.assertEqual(
            output,
            '1 imported bottle of perfume: 32.19\n'
            '1 bottle of perfume: 20.89\n'
            '1 packet of headache pills: 9.75\n'
            '1 imported box of chocolates: 11.85\n'
            'Sales Taxes: 6.70\n'
            'Total: 74.68\n'
        )


if __name__ == '__main__':
    unittest.main()

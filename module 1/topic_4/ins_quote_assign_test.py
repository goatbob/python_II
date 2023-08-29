import unittest
from insurance_quote_assignment import ins_rate_calc


class MyTestCase(unittest.TestCase):

    def setUp(self):
        c = {"Name": "Kyle", "Age": "29", "Coverage": "full"}

    def tearDown(self):
        c = {}

    def test_quote(self):
        expected = 1745
        actual = ins_rate_calc("29", "full")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

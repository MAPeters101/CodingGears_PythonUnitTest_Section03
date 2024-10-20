import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers(self):
        result = calculator.calc_add(-10, -20)
        self.assertEqual(result, -30)


class TestCalculator2(unittest.TestCase):
    def test_add_functionality2(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers2(self):
        result = calculator.calc_add(-10, -20)
        self.assertEqual(result, -30)



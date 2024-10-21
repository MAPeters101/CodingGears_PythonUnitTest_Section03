# Topics: Two classes

import unittest
from unit_testing_02.calculator_v3 import Calculator


class TestCalculatorAddFunctionality(unittest.TestCase):
    def setUp(self):
        print("setUp invoked!")

    def tearDown(self):
        print("tearDown invoked!")

    def test_add_two_positive_numbers(self):
        print(">>> test_add_two_positive_numbers")
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 300)

    def test_add_one_positive_and_one_negative(self):
        print(">>> test_add_one_positive_and_one_negative")
        calc = Calculator(50, -90)
        result = calc.calc_add()
        self.assertEqual(result, -40)

    def test_add_two_negative_numbers(self):
        print(">>> test_add_two_negative_numbers")
        calc = Calculator(-10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -30)

    def test_add_two_positive_decimal_numbers(self):
        print(">>> test_add_two_positive_decimal_numbers")
        calc = Calculator(10.55, 20.97)
        result = calc.calc_add()
        self.assertEqual(result, 31.52)





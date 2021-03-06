import unittest
from lab3.rpn.reverse_polish_notation import ReversePolishNotation


class TestReversePolishNotation(unittest.TestCase):
    def test_convert_simple_expresion(self):
        # given
        expresion = '1 +2'
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '1 2 +'
        self.assertEqual(expected, result)

    def test_explain_multiline_simple_expresion(self):
        # given
        expresion = """1+
        2
        """
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '1 2 +'
        self.assertEqual(expected, result)

    def test_convert_complex_expresion(self):
        # given
        expresion = ' (4-2)*(2+3)-5'
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '4 2 - 2 3 + * 5 -'
        self.assertEqual(expected, result)

    def test_convert_complex_multiline_expresion(self):
        # given
        expresion = """(4-2)
        *(2+3)-5"""
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '4 2 - 2 3 + * 5 -'
        self.assertEqual(expected, result)

    def test_convert__expresion_with_nested_parentheses(self):
        # given
        expresion = '(4-(2 + 12))*(2+3)-5'
        # when
        result = ReversePolishNotation(expresion).convert(True)
        # then
        expected = '4 2 12 + - 2 3 + * 5 -'
        self.assertEqual(expected, result)

    def test_convert_complex_expresion_with_nested_parentheses(self):
        # given
        expresion = '[(9 - 2) * 3 - (9 - 3)^2 / (2 * 3)] * (6 - 4)'
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '9 2 - 3 * 9 3 - 2 ^ 2 3 * / - 6 4 - *'
        self.assertEqual(expected, result)

    def test_calculate_simple_expresion(self):
        # given
        expresion = '3 * 8 - 6 / 3'
        # when
        result = ReversePolishNotation(expresion).calculate()
        # then
        self.assertEqual(22., result)

    def test_calculate_simple_expresion_exp(self):
        # given
        expresion = '3 * 8 - 6 / 3'
        # when
        result = ReversePolishNotation(expresion).calculate(True)
        # then
        self.assertEqual(22., result)

    def test_calculate_complex_expresion_with_nested_parentheses(self):
        # given
        expresion = '[ (9 - 2) * 3 - (9 - 3) ^ 2 / (2 * 3)] * (6 - 4)'
        # when
        result = ReversePolishNotation(expresion).calculate()
        # then
        expected = 30.
        self.assertEqual(expected, result)

    def test_calculate_complex_expresion_with_nested_and_curly_parentheses(self):
        # given
        expresion = '{[(9-7)+(2+3)]-(7-4)}*[(7-5)*3-2]'
        # when
        result = ReversePolishNotation(expresion).calculate()
        # then
        expected = 16.
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

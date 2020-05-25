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
        expresion = ' (4-(2 + 12)*(2+3)-5'
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '4 2 12 + - 2 3 + * 5 -'
        self.assertEqual(expected, result)

    def test_convert_complex_expresion_with_nested_parentheses(self):
        # given
        expresion = '[(9-2)*3-(9-3)^2/(2*3)]*(6-4)'
        # when
        result = ReversePolishNotation(expresion).convert()
        # then
        expected = '9 2 - 3 * 9 3 - 2 ^ 2 3 * / 6 4 - *'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

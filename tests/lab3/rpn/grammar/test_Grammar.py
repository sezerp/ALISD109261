import unittest
from lab3.rpn.grammar.Lexer import SimpleMathGrammar, TokenKind, Token
from lab3.rpn.grammar.Lexer import Precedence1, Precedence2


class TestPrecedence(unittest.TestCase):
    def test_equal(self):
        # given
        p1 = Precedence1()
        p11 = Precedence1()
        p2 = Precedence2()
        # then
        self.assertEqual(p1 == p2, False)
        self.assertEqual(p1 == p11, True)

    def test_gt(self):
        # given
        p1 = Precedence1()
        p2 = Precedence2()
        # then
        self.assertEqual(p1 > p2, False)
        self.assertEqual(p2 > p1, True)

    def test_ls(self):
        # given
        p1 = Precedence1()
        p11 = Precedence1()
        p2 = Precedence2()
        # then
        self.assertEqual(p2 < p1, False)
        self.assertEqual(p1 < p2, True)

    def test_ge(self):
        # given
        p1 = Precedence1()
        p11 = Precedence1()
        p2 = Precedence2()
        # then
        self.assertEqual(p1 >= p2, False)
        self.assertEqual(p1 >= p11, True)
        self.assertEqual(p2 >= p1, True)

    def test_le(self):
        # given
        p1 = Precedence1()
        p11 = Precedence1()
        p2 = Precedence2()
        # then
        self.assertEqual(p2 <= p1, False)
        self.assertEqual(p1 <= p11, True)
        self.assertEqual(p1 <= p2, True)


class TestSimpleMathGrammar(unittest.TestCase):
    def test_tokenize_simple_expresion(self):
        # given
        expresion = '1 +2'
        # when
        result = list(SimpleMathGrammar().tokenize(expresion))
        # then
        expected = [
            Token(TokenKind.NUMBER, '1', 1, 0),
            Token(TokenKind.OP, '+', 1, 2),
            Token(TokenKind.NUMBER, '2', 1, 3)
        ]

        self.assertEqual(expected, result)

    def test_tokenize_multiline_expresion(self):
        # given
        expresion = """1 + 3
        - 3
        """
        # when
        result = list(SimpleMathGrammar().tokenize(expresion))
        # then
        expected = [
            Token(type=TokenKind.NUMBER, value='1', line=1, column=0),
            Token(type=TokenKind.OP, value='+', line=1, column=2),
            Token(type=TokenKind.NUMBER, value='3', line=1, column=4),
            Token(type=TokenKind.OP, value='-', line=2, column=8),
            Token(type=TokenKind.NUMBER, value='3', line=2, column=10)
        ]
        self.assertEqual(expected, result)

    def test_tokenizer_complex_expresion(self):
        # given
        expresion = '[(9-2)*3-(9-3)^2/(2*3)]*(6-4)'
        # when
        result = list(SimpleMathGrammar().tokenize(expresion))
        # then
        expected = [
             Token(type=TokenKind.SEPARATOR, value='[', line=1, column=0),
             Token(type=TokenKind.SEPARATOR, value='(', line=1, column=1),
             Token(type=TokenKind.NUMBER, value='9', line=1, column=2),
             Token(type=TokenKind.OP, value='-', line=1, column=3),
             Token(type=TokenKind.NUMBER, value='2', line=1, column=4),
             Token(type=TokenKind.SEPARATOR, value=')', line=1, column=5),
             Token(type=TokenKind.OP, value='*', line=1, column=6),
             Token(type=TokenKind.NUMBER, value='3', line=1, column=7),
             Token(type=TokenKind.OP, value='-', line=1, column=8),
             Token(type=TokenKind.SEPARATOR, value='(', line=1, column=9),
             Token(type=TokenKind.NUMBER, value='9', line=1, column=10),
             Token(type=TokenKind.OP, value='-', line=1, column=11),
             Token(type=TokenKind.NUMBER, value='3', line=1, column=12),
             Token(type=TokenKind.SEPARATOR, value=')', line=1, column=13),
             Token(type=TokenKind.OP, value='^', line=1, column=14),
             Token(type=TokenKind.NUMBER, value='2', line=1, column=15),
             Token(type=TokenKind.OP, value='/', line=1, column=16),
             Token(type=TokenKind.SEPARATOR, value='(', line=1, column=17),
             Token(type=TokenKind.NUMBER, value='2', line=1, column=18),
             Token(type=TokenKind.OP, value='*', line=1, column=19),
             Token(type=TokenKind.NUMBER, value='3', line=1, column=20),
             Token(type=TokenKind.SEPARATOR, value=')', line=1, column=21),
             Token(type=TokenKind.SEPARATOR, value=']', line=1, column=22),
             Token(type=TokenKind.OP, value='*', line=1, column=23),
             Token(type=TokenKind.SEPARATOR, value='(', line=1, column=24),
             Token(type=TokenKind.NUMBER, value='6', line=1, column=25),
             Token(type=TokenKind.OP, value='-', line=1, column=26),
             Token(type=TokenKind.NUMBER, value='4', line=1, column=27),
             Token(type=TokenKind.SEPARATOR, value=')', line=1, column=28)
        ]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

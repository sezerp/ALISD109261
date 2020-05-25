from typing import Generator
from typing import NamedTuple
import re


class TokenKind:
    NUMBER = 'NUMBER'
    NEWLINE = 'NEWLINE'
    SKIP = 'SKIP'
    MISMATCH = 'MISMATCH'
    SEPARATOR = 'SEPARATOR'
    OP = 'OPERATOR'


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


class Associativity:
    def __init__(self):
        pass


class EmptyAssociativity(Associativity):
    def __init__(self):
        super().__init__()


class LeftRightAssociativity(Associativity):
    def __init__(self):
        super().__init__()


class RightLeftAssociativity(Associativity):
    def __init__(self):
        super().__init__()


class UnaryLeftAssociativity(Associativity):
    def __init__(self):
        super().__init__()


class UnaryRightAssociativity(Associativity):
    def __init__(self):
        super().__init__()


class AssociativityTypes:
    LEFT_RIGHT = LeftRightAssociativity()
    RIGHT_LEFT = RightLeftAssociativity()
    UNARY_LEFT = UnaryLeftAssociativity()
    UNARY_RIGHT = UnaryRightAssociativity()


class Grammar:
    def __init__(self):
        pass


class MathGrammar(Grammar):

    def __init__(self):
        super().__init__()

    def tokenize(self, expresion) -> Generator:
        raise NotImplementedError()

    @classmethod
    def get_operands_precedence(cls, token: Token):
        raise NotImplementedError()

    @classmethod
    def get_operand_associativity(cls, token: Token) -> Associativity:
        raise NotImplementedError()

    @classmethod
    def operands_comparator(cls, op1: Token, op2: Token) -> int:
        raise NotImplementedError


class Precedence:
    def __init__(self, precedence_number: int):
        self.precedence_number = precedence_number

    def __add__(self, other: 'Precedence'):
        return self.precedence_number + other.precedence_number

    def __sub__(self, other: 'Precedence'):
        return self.precedence_number - other.precedence_number

    def __eq__(self, other: 'Precedence'):
        return self.precedence_number == other.precedence_number

    def __gt__(self, other: 'Precedence'):
        return self.precedence_number > other.precedence_number

    def __lt__(self, other: 'Precedence'):
        return self.precedence_number < other.precedence_number

    def __ge__(self, other: 'Precedence'):
        return self.precedence_number >= other.precedence_number

    def __le__(self, other: 'Precedence'):
        return self.precedence_number <= other.precedence_number


class Precedence0(Precedence):
    def __init__(self):
        super().__init__(0)


class Precedence1(Precedence):
    def __init__(self):
        super().__init__(1)


class Precedence2(Precedence):
    def __init__(self):
        super().__init__(2)


class Precedence3(Precedence):
    def __init__(self):
        super().__init__(3)


class Operand:
    def __init__(self, precedence: Precedence, associativity: Associativity):
        self.precedence = precedence
        self.associativity = associativity


class Operand0(Operand):
    def __init__(self):
        super().__init__(Precedence0(), EmptyAssociativity())


class UnaryOperand(Operand):
    def __init__(self, token, grammar: MathGrammar):
        precedence = grammar.get_operands_precedence(token=token)
        associativity = grammar.get_operand_associativity(token=token)
        super().__init__(precedence, associativity)


class Operand2(Operand):
    def __init__(self, token: Token, grammar: MathGrammar):
        priority = grammar.get_operands_precedence(token)
        binding = grammar.get_operand_associativity(token)
        super().__init__(priority, binding)


class SimpleMathGrammar(MathGrammar):
    """SimpleMathGrammar
    Describe simple grammar allowed parsing and tokenize simple math expressions
    """
    OPERANDS_TO_PRECEDENCE = {
        '+': Precedence1(),
        '-': Precedence1(),
        '/': Precedence2(),
        '*': Precedence2(),
        '^': Precedence3(),
    }
    OPERATOR_TO_ASSOCIATIVITY = {
        '+': LeftRightAssociativity(),
        '-': LeftRightAssociativity(),
        '/': RightLeftAssociativity(),
        '*': RightLeftAssociativity(),
        '^': LeftRightAssociativity(),
    }

    PARENTHESIS = {'(', ')', '[', ']'}
    TOKEN_SPECIFICATION = [
        (TokenKind.NUMBER, r'\d+(\.\d*)?'),  # Integer or decimal number
        (TokenKind.SEPARATOR, r'[()\[\]]'),  # Identifiers
        (TokenKind.OP, r'[+\-*/^]'),  # Arithmetic operators
        (TokenKind.NEWLINE, r'\n'),  # Line endings
        (TokenKind.SKIP, r'[ \t]+'),  # Skip over spaces and tabs
        (TokenKind.MISMATCH, r'.'),  # Any other character
    ]
    TOKEN_REGEX = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION)

    def __init__(self):
        super().__init__()
        pass

    def tokenize(self, expresion) -> Generator:
        line_num = 1
        line_start = 0
        for mo in re.finditer(self.TOKEN_REGEX, expresion):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start
            if kind == TokenKind.NEWLINE:
                line_start = mo.end()
                line_num += 1
                continue
            elif kind == TokenKind.SKIP:
                continue
            elif kind == TokenKind.MISMATCH:
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            yield Token(kind, value, line_num, column)

    @classmethod
    def get_operands_precedence(cls, op: Token):
        """
        return priority index used for comparing operator priority, higher value is higher precedence
        :param op:
        :return: operand precedence as int
        Raises:
            ValueError: when given token `op` is not a operand.
        """
        if op.type != TokenKind.OP:
            raise ValueError(f'The op must be Token of operand type')

        return cls.OPERANDS_TO_PRECEDENCE[op.value]

    @classmethod
    def get_operand_associativity(cls, op: Token) -> Associativity:
        if op.type != TokenKind.OP or op.value not in cls.OPERATOR_TO_ASSOCIATIVITY:
            raise ValueError(f'The op must be Token of operand type')
        return cls.OPERATOR_TO_ASSOCIATIVITY[op.value]

    @classmethod
    def operands_comparator(cls, op1: Token, op2: Token) -> int:
        """
        Compare operands precedence
        :param op1:
        :param op2:
        :return: int
            return < 0 =>  op1 < op2
            return = 0 =>  op1 == op2
            return > 0 =>  op1 > op2
        """
        return cls.get_operands_precedence(op1) - cls.get_operands_precedence(op2)

    @classmethod
    def token_to_operand(cls, token: Token) -> Operand2:
        if token.type != TokenKind.OP:
            raise ValueError(f'The op must be Token of operand type but given {token}')

        return Operand2(token, cls)
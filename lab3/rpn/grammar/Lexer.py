from typing import Generator, List
from typing import NamedTuple
import re


class TokenKind:
    OPERAND = 'NUMBER'
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

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __eq__(self, other: 'Associativity') -> bool:
        if other is None:
            return False

        return other.__str__() == self.__str__()


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
    """
    Operand is representation of algebraic statement
    Minimal requirements for operand are:
        - need to has identity element
    """
    def __init__(self, number_arguments, precedence: Precedence, associativity: Associativity, identity_element, operator):
        self.precedence = precedence
        self.associativity = associativity
        self.e = identity_element
        self.operator = operator
        self.number_arguments = number_arguments

    def apply(self, operands: List):
        if self.associativity == LeftRightAssociativity():
            return self._left_right(operands)
        elif self.associativity == RightLeftAssociativity():
            return self._right_left(operands)
        else:
            raise ValueError(f'The {self.associativity} for given operator `{self.operator}` not implemented')

    def _left_right(self, operands):
        result = self.e
        for op in operands:
            result = self.operator(op, result)
        return result

    def _right_left(self, operands):
        result = self.e
        for op in operands:
            result = self.operator(result, op)
        return result


class Operand0(Operand):
    def __init__(self):
        super().__init__(0, Precedence0(), EmptyAssociativity(), 0, lambda a, b: 0)


class UnaryOperand(Operand):
    def __init__(self, token, grammar: MathGrammar):
        precedence = grammar.get_operands_precedence(token=token)
        associativity = grammar.get_operand_associativity(token=token)
        super().__init__(1, precedence, associativity)


class Operand2(Operand):
    def __init__(self, priority, associativity, identity_element, operator):
        super().__init__(2, priority, associativity, identity_element, operator)


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
        '/': LeftRightAssociativity(),
        '*': LeftRightAssociativity(),
        '^': LeftRightAssociativity(),
    }

    OPERATOR_TO_FUNCTION = {
        '+': lambda a, b: float(a).__add__(b),
        '-': lambda a, b: float(a).__sub__(b),
        '/': lambda a, b: a / b,
        '*': lambda a, b: float(a).__mul__(b),
        '^': lambda a, b: float(a).__pow__(b),
    }

    OPERATOR_TO_IDENTITY_ELEMENT = {
        '+': 0,
        '-': 0,
        '/': 1,
        '*': 1,
        '^': 1,
    }

    PARENTHESIS = {'(', ')', '[', ']', '{', '}'}
    TOKEN_SPECIFICATION = [
        (TokenKind.OPERAND, r'\d+(\.\d*)?'),  # Integer or decimal number
        (TokenKind.SEPARATOR, r'[()\[\]\{\}]'),  # Identifiers
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
            ValueError: when given token `op` is not an operator.
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
    def get_operand_id_element(cls, op: Token):
        if op.type != TokenKind.OP or op.value not in cls.OPERATOR_TO_ASSOCIATIVITY:
            raise ValueError(f'The op must be Token of operand type')
        return cls.OPERATOR_TO_IDENTITY_ELEMENT[op.value]

    @classmethod
    def get_operator_function(cls, op: Token):
        if op.type != TokenKind.OP or op.value not in cls.OPERATOR_TO_ASSOCIATIVITY:
            raise ValueError(f'The op must be Token of operand type')
        return cls.OPERATOR_TO_FUNCTION[op.value]

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
    def token_to_operator(cls, token: Token) -> Operand2:
        if token.type != TokenKind.OP:
            raise ValueError(f'The operand must be Token of `OPERATOR` type but given {token}')

        priority = cls.get_operands_precedence(token)
        associativity = cls.get_operand_associativity(token)
        identity_element = cls.get_operand_id_element(token)
        operand = cls.get_operator_function(token)

        return Operand2(priority, associativity, identity_element, operand)

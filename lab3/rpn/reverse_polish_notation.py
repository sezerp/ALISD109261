from lab3.rpn.grammar.Lexer import SimpleMathGrammar, TokenKind, Operand0, Token
from collections import deque
from typing import List


class Step:

    def __init__(self):
        pass


class ReversePolishNotation:
    """ReversePolishNotation - class converting and explaining convert between standard math notation
    and reverse polish notation
    author:
        Pawel Zabczynski
    """
    _EXPLAIN_DELIMITER = ' '
    LEFT_P = {'(', '[', '{'}
    RIGHT_P = {')', ']', '}'}

    def __init__(self, expresion: str):
        self.expresion = expresion

    def convert(self, explain=False) -> str:
        """Convert `self.expresion` into expresion
            Do not support unary operations
            :param explain: boolean set to true to see in output explain each step
            Returns:
                :return: str
            Raises:
                 ValueError: If `self.expresion` is not valid math expresion.
        """
        smg = SimpleMathGrammar()
        stack = []
        que = deque()
        step = 1
        for t in smg.tokenize(self.expresion):
            if t.type == TokenKind.OPERAND:
                if stack and stack[-1].type == TokenKind.OP:
                    que.append(t)
                    operator = stack.pop()
                    que.append(operator)
                else:
                    que.append(t)
            elif t.type == TokenKind.SEPARATOR and t.value in self.LEFT_P:
                stack.append(t)
            elif t.type == TokenKind.SEPARATOR and t.value in self.RIGHT_P:
                # pop last operator from stack as long as not rich open parenthesis
                while stack and stack[-1].value not in self.LEFT_P:
                    operator = stack.pop()
                    que.append(operator)
                # remove from stack open parenthesis
                stack.pop()
            elif t.type == TokenKind.OP:
                o1 = SimpleMathGrammar.token_to_operator(t)
                o2 = SimpleMathGrammar.token_to_operator(stack[-1]) if stack and stack[-1].type == TokenKind.OP else Operand0()
                if o1.precedence > o2.precedence:
                    stack.append(t)
                elif stack and (o1.precedence < o2.precedence or o1.precedence == o2.precedence):
                    o = stack.pop()
                    que.append(o)
                    stack.append(t)
            if explain:
                print(f'step: {step} => {self._explain_step(que, stack)}')
                step += 1

        # moving
        for t in stack:
            if t.type not in TokenKind.SEPARATOR:
                que.append(t)
                if explain:
                    print(f'step: {step} => {self._explain_step(que, stack)}')
                    step += 1

        return self._que_mk_string(que)

    def calculate(self, explain = False) -> float:
        """
        Calculate given algebraic expresion
        :param explain: if set to `True` then will print step by stem explanation
        :return: result after calculation expresion
        """

        stc = []
        rpn_exp = self.convert(explain)
        smg = SimpleMathGrammar()
        step = 1
        print(rpn_exp)
        for t in smg.tokenize(rpn_exp):
            if t.type == TokenKind.OPERAND:
                stc.append(t.value)
                if explain:
                    print(f'step: {step} stack: {stc}, v: {t.value}')
                    step += 1
            elif t.type == TokenKind.OP:
                operator = SimpleMathGrammar.token_to_operator(t)
                operands = []
                for _ in range(operator.number_arguments):
                    operand = float(stc.pop())
                    operands.append(operand)
                sub_result = operator.apply(operands)
                stc.append(sub_result)
                if explain:
                    print(f'step: {step} stack: {stc} operator: {t.value} operands{operands} sub_result: {sub_result}')
                    step += 1
        return stc.pop()

    def explain(self) -> str:
        """Print all steps as values stored in que and stack
            Returns:
                :return: explanation as string
            Raises:
                 ValueError: If `self.expresion` is not valid math expresion.
        """

        return self.convert(explain=True)

    @staticmethod
    def _explain_step(que: deque, stack: List) -> str:
        que_values = '['
        stack_values = '['

        for t in que:
            que_values += t.value + ' '
        que_values += ']'

        for t in stack:
            stack_values += f'"{t.value}"' + ', '
        stack_values += ']'

        return f' queue: {que_values} stack: {stack_values}'

    def _que_mk_string(self, q: deque):
        result = ''

        result += f'{q.popleft().value}'
        for e in q:
            result += self._EXPLAIN_DELIMITER
            result += f'{e.value}'

        return result

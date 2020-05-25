from lab3.rpn.grammar.Lexer import SimpleMathGrammar, TokenKind, Operand0
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
            :param explain: boolean set to tru to see in output explain each step
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
            if t.type == TokenKind.NUMBER:
                if stack and stack[-1].type == TokenKind.OP:
                    que.append(t)
                    operator = stack.pop()
                    que.append(operator)
                else:
                    que.append(t)
            elif t.type == TokenKind.SEPARATOR and t.value in self.LEFT_P:
                stack.append(t)
            elif t.type == TokenKind.SEPARATOR and t.value in self.RIGHT_P:
                # pop last operator from stack as long as rich open parenthesis
                if stack and stack[-1].value not in self.LEFT_P:
                    operator = stack.pop()
                    que.append(operator)
                # remove from stack open parenthesis
                stack.pop()
            elif t.type == TokenKind.OP:
                o1 = SimpleMathGrammar.token_to_operand(t)
                o2 = SimpleMathGrammar.token_to_operand(stack[-1]) if stack and stack[-1].type == TokenKind.OP else Operand0()
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

        return self._que_expresion_to_string(que)

    def explain(self) -> str:
        """Print all steps as values stored in que and stack
            Returns:
                :return: explanation as string
            Raises:
                 ValueError: If `self.expresion` is not valid math expresion.
        """

        return self.convert(explain=True)

    def _explain_step(self, que: deque, stack: List) -> str:
        que_values = '['
        stack_values = '['

        for t in que:
            que_values += t.value + ' '
        que_values += ']'

        for t in stack:
            stack_values += f'"{t.value}"' + ', '
        stack_values += ']'

        return f' queue: {que_values} stack: {stack_values}'

    def _que_expresion_to_string(self, q: deque):
        result = ''

        result += f'{q.popleft().value}'
        for e in q:
            result += self._EXPLAIN_DELIMITER
            result += f'{e.value}'

        return result

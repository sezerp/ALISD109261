from lab3.rpn.grammar.Lexer import SimpleMathGrammar, TokenKind, Operand0
import queue


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

    def convert(self) -> str:
        """Convert `self.expresion` into expresion
            Do not support unary operations
            Returns:
                :return: str
            Raises:
                 ValueError: If `self.expresion` is not valid math expresion.
        """
        smg = SimpleMathGrammar()
        stack = []
        que = queue.Queue()
        for t in smg.tokenize(self.expresion):
            if t.type == TokenKind.NUMBER:
                if stack and stack[-1].type == TokenKind.OP:
                    que.put(t)
                    operator = stack.pop()
                    que.put(operator)
                else:
                    que.put(t)
            elif t.type == TokenKind.SEPARATOR and t.value in self.LEFT_P:
                stack.append(t)
            elif t.type == TokenKind.SEPARATOR and t.value in self.RIGHT_P:
                # pop last operator from stack as long as rich open parenthesis
                if stack and stack[-1].value not in self.LEFT_P:
                    operator = stack.pop()
                    que.put(operator)
                # remove from stack open parenthesis
                stack.pop()
            elif t.type == TokenKind.OP:
                o1 = SimpleMathGrammar.token_to_operand(t)
                o2 = SimpleMathGrammar.token_to_operand(stack[-1]) if stack and stack[-1].type == TokenKind.OP else Operand0()
                if o1.precedence > o2.precedence:
                    stack.append(t)
                elif stack and (o1.precedence < o2.precedence or o1.precedence == o2.precedence):
                    o = stack.pop()
                    que.put(o)
                    stack.append(t)
            # self._explain_step(que, stack)

        # moving
        for t in stack:
            if t.type not in TokenKind.SEPARATOR:
                que.put(t)

        return self._que_expresion_to_string(que)

    def explain(self) -> str:
        """Print all steps
            Returns:
                :return: explanation as string
            Raises:
                 ValueError: If `self.expresion` is not valid math expresion.
        """
        raise NotImplementedError()

    def _explain_step(self, que, stack) -> str:
        return f' queue: {self._que_expresion_to_string(que)} stack: {stack}'

    def _que_expresion_to_string(self, q: queue.Queue):
        result = ''

        result += f'{q.get().value}'
        for e in range(0, q.qsize()):
            result += self._EXPLAIN_DELIMITER
            result += f'{q.get().value}'

        return result

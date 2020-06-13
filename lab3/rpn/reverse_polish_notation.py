from lab3.rpn.grammar.Lexer import SimpleMathGrammar, TokenKind, Operand0, Token
from collections import deque
from typing import List


class RPNExplanator:

    _step = 'Step'
    _input = 'Input'
    _operation = 'Operation'
    _stack = 'Stack'

    def __init__(self):
        self.step = 0
        self.columns = {
            self._step: {
                'width': len(self._step) + 2,
                'column': []
            },
            self._input: {
                'width': len(self._input) + 2,
                'column': []
            },
            self._operation: {
                'width': len(self._input) + 2,
                'column': []
            },
            self._stack: {
                'width': len(self._input) + 2,
                'column': []
            }
        }

    def add(self, queue, stack: List[Token], op='-'):
        self._update_step_col(self.step)
        self._update_input_col(queue)
        self._update_stack_col(stack)
        self._update_operation_col(op)

    def __str__(self):
        offset = 1
        st_w = self.columns[self._step]['width']
        in_w = self.columns[self._input]['width']
        stc_w = self.columns[self._stack]['width']
        op_w = self.columns[self._operation]['width']
        result = ''
        for (k, v) in self.columns.items():
            w = v['width']
            col_title = k + (' ' * (w - len(k)))
            result += f'|{col_title}'
        result += '\n'
        result += '-' * (st_w + in_w + stc_w + op_w)
        result += '\n'
        for i in range(self.step):
            st_s = f"{self.columns[self._step]['column'][i]}" + (' ' * (st_w - len(f"{self.columns[self._step]['column'][i]}") + offset))
            in_s = f"{self.columns[self._input]['column'][i]}" + (' ' * (in_w - len(f"{self.columns[self._input]['column'][i]}") + offset))
            stc_s = f"{self.columns[self._stack]['column'][i]}" + (' ' * (stc_w - len(f"{self.columns[self._stack]['column'][i]}") + offset))
            op_s = f"{self.columns[self._operation]['column'][i]}" + (' ' * (op_w - len(f"{self.columns[self._operation]['column'][i]}")))
            result += f'{st_s}|{in_s}|{stc_s}|{op_s}\n'

        return result

    def _update_step_col(self, step):
        self.step += 1
        if len(f'{step}') > len(f'{step - 1}'):
            self.columns[self._step]['width'] = len(f'{step}')

        self.columns[self._step]['column'].append(f'{step}')

    def _update_input_col(self, input_d):
        actual_w = self.columns[self._stack]['width']
        if len(self._mk_string_queue(input_d)) > actual_w:
            self.columns[self._input]['width'] = len(self._mk_string_queue(input_d)) + 2

        self.columns[self._input]['column'].append(self._mk_string_queue(input_d))

    def _update_stack_col(self, stack):
        actual_w = self.columns[self._stack]['width']
        if len(self._mk_string_stack(stack)) > actual_w:
            self.columns[self._stack]['width'] = len(self._mk_string_stack(stack))

        self.columns[self._stack]['column'].append(self._mk_string_queue(stack))

    def _update_operation_col(self, op='-'):
        actual_w = self.columns[self._operation]['width']
        if len(f'{op}') > actual_w:
            self.columns[self._operation]['width'] = len(f'{op}')

        self.columns[self._operation]['column'].append(f'{op}')

    @staticmethod
    def _mk_string_stack(iterable: List[Token]) -> str:
        if len(iterable) == 0:
            return '[Empty]'
        new_iterable = iterable.copy()
        new_iterable.reverse()
        result = ''
        for e in new_iterable:
            try:
                result += f', {e.value}'
            except AttributeError:
                result += f', {e}'

        return result

    @staticmethod
    def _mk_string_queue(iterable: deque) -> str:
        if len(iterable) == 0:
            return '[Empty]'
        result = ''
        for e in iterable:
            try:
                result += f', {e.value}'
            except AttributeError:
                result += f', {e}'

        return result


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
        step_recorder = RPNExplanator()
        smg = SimpleMathGrammar()
        stack = []
        que = deque()
        for t in smg.tokenize(self.expresion):
            if t.type == TokenKind.OPERAND:
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
                while stack and o1.precedence <= o2.precedence:
                    o = stack.pop()
                    que.append(o)
                    o2 = SimpleMathGrammar.token_to_operator(stack[-1]) if stack and stack[-1].type == TokenKind.OP else Operand0()
                stack.append(t)

            if explain:
                step_recorder.add(que, stack)

        while stack:
            t = stack.pop()
            if t.type not in TokenKind.SEPARATOR:
                que.append(t)
                if explain:
                    step_recorder.add(que, stack)

        if explain:
            print(step_recorder)

        return self._que_mk_string(que)

    def calculate(self, explain=False) -> float:
        """
        Calculate given algebraic expresion
        :param explain: if set to `True` then will print step by stem explanation
        :return: result after calculation expresion
        """

        stc = []
        rpn_exp = self.convert(explain)
        step_recorder = RPNExplanator()
        smg = SimpleMathGrammar()
        for t in smg.tokenize(rpn_exp):
            if t.type == TokenKind.OPERAND:
                stc.append(t.value)
                if explain:
                    step_recorder.add([], stc)
            elif t.type == TokenKind.OP:
                operator = SimpleMathGrammar.token_to_operator(t)
                operands = []
                for _ in range(operator.number_arguments):
                    operand = float(stc.pop())
                    operands.append(operand)
                sub_result = operator.apply(operands)
                stc.append(sub_result)
                if explain:
                    step_recorder.add(['[Empty]'], stc)
        if explain:
            print(step_recorder)

        return stc.pop()

    def explain(self) -> str:
        """Print all steps as values stored in que and stack
            Returns:
                :return: explanation as string
            Raises:
                 ValueError: If `self.expresion` is not valid math expresion.
        """

        return self.convert(explain=True)

    def _que_mk_string(self, q: deque):
        if len(q) == 0:
            return ''
        result = ''

        result += f'{q.popleft().value}'
        for e in q:
            result += self._EXPLAIN_DELIMITER
            result += f'{e.value}'

        return result

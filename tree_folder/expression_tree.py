from tree_folder.linked_binary_tree import LinkedBinaryTree
from stack_folder.linked_stack import LinkedStack


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)

    def __str__(self):
        """Return string representation of the expression."""
        # 类似于中序遍历
        pieces = []
        self._parenthesize_recur(self.root(), pieces)  # 生成一个字符串列表
        return ''.join(pieces)                         # 转换成一个字符串

    def __repr__(self):
        return self.__str__()

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(')')

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):    # p表示一个子树的根位置
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())   # 将字符转换为可以计算的浮点数
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val


def tokenize(raw):
    """Produces list of tokens indicated by a raw expression string.
    For example, the string '(43-(3*10))' results in the list
    ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    SYMBOLS = set('+-x*/() ')
    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j])
            if raw[j] != ' ':
                tokens.append(raw[j])
            mark = j+1
    if mark != n:
        tokens.append(raw[mark:n])
    return tokens


def build_expression_tree(expression):
    """Returns an ExpressionTree based upon by a tokenized
    expression. tokens must be an iterable of strings
    representing a fully parenthesized binary expression,
    such as ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    tokens = tokenize(expression)
    S = LinkedStack()
    for t in tokens:
        if t in '+-x*/':
            S.push(t)
        elif t not in '()':
            S.push(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.push(ExpressionTree(op, left, right))
    if len(S) > 1:
        right = S.pop()
        op = S.pop()
        left = S.pop()
        S.push(ExpressionTree(op, left, right))
    return S.pop()


if __name__ == '__main__':
    # expression = '((((3 + 1) * 3)/((9-5)+2))-((3x(7-4))+6))'
    expression = '(3+4)*(5-2)'
    tree = build_expression_tree(expression)
    print(f'{expression} = {tree.evaluate()}')

from tree_folder.tree import Tree
from stack_folder.linked_stack import LinkedStack


class BinaryTree(Tree):

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self, mode='inoder'):
        if mode == 'inorder':
            return self.inorder()
        elif mode == 'preorder':
            return self.preorder()
        elif mode == 'postorder':
            return self.postorder()
        elif mode in ('breadthfirst', 'levelorder'):
            return self.breadthfirst()
        else:
            raise ValueError('Invalid mode!')

    def inorder_with_one_stack(self):
        """implementation of inorder traversal using one stack"""
        if self.is_empty():
            return

        current = self.root()
        s = LinkedStack()

        while True:
            if current is not None:
                s.push(current)
                current = self.left(current)

            elif not s.is_empty():
                current = s.pop()
                yield current
                current = self.right(current)

            else:
                break

    def preorder_with_one_stack(self):
        """implementation of preorder traversal using one stack"""
        if self.is_empty():
            return

        s = LinkedStack()
        s.push(self.root())

        while not s.is_empty():
            current = s.pop()
            yield current

            if self.right(current) is not None:
                s.push(self.right(current))

            if self.left(current) is not None:
                s.push(self.left(current))

    def postorder_with_two_stacks(self):
        """implementation of postorder traversal using two stacks"""
        if self.is_empty():
            return

        s1 = LinkedStack()
        s2 = LinkedStack()
        s1.push(self.root())

        while not s1.is_empty():
            current = s1.pop()
            s2.push(current)

            if self.left(current) is not None:
                s1.push(self.left(current))

            if self.right(current) is not None:
                s1.push(self.right(current))

        while not s2.is_empty():
            yield s2.pop()

    def postorder_with_one_stack(self):
        """implementation of postorder traversal using one stack"""
        if self.is_empty():
            return

        s = LinkedStack()
        current = self.root()

        while True:
            while current is not None:
                if self.right(current) is not None:
                    s.push(self.right(current))
                s.push(current)

                current = self.left(current)

            current = s.pop()
            p = s.top() if not s.is_empty() else None
            if self.right(current) is not None and p == self.right(current):
                s.pop()
                s.push(current)
                current = self.right(current)

            else:
                yield current
                current = None

            if s.is_empty():
                break
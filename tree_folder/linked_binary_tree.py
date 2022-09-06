from tree_folder.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


if __name__ == '__main__':
    t1 = LinkedBinaryTree()
    print(t1._add_root('3'))
    print(t1._validate(t1.root()))
    t1._add_left(t1.root(), 'zzw')
    t2 = LinkedBinaryTree()
    t2._add_root('4')
    t3 = LinkedBinaryTree()
    t3._add_root('+')
    t3._attach(t3.root(), t1, t2)
    print('test')
    print(t3.root())
    print(t3.root())
    print('test')

    t4 = LinkedBinaryTree()
    t4._add_root('5')
    t5 = LinkedBinaryTree()
    t5._add_root('2')
    t6 = LinkedBinaryTree()
    t6._add_root('-')
    t6._attach(t6.root(), t4, t5)

    t = LinkedBinaryTree()
    t._add_root('*')
    t._attach(t.root(), t3, t6)
    print(t)


    s = [p.element() for p in t.preorder()]
    print(s)

    s = [p.element() for p in t.postorder()]
    print(s)

    s = [p.element() for p in t.inorder()]
    print(s)

    s = [p.element() for p in t.inorder_with_one_stack()]
    print(s)

    s = [p.element() for p in t.preorder_with_one_stack()]
    print(s)

    s = [p.element() for p in t.postorder_with_two_stacks()]
    print(s)

    s = [p.element() for p in t.postorder_with_one_stack()]
    print(s)

from tree_folder.tree import Tree
from queue_folder.linked_queue import LinkedQueue
from stack_folder.linked_stack import LinkedStack


class NormalTree(Tree):

    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None, children=None):
            self._children = [] if children is None else children
            self._element = element
            self._parent = parent

    class Position(Tree.Position):
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

    def children(self, p):
        node = self._validate(p)
        l = []
        for i in node._children:
            l.append(self._make_position(i))
        return l

    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_children(self, p, L):
        node = self._validate(p)
        self._size += len(L)
        n1 = self.num_children(p)
        for e in L:
            node._children.append(self._Node(e, node))
        n2 = self.num_children(p)
        l = []
        for i in range(n1, n2, 1):
            l.append(self._make_position(node._children[i]))
        return l

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) >= 2:
            raise ValueError('Position has more than one child')
        if self.children(p) != None:
            child = node._children[0]
            child._parent = node._parent
            if node is self._root:
                self._root = child
            else:
                parent = node._parent
                parent._children.append(child)
        node._parent._children.remove(node)
        self._size -= 1
        node._parent = node
        return node._element

    def attach_subtree(self, p, subtree):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        for t in subtree:
            if not type(self) is type(t):
                raise TypeError('Tree types must match')
            self._size += len(t)
            if not t.is_empty():
                t._root._parent = node
                node._children.append(t._root)
                t._root = None
                t._size = 0

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def levelorder(self):
        if not self.is_empty():
            Q = LinkedQueue()
            Q.enqueue(self.root())
            while not Q.is_empty():
                p = Q.dequeue()
                yield p
                for c in self.children(p):
                    Q.enqueue(c)

    def reverse_levelorder(self):
        S = LinkedStack()
        S.push([self.root()])
        def dfs(root,depth):
            if len(root) == 0:
                S.pop()
                return
            if len(S) <= depth + 1:
                S.push([])
            for i in root:
                S.top().extend(self.children(i))
            dfs(S.top(), depth+1)
        dfs([self.root()], 0)
        while not S.is_empty():
            for p in S.pop():
                yield p

    def k_distance(self, k):
        if k == 0:
            return [self.root()]
        else:
            l = []
            for i in self.k_distance(k-1):
                l.extend(self.children(i))
            return l

    def test(self):
        if not self.is_empty():
            S = LinkedStack()
            P = LinkedStack()
            Q = LinkedStack()
            P.push(self.root())
            while not P.is_empty() and Q.is_empty():
                while not P.is_empty():
                    p = P.pop()
                    S.push(p)
                    if self.children(p) != None:
                        l = self.children(p)
                        l.reverse()
                        for c in l:
                            Q.push(c)
                while not Q.is_empty():
                    P.push(Q.pop())
            while not S.is_empty():
                yield S.pop()


if __name__ == '__main__':
    t1 = NormalTree()
    pos1 = t1.add_root('A')
    t2 = NormalTree()
    t2.add_root('B')
    t3 = NormalTree()
    pos3 = t3.add_root('C')
    print(pos3._container)
    print(pos3)
    t4 = NormalTree()
    pos4 = t4.add_root('D')
    t5 = NormalTree()
    pos5 = t5.add_root('E')
    t6 = NormalTree()
    pos6 = t6.add_root('F')
    pos7, pos8 = t5.add_children(t5.root(), ['G', 'H'])
    # print(t5.delete(pos7))
    t2.attach_subtree(t2.root(), [t4, t5, t6])
    t1.attach_subtree(t1.root(), [t2, t3])
    # print(t1._validate(pos1))
    # print(pos1._container)
    # print(pos1)
    # pos2, pos3 = t1.children(pos1)
    # print(pos3._container)
    # print(pos3)
    # # print(t1.delete(pos3))
    #
    # s = [p.element() for p in t1.preorder()]
    # print(s)
    # s = [p.element() for p in t1.postorder()]
    # print(s)
    # s = [p.element() for p in t1.levelorder()]
    # print(s)
    # s = [p.element() for p in t1.reverse_levelorder()]
    # print(s)
    print('begin test')
    print(t1.root())
    print(t1.root())
    b = t1.children(t1.root())
    print(b[0])
    print(b[1])
    print('测试兄弟节点的双亲节点地址是否一致')
    print(t1.parent(b[0]))
    print(t1.parent(b[1]))
    print('测试')
    l = []
    print(l)
    l.extend([])
    print(l)
    print([] == None)






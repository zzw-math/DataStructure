from queue_folder.doubly_linked_base import DoublyLinkedBase


class PositionalList(DoublyLinkedBase):

    class Position:
        def __init__(self, container, node):
            self._container = container       # 可以去掉
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """判断两个Position类是否相等"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        """p描述的结点不能是岗哨结点"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None or p._node._prev is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)      # self赋给_container，node赋给_node

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __repr__(self):
        return f'{list(iter(self))}'


if __name__ == '__main__':
    L = PositionalList()
    print(L)
    p = L.add_last(8)
    print(L, p == L.first())
    q = L.add_after(p, 5)
    print(L, p == L.before(q))
    r = L.add_before(q, 3)
    print(L, r.element())
    print(r == L.after(p), L.before(p))
    s = L.add_first(9)
    print(L)
    a = L.delete(L.last())
    print(L, a)
    L.replace(p, 7)
    print(L)

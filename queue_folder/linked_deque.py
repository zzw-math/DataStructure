from queue_folder.doubly_linked_base import DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(DoublyLinkedBase):

    """ Double -ended queue implementation based on a doubly linked list."""

    def first(self):
        """ Return (but do not remove) the element at the front"""
        if self.is_empty():
            raise Empty(" Deque is empty")
        return self._header._next._element

    def last(self):
        """ Return (but do not remove) the element at the back"""
        if self.is_empty():
            raise Empty(" Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """ Add an element to the front"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """ Add an element to the back"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """ Remove and return the element from the front.
            Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty(" Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """ Remove and return the element from the back.
            Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty(" Deque is empty")
        return self._delete_node(self._trailer._prev)

    def __repr__(self):
        data = []
        walk = self._header._next
        while walk._next is not None:
            data.append(walk._element)
            walk = walk._next
        return f'{data}'


if __name__ == '__main__':
    q = LinkedDeque()
    q.insert_first(1)
    q.insert_first(2)
    q.insert_last(3)
    q.insert_last(4)
    print(q)
    print(q.first())
    print(q.last())
    q.delete_first()
    q.delete_last()
    print(q)
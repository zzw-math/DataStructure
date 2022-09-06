class Empty(Exception):
    pass


class CircularQueue:
    """ Queue implementation using circularly linked list for storage."""

    class _Node:
        """ Nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """ Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Return the number of elements."""
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the front.
            Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """ Remove and return the element at the front.
            Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """ Add an element to the back."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """ Rotate front element to the back"""
        if self._size > 0:
            self._tail = self._tail._next

    def __repr__(self):
        data = []
        walk = self._tail._next
        while walk is not self._tail:
            data.append(walk._element)
            walk = walk._next
        data.append(walk._element)
        return f'{data}'


if __name__ == '__main__':
    q = CircularQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
    print(q.first())

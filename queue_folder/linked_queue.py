class Empty(Exception):
    pass


class LinkedQueue:
    """ LIFO Stack implementation using a singly linked list for storage.
    """
    class _Node:
        """ Nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """ Create an empty stack."""
        self._head = None  # reference to the head
        self._tail = None  # reference to the tail
        self._size = 0  # number of element

    def __len__(self):
        """ Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """ Return True if the stack is empty."""
        return self._size == 0

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def __str__(self):
        data = []
        s = self._head
        while s != None:
            data.append(s._element)
            s = s._next
        return f'{data}'

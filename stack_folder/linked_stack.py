class Empty(Exception):
    pass


class LinkedStack:
    """ LIFO Stack implementation using a singly linked list for storage.
    """

    class _Node:
        """ Nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next_):
            self._element = element
            self._next = next_

    def __init__(self):
        """ Create an empty stack."""
        self._head = None  # reference to the head
        self._size = 0     # number of element

    def __len__(self):
        """ Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """ Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """ Add element e to the top of the stack."""
        node = self._Node(e, self._head)  # create and positional_list_folder a new node
        self._head = node
        self._size += 1

    def pop(self):
        """ Remove and return the element at the top.
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result

    def top(self):
        """ Return (do not remove) the element at the top.
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def __repr__(self):
        data = []
        s = self._head
        while s is not None:
            data.append(s._element)
            s = s._next
        return f'{data}'


if __name__ == '__main__':
    q = LinkedStack()

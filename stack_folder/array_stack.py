class Empty(Exception):
    pass


class ArrayStack:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._top = -1

    def __len__(self):
        return self._size

    def push(self, val):
        if self._size == self.DEFAULT_CAPACITY:
            raise Exception('Stack is full!')

        self._data[self._size] = val
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        result = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._data[self._top]

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        return f'{self._data[:self._size]}'



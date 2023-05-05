class Empty(Exception):
    pass


class ArrayDeque():
    DEFAULT_CAPACITY = 20

    def __init__(self):
        """ Create an empty queue"""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """ Return the number of elements in the deque"""
        return self._size

    def is_empty(self):
        """ Return True if the deque is empty"""
        return self._size == 0

    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        last = (self._front + self._size - 1) % len(self._data)
        result = self._data[last]
        self._data[last] = None
        self._size -= 1
        return result

    def add_first(self, e):
        if len(self) == len(self._data):
            self._resize(2*len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        if len(self) == len(self._data):
            self._resize(2*len(self._data))
        last = (self._front + self._size) % len(self._data)
        self._data[last] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        temp = [x for x in self._data[self._front:]+self._data[:self._front] if x != None]
        self._data = temp + [None] * (cap - len(self._data))
        self._front = 0

    def __str__(self):
        return f'{[x for x in self._data[self._front:]+self._data[:self._front] if x != None] }'


if __name__ == '__main__':
    d = ArrayDeque()
    d.add_first(1)
    print(d)
    d.add_first(2)
    print(d)
    d.add_last(3)
    print(d)
    d.add_last(4)
    print(d)

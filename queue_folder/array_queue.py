class Empty(Exception):
    pass


class FULL(Exception):
    pass


class ArrayQueue:
    """ FIFO queue implementation using a list as underlying storage.
    """
    DEFAULT_CAPACITY = 5

    def __init__(self):
        """ Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def first(self):
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            raise FULL('The stack is full')
        self._data[(self._front + self._size) % len(self._data)] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        return f'{[x for x in self._data[self._front:] + self._data[:self._front] if x != None]}'


if __name__ == '__main__':
    q = ArrayQueue()
    print(q)

    q.enqueue(1)
    print(q)
    q.enqueue(2)
    print(q)
    q.enqueue(3)
    print(q)
    q.enqueue(4)
    print(q)
    q.dequeue()
    print(q)

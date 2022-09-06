from priority_queue_folder.priority_queue_base import PriorityQueueBase
from priority_queue_folder.positional_list import PositionalList
from priority_queue_folder.exceptions import Empty


class UnsortedPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """ Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):           # 时间复杂度为O(1)
        """ Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):   # 时间复杂度为O(1)
        """ Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def _find_min(self):         # 时间复杂度为O(n)
        """ Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):               # 时间复杂度为O(n)
        """ Return but do not remove (k,v) with minimum key.
            Raise Empty exception if empty.
        """
        p = self._find_min()
        item = p.element()
        return item._key, item._value

    def remove_min(self):        # 时间复杂度为O(n)
        """ Remove and return (k,v) with minimum key.
            Raise Empty exception if empty.
        """
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value

    def __repr__(self):
        return f'{self._data}'

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    P = UnsortedPriorityQueue()
    print(P)
    print(P.add(5, 'A'), P)
    print(P.add(9, 'C'), P)
    print(P.add(3, 'B'), P)
    print(P.add(7, 'D'), P)
    print(P.min(), P)
    print(P.remove_min(), P)
    print(P.remove_min(), P)
    print(len(P), P)
    print(P.remove_min(), P)
    print(P.remove_min(), P)
    print(P.is_empty(), P)
    # print(P.remove_min())

from priority_queue_folder.priority_queue_base import PriorityQueueBase
from priority_queue_folder.positional_list import PositionalList
from priority_queue_folder.exceptions import Empty


class SortedPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """ A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """ Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """ Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair."""
        new = self._Item(key, value)  # make new item instance
        walk = self._data.last()  # walk backward looking for smaller key
        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)  # new key is smallest
        else:
            self._data.add_after(walk, new)  # new goes after walk

    def min(self):
        """ Return but do not remove (k,v) with minimum key.
            Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        """ Remove and return (k,v) with minimum key.
            Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return item._key, item._value

    def __repr__(self):
        return f'{self._data}'

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    P = SortedPriorityQueue()
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

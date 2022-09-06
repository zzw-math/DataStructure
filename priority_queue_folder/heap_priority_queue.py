from priority_queue_folder.priority_queue_base import PriorityQueueBase
from priority_queue_folder.exceptions import Empty


class HeapPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""

    # -------------- public behaviors ----------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    # -------------- nonpublic behaviors ---------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                # recur at position of small child
                self._downheap(small_child)

    # ----------- public behaviors ----------------
    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        # upheap newly added position
        self._upheap(len(self._data) - 1)

    def min(self):
        """Return but do not remove (k,v) with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        # put minimum item at the end
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()   # and remove it from the list
        self._downheap(0)         # then fix new root
        return (item._key, item._value)


if __name__ == '__main__':
    P = HeapPriorityQueue()
    P.add(4, 'C'), P.add(5, 'A'), P.add(6, 'Z')
    P.add(15, 'K'), P.add(9, 'F'), P.add(7, 'Q')
    P.add(20, 'B'), P.add(16, 'X'), P.add(25, 'J')
    P.add(14, 'E'), P.add(12, 'H'), P.add(11, 'S')
    P.add(13, 'W')
    print(P._data)

    P.add(2, 'T')
    print(P._data)

    P.remove_min()
    print(P._data)

"""
[(4, C), (5, A), (6, Z), (15, K), (9, F), (7, Q), (20, B), (16, X), (25, J), (14, E), (12, H), (11, S), (13, W)]
[(2, T), (5, A), (4, C), (15, K), (9, F), (7, Q), (6, Z), (16, X), (25, J), (14, E), (12, H), (11, S), (13, W), (20, B)]
[(4, C), (5, A), (6, Z), (15, K), (9, F), (7, Q), (20, B), (16, X), (25, J), (14, E), (12, H), (11, S), (13, W)]
"""

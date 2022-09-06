from priority_queue_folder.positional_list import PositionalList
from priority_queue_folder.sorted_priority_queue import SortedPriorityQueue


def insertion_sort(L):
    """ implementation of selection sort"""
    C = PositionalList()
    for e in L:
        C.add_last(e)
    n = len(C)
    P = SortedPriorityQueue()
    for j in range(n):
        elem = C.delete(C.first())
        P.add(elem, elem)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)
    return C


L = [6, 7, 4, 5, 2, 9]
print(L)
C = insertion_sort(L)
print(C)

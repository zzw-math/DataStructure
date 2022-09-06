from priority_queue_folder.positional_list import PositionalList
from priority_queue_folder.unsorted_priority_queue import UnsortedPriorityQueue
from priority_queue_folder.sorted_priority_queue import SortedPriorityQueue
from priority_queue_folder.heap_priority_queue import HeapPriorityQueue
import numpy as np
import time


def sort(C, method='Selected'):
    """ implementation of selection sort"""
    n = len(C)
    if method == 'Sorted':
        P = SortedPriorityQueue()
    elif method == 'Selected':
        P = UnsortedPriorityQueue()
    elif method == 'Heap':
        P = HeapPriorityQueue()
    else:
        raise ValueError('Not support method')

    for j in range(n):
        elem = C.delete(C.first())
        P.add(elem, elem)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)


L = np.random.rand(1000)

for m in ['Sorted', 'Selected', 'Heap']:
    start = time.time()
    C = PositionalList()
    for e in L:
        C.add_last(e)
    start = time.time()
    sort(C, method=m)
    end = time.time()
    time = end - start
    print(time)




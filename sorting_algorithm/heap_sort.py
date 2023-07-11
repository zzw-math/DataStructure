class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def pa(self, idx):
        return (idx - 1)//2

    def left_ch(self, idx):
        return 2*idx + 1

    def right_ch(self, idx):
        return 2 * idx + 2

    def bubble_up(self, idx):
        p = idx
        while self.pa(p) > -1:
            if self.heap[self.pa(p)] < self.heap[p]:
                self.heap[self.pa(p)], self.heap[p] = self.heap[p], self.heap[self.pa(p)]
            else:
                break

    def bubble_down(self):
        p = 0
        while self.left_ch(p) < self.size or self.right_ch(p) < self.size:
            if self.left_ch(p) < self.size and self.right_ch(p) < self.size:
                if self.heap[self.left_ch(p)] < self.heap[self.right_ch(p)]:
                    candidate = self.right_ch(p)
                else:
                    candidate = self.left_ch(p)
            if self.right_ch(p) >= self.size:
                candidate = self.left_ch(p)
            elif self.left_ch(p) >= self.size:
                candidate = self.right_ch(p)
            if self.heap[p] < self.heap[candidate]:
                self.heap[p], self.heap[candidate] = self.heap[candidate], self.heap[p]
                p = candidate
            else:
                break

    def add_node(self, val):
        self.heap.append(val)
        self.bubble_up(len(self.heap)-1)
        self.size += 1

    def remove_node(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.size -= 1
        self.bubble_down()
        return val


def heap_sort(arr):
    heap = Heap()
    n = len(arr)
    for c in arr:
        heap.add_node(c)
    _result = [None] * n
    for i in range(n-1, -1, -1):
        _result[i] = heap.remove_node()
    return _result


if __name__ == '__main__':
    b = [3, 5, 2, 4, 1]
    result = heap_sort(b)
    print(result)

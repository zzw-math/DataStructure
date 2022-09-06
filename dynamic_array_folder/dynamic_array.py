from ctypes import py_object


class DynamicArray(object):
    """ Dynamic array class akin to a simplified Python list. """

    def __init__(self):
        """ Create an empty array """
        self._n = 0  # 包含元素个数
        self._capacity = 1  # 最大容量
        self._A = self._make_array(self._capacity)  # 地址

    def _make_array(self, c):
        """ Return a new array with capacity c """
        return (c * py_object)()

    def __len__(self):
        """ Return number of elems stored in the array """
        return self._n

    def __getitem__(self, k):
        """ Return elem at index k """
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        """ Add an object to the end of the array """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """ Resize internal array to capacity c """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def insert(self, k, obj):
        """ Insert an object at index k """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = obj
        self._n += 1

    def pop(self, k=None):
        """ Pop out the last elem if k is None, else the elem at index k """
        if k is None:
            val = self._A[self._n - 1]
            self._A[self._n - 1] = None
            self._n -= 1
            return val
        else:
            if not 0 <= k < self._n:
                raise IndexError('Invalid index')
            val = self._A[k]
            for j in range(k, self._n - 1):
                self._A[j] = self._A[j + 1]
            self._A[self._n - 1] = None
            self._n -= 1
            return val

    def remove(self, val):
        for k in range(self._n):
            if self._A[k] == val:
                return self.pop(k)
        raise ValueError('There is not the val in the list')

    def __repr__(self):
        return f'{self._A[:self._n]}'


if __name__ == '__main__':
    a = DynamicArray()
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)
    a.pop(1)
    print(a)
    a.remove(1)
    print(a)
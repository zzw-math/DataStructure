def bubble_sort(arr):
    """
    使用冒泡排序对数组进行原地排序
    :param arr: 待排序数组
    :return: 不返回任何值
    """
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort2(arr):
    """
    改进的冒泡排序: 改进外部循环，若上一次内循环未发生交换，则数组已有序，退出外部循环；
                 改进内部循环，记录上一次内循环最后发生交换的位置，作为下一次内循环的终点。
    :param arr: 待排序数组
    :return: 不返回任何值
    """
    n = len(arr)
    k = n-1
    for i in range(n-1):
        swap = False
        pos = 0
        for j in range(k):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                pos = j
        if swap is False:
            break
        k = pos


if __name__ == '__main__':
    b = [3, 5, 2, 4, 1]
    bubble_sort(b)
    print(b)

    b = [3, 5, 2, 4, 1]
    bubble_sort2(b)
    print(b)

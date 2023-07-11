def selection_sort(arr):
    """
    使用选择排序对数组进行原地排序
    :param arr: 待排序数组
    :return: 不返回任何值
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    b = [3, 5, 2, 4, 1]
    selection_sort(b)
    print(b)

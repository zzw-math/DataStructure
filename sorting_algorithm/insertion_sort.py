def insertion_sort(arr):
    """
    使用插入排序对数组进行原地排序
    :param arr: 待排序数组
    :return: 不返回任何值
    """
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i-1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value


if __name__ == '__main__':
    b = [3, 5, 2, 4, 1]
    insertion_sort(b)
    print(b)

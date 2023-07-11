def bubble_sort(l):
    """
    使用冒泡排序对列表进行原地排序
    :param l: 待排序列表
    :return: 不返回任何值
    """
    n = len(l)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


b = [3, 5, 2, 4, 1]
bubble_sort(b)
print(b)

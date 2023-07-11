def partition(arr, left, right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left


def qsort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        qsort(arr, left, pivot-1)
        qsort(arr, pivot+1, right)


def quick_sort(arr):
    n = len(arr)
    qsort(arr, 0, n-1)


if __name__ == '__main__':
    b = [3, 5, 2, 4, 1]
    quick_sort(b)
    print(b)

def merge_sorted_array(arr, left, middle, right):
    temp = [None]*(right-left+1)
    i = left
    j = middle + 1
    k = 0
    while i <= middle and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            k += 1
            j += 1
    while i <= middle:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    arr[left:(right+1)] = temp


def internal_merge_sort(arr, left, right):
    if left < right:
        middle = (left+right)//2
        internal_merge_sort(arr, left, middle)
        internal_merge_sort(arr, middle+1, right)
        merge_sorted_array(arr, left, middle, right)


def merge_sort(arr):
    n = len(arr)
    internal_merge_sort(arr, 0, n-1)


if __name__ == '__main__':
    b = [3, 5, 2, 4, 1]
    merge_sort(b)
    print(b)

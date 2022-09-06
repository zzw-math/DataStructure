from queue_folder.array_deque import ArrayDeque


# 回文序列的判断
def is_palindromic(str):
    Q = ArrayDeque()
    for ch in str:
        Q.add_last(ch)
    for i in range(0, len(Q)//2):
        first = Q.delete_first()
        last = Q.delete_last()
        if first != last:
            return False
    return True


print(is_palindromic('abc sds cba'))
print(is_palindromic('123ab321'))
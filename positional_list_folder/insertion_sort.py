from positional_list_folder.positional_list import PositionalList


def insertion_sort(L):
    """ Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


if __name__ == '__main__':
    L = [4, 3, 2, 10, 12, 1, 5, 6]
    PL = PositionalList()           # 这里的圆括号不能删除
    for e in L:
        PL.add_last(e)
    print(f'before sort: {PL}')
    insertion_sort(PL)
    print(f'after sort: {PL}')

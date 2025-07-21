def isSorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True

    if a[0] > a[1]:
        return False

    smallerList = a[1:]
    isSmallerListSorted = isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(isSorted(a))

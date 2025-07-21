def bin_search(a,x,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return bin_search(a,x,si,mid-1)
    else:
        return bin_search(a,x,mid+1,ei)
bin_search([1,3,5,7,9,11,13],3,0,9)
print(bin_search([1,3,5,7,9,11,13],4,0,9))
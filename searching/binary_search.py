def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
        
    while lo < hi:
        mid = lo + (hi-lo)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid

    return -1


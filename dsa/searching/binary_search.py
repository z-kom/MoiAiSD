def binary_search(a: list[int], x: int, lo: int = 0, hi: int | None = None) -> int:
    """
    Индекс x в a[lo:hi] (полуинтервал) или -1.
    Время: O(log n) 
    Память: O(1)
    Требует: a отсортирован по возрастанию.
    """
    if hi is None:
        hi = len(a)
    if hi > len(a):
        hi = len(a)
    if lo < 0:
        lo = 0
    if lo > len(a):
        lo = len(a)
    if hi < 0:
        hi = 0
        
    while lo < hi:
        mid = lo + (hi-lo)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid

    return -1


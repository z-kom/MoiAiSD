def lower_bound(a: list[int], x: int, lo: int = 0, hi: int | None = None) -> int:
    """
    Первое вхождение x в a[lo:hi] (полуинтервал), если нет, то hi.
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
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid

    return lo

def upper_bound(a: list[int], x: int, lo: int = 0, hi: int | None = None) -> int:
    """
    Последнее вхождение x в a[lo:hi] (полуинтервал), если нет, то hi.
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
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid

    return lo

def count_by_bounds(a: list[int], x: int, lo: int = 0, hi: int | None = None) -> int:
    """
    Количество элементов x в a[lo:hi] (полуинтервал).
    Время: O(log n) 
    Память: O(1)
    Требует: a отсортирован по возрастанию.
    """
    return upper_bound(a, x, lo, hi) - lower_bound(a, x, lo, hi)
    

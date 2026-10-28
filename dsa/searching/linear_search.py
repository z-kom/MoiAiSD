def linear_search(a: list, x, start: int = 0, stop: int | None = None) -> int:
    """
    Первый индекс в i в [start, stop), где a[i == x, иначе -1.
    Время: O(n)
    Память: O(1)
    """
    if stop is None:
        stop = len(a)
    if start < 0:
        start = 0
    if stop > len(a):
        stop = len(a)
    
    for i in range(start, stop):
        if x == a[i]:
            return i
    return -1

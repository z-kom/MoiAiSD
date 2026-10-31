def isqrt(n: int) -> int:
    """
    Наибольшее r >= 0, такое что r*r <= n.
    Время: O(log n) 
    Память: O(1)
    """
    if n < 0:
        raise ValueError("isqrt: n must be >= 0")
    if n < 2:
        return n

    lo, hi = 0, n//2
    
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1

    return lo



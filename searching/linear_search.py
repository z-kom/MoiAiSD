# Линейный поиск с пропуском вариантов
def linear_search(a, x, skip=0):
    """
    Время: O(n)
    Память: O(1)
    """
    indices = range(len(a))
    if skip < 0:
        indices = range(len(a)-1, -1, -1)
        skip = -skip - 1
        
    for i in indices:
        if x == a[i]:
            if not skip:
                return i
            skip -= 1
            
    return -1
    

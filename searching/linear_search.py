def linear_search(a, x):
    for i in range(len(a)):
        if x == a[i]:
            return i
    return -1

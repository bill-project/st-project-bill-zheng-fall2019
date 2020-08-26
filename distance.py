from math import sqrt

def distance(a, b):
    if len(a) != len(b):
        return none
    else:
        start = 0
        for k in range(0, len(a)):
            start += (a[k]-b[k])**2
    start = sqrt(start)
    print(start)
    return start

distance([1, 2, 5, 2], [2, 3, 2, 1])

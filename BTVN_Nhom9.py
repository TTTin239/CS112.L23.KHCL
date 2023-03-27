import copy
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
 
    return min_val

def stripClosest(strip, size, d):
     
    min_val = d

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val

def closestUtil(P, A, n):
    if n <= 3:
        return bruteForce(P, n)
 
    mid = n // 2
    midPoint = P[mid]
 
    Pl = P[:mid]
    Pr = P[mid:]
 
    dl = closestUtil(Pl, A, mid)
    dr = closestUtil(Pr, A, n - mid)
 
    d = min(dl, dr)

    stripP = []
    stripA = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(A[i].x - midPoint.x) < d:
            stripA.append(A[i])
 
    stripP.sort(key = lambda point: point.y)
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripA, len(stripA), d))
    
    return min(min_a,min_b)

def closest(P, n):
    P.sort(key = lambda point: point.x)
    A = copy.deepcopy(P)
    A.sort(key = lambda point: point.y)   

    return closestUtil(P, A, n)

P = [Point(1, 1), Point(1, 4),
     Point(2, 5), Point(3, 1),
     Point(3, 3), Point(5, 3),
     Point(5, 5), Point(5, 6),
     Point(6, 2), Point(7, 4)]
n = len(P)

print("The smallest distance is",
                   closest(P, n))
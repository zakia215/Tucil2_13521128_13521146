import math
from .sorting import quickSort

timesEuclideanDistanceCalculated = 0

def findDistance(a, b):
    global timesEuclideanDistanceCalculated
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i]) ** 2
    timesEuclideanDistanceCalculated += 1
    return math.sqrt(res)

def findClosestPair(points, n, dimension):
    if (n <= 3):
        return findClosestPairOfBF(points)
    else:
        # Sort the points on their abses
        quickSort(points, 0, len(points) - 1, 0)

        # Split the index into two arbitrary area, s1 and s2 and find the shortest pair in those two areas
        mid = n // 2
        s1 = points[:mid]
        s2 = points[mid:]
        shortest_s1 = findClosestPair(s1, len(s1), dimension)
        shortest_s2 = findClosestPair(s2, len(s2), dimension)
        if (shortest_s1[2] >= shortest_s2[2]) :
            shortest_s1_s2 = shortest_s2
        else :
            shortest_s1_s2 = shortest_s1
        
        # Find points in 'slab' such that those points have distance shorter than or equal to shortest_s1_s2 to the point in the mid index
        slab_s1 = [p for p in s1 if abs(p[0] - points[mid][0]) < shortest_s1_s2[2]]
        quickSort(slab_s1, 0, len(slab_s1) - 1, 1)
        slab_s2 = [p for p in s2 if abs(p[0] - points[mid][0]) < shortest_s1_s2[2]]
        quickSort(slab_s2, 0, len(slab_s2) - 1, 1)

        for i in range(len(slab_s1)):
            for j in range(len(slab_s2)):
                check = True
                for k in range(dimension):
                    if abs(slab_s1[i][k] - slab_s2[j][k]) > shortest_s1_s2[2]:
                        check = False
                if (check) :
                    tempDistance = findDistance(slab_s1[i], slab_s2[j])
                    if tempDistance < shortest_s1_s2[2]:
                        shortest_s1_s2 = (slab_s1[i], slab_s2[j], tempDistance)
                
        return shortest_s1_s2


def findClosestPairOfBF(points):
    closest = ()
    min = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            tempDistance = findDistance(points[i], points[j])
            if tempDistance < min:
                min = tempDistance
                closest = (points[i], points[j])
    return closest + (min,)
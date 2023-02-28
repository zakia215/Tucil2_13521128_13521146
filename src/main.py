import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random


timesEuclideanDistanceCalculated = 0

def quickSort(arr, low, high, tuple_att_to_sort):
    if (low < high):
        pi = partition(arr, low, high, tuple_att_to_sort)
        quickSort(arr, low, pi - 1, tuple_att_to_sort)
        quickSort(arr, pi + 1, high, tuple_att_to_sort)

def partition(arr, low, high, tuple_att_to_sort):
    i = low - 1
    pivot = arr[high][tuple_att_to_sort]
    for j in range(low, high):
        if (arr[j][tuple_att_to_sort] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def findDistance(a, b):
    global timesEuclideanDistanceCalculated
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i]) ** 2
    timesEuclideanDistanceCalculated += 1
    return math.sqrt(res)

def findClosestPair(points, n, dimension):
    if (n <= 3):
        return findClosestPairOfThreePoints(points)
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
        slab_s1 = [p for p in s1 if abs(p[0] - points[mid][0]) < shortest_s1_s2[2] / 2]
        quickSort(slab_s1, 0, len(slab_s1) - 1, 1)
        slab_s2 = [p for p in s2 if abs(p[0] - points[mid][0]) < shortest_s1_s2[2] / 2]
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


def findClosestPairOfThreePoints(points):
    closest = ()
    min = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            tempDistance = findDistance(points[i], points[j])
            if tempDistance < min:
                min = tempDistance
                closest = (points[i], points[j])
    return closest + (min,)

if __name__ == "__main__":

    
    nPoints = int(input("Enter number of points generated: "))
    dimPoints = int(input("Enter dimension of points generated: "))

    points = []
    # points = [(49, -364), (647, 422), (907, -978), (-802, 399), (946, 958), (-239, -954), (682, 516), (427, -956), (-125, -130), (-913, -386)]

    for i in range(int(nPoints)):
        points.append(tuple([random.randint(-1000, 1000) for i in range(int(dimPoints))]))

    # Divide and Conquer
    startDNC = time.time()
    
    closest_pair_3d = findClosestPair(points, nPoints, dimPoints)
    timesEuclideanDistanceCalculatedDNC = timesEuclideanDistanceCalculated

    endDNC = time.time()

    # Brute Force

    startBF = time.time()

    timesEuclideanDistanceCalculated = 0

    closest_pair_brute = findClosestPairOfThreePoints(points)
    timesEuclideanDistanceCalculatedBF = timesEuclideanDistanceCalculated

    endBF = time.time()
    
    print('\n'+ str(closest_pair_3d[:2]))
    print("Distance : ", closest_pair_3d[2])
    print(timesEuclideanDistanceCalculatedDNC, "times Euclidean distance calculated")
    print("Time taken: ",'%.15f' % (endDNC - startDNC), "seconds")
    

    print('\n' + str(closest_pair_brute[:2]))
    print("Distance : ", closest_pair_brute[2])
    print(timesEuclideanDistanceCalculatedBF, "times Euclidean distance calculated")
    print("Time taken: ",'%.15f' % (endBF - startBF), "seconds")


    points = [(random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000)) for i in range(1000)]


    # numpied_points = np.array(points)

    # fig = plt.figure()
    # ax = fig.add_subplot(projection = '3d')

    # for x, y, z in points:
    #     if ((x, y, z) in closest_pair_3d[:2]) :
    #         ax.scatter(x, y, z, marker='^', color='r')
    #     else:    
    #         ax.scatter(x, y, z, marker='o', color='g')

    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')

    # plt.show()

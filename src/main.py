import math
import numpy as np
import matplotlib.pyplot as plt

def findDistance(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i]) ** 2
    return math.sqrt(res)

def findClosestPair(points, n, dimension):
    if (n <= 3):
        return findClosestPairOfThreePoints(points, dimension)
    else:
        # Sort the points on their abses
        sorted_points = points.sort(key=lambda p: p[0])

        # Split the index into two arbitrary area, s1 and s2 and find the shortest pair in those two areas
        mid = n // 2
        s1 = points[:mid]
        s2 = points[mid:]
        shortest_s1 = findClosestPair(s1, len(s1), dimension)
        shortest_s2 = findClosestPair(s2, len(s2), dimension)
        if (shortest_s1[2] >= shortest_s2[2]):
            shortest_s1_s2 = shortest_s2
        else :
            shortest_s1_s2 = shortest_s1
        
        # Find points in 'slab' such that those points have distance shorter than or equal to shortest_s1_s2 to the point in the mid index
        slab = [p for p in points if abs(p[0] - points[mid][0]) < shortest_s1_s2[2]]
        slab.sort(key=lambda p: p[0])

        for i in range(len(slab)):
            for j in range(i + 1, len(slab)):
                if findDistance(slab[i], slab[j]) < shortest_s1_s2[2]:
                    shortest_s1_s2 = (slab[i], slab[j], findDistance(slab[i], slab[j]))
        
        return shortest_s1_s2


def findClosestPairOfThreePoints(points, dimension):
    closest = ()
    min = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if findDistance(points[i], points[j]) < min:
                min = findDistance(points[i], points[j])
                closest = (points[i], points[j])
    return closest + (min,)

if __name__ == "__main__":
    points = [
        (2694, 1833, 770),
        (1879, 2186, 2165),
        (2572, 2529, 2488),
        (2291, 2899, 1125),
        (2733, 1659, 884),
        (1882, 2257, 1475),
        (706, 97, 1258),
        (302, 384, 2354),
        (2123, 1088, 1782),
        (134, 2460, 2444),
        (178, 356, 695),
        (1686, 2627, 1733),
        (1661, 664, 324),
        (1028, 2622, 1916),
    ]

    closest_pair_3d = findClosestPair(points, 14, 3)
    print(closest_pair_3d[:2])

    numpied_points = np.array(points)

    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')

    for x, y, z in points:
        if ((x, y, z) in closest_pair_3d[:2]) :
            ax.scatter(x, y, z, marker='^', color='r')
        else:    
            ax.scatter(x, y, z, marker='o', color='g')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

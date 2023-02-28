import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import sys
import platform

sys.path.append('/util/')

from util import closest_pair, display

if __name__ == "__main__":

    sys.setrecursionlimit(10000)    
    nPoints = int(input("Enter number of points generated: "))
    dimPoints = int(input("Enter dimension of points generated: "))

    points = []

    for i in range(int(nPoints)):
        points.append(tuple([random.randint(-1000, 1000) for i in range(int(dimPoints))]))

    # Divide and Conquer
    startDNC = time.time()
    
    closest_pair_3d = closest_pair.findClosestPair(points, nPoints, dimPoints)
    timesEuclideanDistanceCalculatedDNC = closest_pair.timesEuclideanDistanceCalculated

    endDNC = time.time()

    # Brute Force

    startBF = time.time()

    closest_pair.timesEuclideanDistanceCalculated = 0

    closest_pair_brute = closest_pair.findClosestPairOfBF(points)
    timesEuclideanDistanceCalculatedBF = closest_pair.timesEuclideanDistanceCalculated

    endBF = time.time()
    
    print('\n'+ str(closest_pair_3d[:2]))
    print("Distance : ", closest_pair_3d[2])
    print(timesEuclideanDistanceCalculatedDNC, "times Euclidean distance calculated")
    print("Time taken: ",'%.15f' % (endDNC - startDNC), "seconds")
    

    print('\n' + str(closest_pair_brute[:2]))
    print("Distance : ", closest_pair_brute[2])
    print(timesEuclideanDistanceCalculatedBF, "times Euclidean distance calculated")
    print("Time taken: ",'%.15f' % (endBF - startBF), "seconds")

    print("Device used: " + platform.processor())

    display.display(points, closest_pair_3d, dimPoints)

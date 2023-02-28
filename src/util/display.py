import numpy as np
import matplotlib.pyplot as plt

def display(points, closest_pair, dimension):
    if (dimension == 3):
        red_points = []
        for p in closest_pair:
            for q in range(len(p) - 1):
                red_points.append(p[q])

        fig = plt.figure()
        ax = fig.add_subplot(projection = '3d')

        for x, y, z in points:
            if ((x, y, z) in red_points) :
                ax.scatter(x, y, z, marker='^', color='r')
            else:    
                ax.scatter(x, y, z, marker='o', color='g')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()
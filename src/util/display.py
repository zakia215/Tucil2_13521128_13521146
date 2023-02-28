import numpy as np
import matplotlib.pyplot as plt

def display(points, closest_pair, dimension):
    if (dimension == 3):
        numpied_points = np.array(points)

        fig = plt.figure()
        ax = fig.add_subplot(projection = '3d')

        for x, y, z in points:
            closestPlotted = False
            for i in range(len(closest_pair)):
                if ((x, y, z) in closest_pair[i][:2]) :
                    ax.scatter(x, y, z, marker='^', color='r')
                    closestPlotted = True

            if not closestPlotted:
                ax.scatter(x, y, z, marker='o', color='g')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()
import numpy as np
import matplotlib.pyplot as plt

def display(points, closest_pair, dimension):
    if (dimension == 3):
        numpied_points = np.array(points)

        fig = plt.figure()
        ax = fig.add_subplot(projection = '3d')

        for x, y, z in points:
            if ((x, y, z) in closest_pair[:2]) :
                ax.scatter(x, y, z, marker='^', color='r')
            else:    
                ax.scatter(x, y, z, marker='o', color='g')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()
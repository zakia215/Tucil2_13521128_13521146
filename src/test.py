import main
import random

if __name__ == '__main__':
    points = []
    # points = [(49, -364), (647, 422), (907, -978), (-802, 399), (946, 958), (-239, -954), (682, 516), (427, -956), (-125, -130), (-913, -386)]

    for i in range(10):
        points.append(tuple([random.randint(-1000, 1000) for i in range(int(3))]))
    
    main.quickSort(points, 0, len(points) - 1, 0)
    print(points)
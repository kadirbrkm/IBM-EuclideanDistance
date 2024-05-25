import math


points = [(2, 3), (5, 7), (1, 9), (4, 6), (8, 2)]


def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


min_distance = float('inf')  
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        min_distance = min(min_distance, distance)


print("Minimum Mesafe:", min_distance)

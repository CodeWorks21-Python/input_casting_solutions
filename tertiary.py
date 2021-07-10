# The distance from one point to another on a 2 Dimensional Plane is defined by the following equation:
#
#   d = sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)
#       where d = distance; sqrt() represent square root, or to the power of (1/2)

# Write a program that accepts two coordinates from the user and then calculates distance between the points.

# Example Output:
#   x1 = 5
#   y1 = 10
#
#   x2 = 35
#   y2 = -85
#
#   distance from (5, 10) to (35, -85) is 99.6423

from math import sqrt

x1 = float(input('x1 | '))
y1 = float(input('y1 | '))

x2 = float(input('x2 | '))
y2 = float(input('y2 | '))

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'distance from ({x1}, {y1}) to ({x2}, {y2}) is {d}')
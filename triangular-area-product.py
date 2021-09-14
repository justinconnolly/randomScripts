# Find the product of the smallest and largest triangles with the provided coordinates

from itertools import combinations

def getArea(points: list):
    a = points[0]
    b = points[1]
    c = points[2]
    area = (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) + 
            c[0] * (a[1] - b[1])) / 2
    return abs(area)


# Provided coordinates for the challenge
coords = [[-6, 3], [-5, 2], [-4, 0], [-11, 12],[-12, -2],
         [-4, -10], [-16, -20], [-13, -11],[-18, 17], [-8, -3],
         [4, -27], [0, 0], [-10, 6],[-10,0]]

# because itertools is amazing
combos = combinations(coords,3)

triangle_areas = []

# arbitrarily large minimum
min = 1000
max = 0

# this isn't entirely necessary, but I was interested in knowing the coordinates when a new min/max is found
for combo in combos:
    appendList = []
    area = getArea(combo)
    if area > max:
        print(f"New max: {area} from {combo}")
        max = area
    if area < min and area > 0:
        print(f"New min: {area} from {combo}")
        min = area
    if area > 0:
        appendList.append(area)
        appendList.append(combo)
        triangle_areas.append(appendList)


print(f"Min area: {min}")
print(f"Max area: {max}")
print(f"{min} * {max} = {min*max}")

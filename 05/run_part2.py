from collections import defaultdict


def unformatLine(line):
    line = line.split(' -> ')
    return line[0].split(',') + line[1].split(',')


def generateAllPoints(x1: int, y1: int, x2: int, y2: int):
    points = list()

    x_direction = 0 if x1 == x2 else 1 if x1 < x2 else -1
    y_direction = 0 if y1 == y2 else 1 if y1 < y2 else -1

    if x_direction != 0:
        y = y1
        for x in range(x1, x2, x_direction):
            points.append(str(x) + ',' + str(y))
            y += y_direction
    elif y_direction != 0:
        x = x1
        for y in range(y1, y2, y_direction):
            points.append(str(x) + ',' + str(y))
            x += x_direction

    points.append(str(x2) + ',' + str(y2))

    return points


def isOverlapping(x):
    return x > 1


with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')

lines = list(map(unformatLine, input_array))

point_occurances = defaultdict(int)
for line in lines:
    points = generateAllPoints(*map(int, line))
    for point in points:
        point_occurances[point] += 1

overlapping_points_total = len(list(filter(isOverlapping, point_occurances.values())))
print(overlapping_points_total)

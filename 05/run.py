from collections import defaultdict


def isNotDiagonal(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


def unformatLine(line):
    line = line.split(' -> ')
    return line[0].split(',') + line[1].split(',')


def generateAllPoints(x1: int, y1: int, x2: int, y2: int):
    points = list()

    for x in range(x1, x2, -1 if x1 > x2 else 1):
        points.append(str(x) + ',' + str(y1))
    for y in range(y1, y2, -1 if y1 > y2 else 1):
        points.append(str(x1) + ',' + str(y))
    points.append(str(x2) + ',' + str(y2))
    return points


def isOverlapping(x):
    return x > 1


with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')

lines = list(map(unformatLine, input_array))
non_diagonal_lines = list(filter(lambda line: isNotDiagonal(*line), lines))

point_occurances = defaultdict(int)
for line in non_diagonal_lines:
    points = generateAllPoints(*map(int, line))
    for point in points:
        point_occurances[point] += 1

overlapping_points_total = len(list(filter(isOverlapping, point_occurances.values())))
print(overlapping_points_total)

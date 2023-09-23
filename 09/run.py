with open('input.txt') as input_file:
    input_array = [[int(y) for y in list(x)] for x in input_file.read().split('\n')]

point_graph = {}
low_points = []
risk_level_total = 0
row_length = len(input_array[0])
input_height = len(input_array)

def checkAdjacent(start_x, start_y, direction):
    x = start_x
    y = start_y

    if direction == 'above':
        if x - 1 < 0:
            return False
        x -= 1
    elif direction == 'right':
        if y + 1 >= row_length:
            return False
        y += 1
    if direction == 'below':
        if x + 1 >= input_height:
            return False
        x += 1
    elif direction == 'left':
        if y - 1 < 0:
            return False
        y -= 1

    return {
        'value': input_array[x][y],
        'diff': input_array[x][y] - input_array[start_x][start_y],
        'cordinates': [x, y]
    }


for x, row in enumerate(input_array):
    for y, point in enumerate(row):
        adjacents = {}
        is_low_point = True
        for direction in ['above', 'right', 'below', 'left']:
            adjacents[direction] = checkAdjacent(x, y, direction)
            if adjacents[direction] and adjacents[direction]['diff'] <= 0:
                is_low_point = False

        if is_low_point:
            risk_level_total += point + 1
            low_points.append([x, y])

        if not point_graph.get(x):
            point_graph[x] = {}

        point_graph[x][y] = {
            'value': point,
            'cordinates': [x, y],
            'adjacents': adjacents
        }

print('Part 1: ' + str(risk_level_total))

def createSetValue(x, y):
    return str(x) + ',' + str(y)


def generateBasinCoods(x, y, basin_points):
    basin_points.add(createSetValue(x, y))
    for adjacentPoint in point_graph[x][y]['adjacents'].values():
        if adjacentPoint and adjacentPoint['diff'] >= 0 and adjacentPoint['value'] < 9 and createSetValue(*adjacentPoint['cordinates']) not in basin_points:
            basin_points |= generateBasinCoods(*adjacentPoint['cordinates'], basin_points)
    return basin_points


basin_sizes = []
for low_point in low_points:
    basin_sizes.append(len(generateBasinCoods(*low_point, set())))
basin_sizes.sort()
largest = basin_sizes[-3:]

print('Part 2: ' + str(largest[0] * largest[1] * largest[2]))
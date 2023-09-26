def countUnique(list):
    return len(set([str(x[0]) + ',' + str(x[1]) for x in list]))

def generateGraph(coords):
    graph = {}
    for x, y in coords:
        if x not in graph:
            graph[x] = {}
        if y not in graph[x]:
            graph[x][y] = {}

        graph[x][y] = 1
    return graph


def outputDisplay(coords):
    min_x = min([x[0] for x in coords])
    max_x = max([x[0] for x in coords]) + 1
    max_y = max([y[1] for y in coords]) + 1
    min_y = min([y[1] for y in coords])
    graph = generateGraph(coords)

    for y in range(min_y, max_y):
        for x in reversed(range(min_x, max_x)):
            print('#' if x in graph and y in graph[x] else '.', end='')
        print()

with open('input.txt') as input_file:
    coords, folds = input_file.read().split('\n\n')

coords = [list(map(int, coord.split(','))) for coord in coords.split('\n')]
folds = [fold[len('fold along '):].split('=') for fold in folds.split('\n')]

for fold_key, fold in enumerate(folds):
    fold_axis = fold[0]
    fold_position = int(fold[1])
    for key, coord in enumerate(coords):
        axis = 0 if fold_axis == 'x' else 1
        val = int(coord[axis])
        if (fold_axis == 'x' and val < fold_position):
            coords[key][axis] = (fold_position + (fold_position - val))
        elif (fold_axis == 'y' and val > fold_position):
            coords[key][axis] = (fold_position + (fold_position - val))
        if fold_axis == 'x':
            coords[key][axis] -= fold_position + 1
    if fold_key == 0:
        print('Part 1: ' + str(countUnique(coords)))

print('Part 2:')
outputDisplay(coords)

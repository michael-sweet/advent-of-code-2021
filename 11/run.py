def increaseEnergy(x, y):
    grid[x][y] += 1
    if grid[x][y] > 9 and createSetValue(x, y) not in flashes:
        simulateFlash(x, y)


def simulateFlash(x, y):
    global total_flashes
    total_flashes += 1
    flashes.add(createSetValue(x, y))
    increaseAdjacent(x, y)


def createSetValue(x, y):
    return str(x) + ',' + str(y)


def increaseAdjacent(x, y):
    min_x = x - 1 if x - 1 >= 0 else x
    min_y = y - 1 if y - 1 >= 0 else y
    max_x = x + 1 if x + 1 < max_rows else x
    max_y = y + 1 if y + 1 < max_cols else y

    for adj_x in range(min_x, max_x + 1):
        for adj_y in range(min_y, max_y + 1):
            if not (adj_x == x and adj_y == y):
                increaseEnergy(adj_x, adj_y)


def resetEnergy(grid):
    for x, row in enumerate(grid):
        for y, energy_level in enumerate(row):
            if energy_level > 9:
                grid[x][y] = 0
    return grid


with open('input.txt') as input_file:
    input_array = [[int(y) for y in list(x)]
                   for x in input_file.read().split('\n')]

grid = [list(x) for x in input_array]
max_rows = len(grid)
max_cols = len(grid[0])
flashes = set()
total_flashes = 0
first_all_flash = None

steps = 100
counter = 0
while not first_all_flash:
    for x, row in enumerate(grid):
        for y, energy_level in enumerate(row):
            increaseEnergy(x, y)
    counter += 1
    if len(flashes) == max_rows * max_cols and not first_all_flash:
        first_all_flash = counter
    flashes = set()
    grid = resetEnergy(grid)
    if counter == steps:
        print('Part 1: ' + str(total_flashes))

print('Part 2: ' + str(first_all_flash))

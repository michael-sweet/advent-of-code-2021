with open('input.txt') as input_file:
    grid = [list(map(int, x)) for x in input_file.read().split('\n')]

start = (0, 0)
end = (len(grid[0]) - 1, len(grid) - 1)
visited = set()
min_dist = {}
min_dist_unvisited = {}


def getUnvisitedAdjacent(node):
    x, y = node
    updates = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    adjacents = []
    for x_move, y_move in updates:
        new_x = x + x_move
        new_y = y + y_move
        if new_x < len(grid[0]) and new_x >= 0 and new_y < len(grid) and new_y >= 0:
            if (new_x, new_y) not in visited:
                adjacents.append((new_x, new_y))
    return adjacents


def updateNode(node):
    global visited
    visited.add(node)
    del min_dist_unvisited[node]
    for adjacent in getUnvisitedAdjacent(node):
        updateDistance(adjacent, min_dist[node])


def updateDistance(node, current_dist):
    global min_dist
    dist = current_dist + grid[node[1]][node[0]]
    if node in min_dist:
        min_dist[node] = min(dist, min_dist[node])
        min_dist_unvisited[node] = min_dist[node]
    else:
        min_dist[node] = dist
        min_dist_unvisited[node] = dist


def getMinDistUnvisitedNode():
    min_d = None
    min_node = None
    for node, dist in min_dist_unvisited.items():
        if (not min_d or dist < min_d):
            min_d = dist
            min_node = node
    return min_node


def increaseGrid(amount):
    global grid
    max_x = len(grid[0])
    max_y = len(grid)
    for y in range(max_y):
        for x in range(max_x, max_x * amount):
            prev_val = grid[y][x - max_x]
            grid[y].append(prev_val + 1 if prev_val < 9 else 1)

    max_x = len(grid[0])
    for y in range(max_y, max_y * amount):
        row = []
        for x in range(max_x):
            prev_val = grid[y - max_y][x]
            row.append(prev_val + 1 if prev_val < 9 else 1)
        grid.append(row)


def run():
    current = start
    min_dist[current] = 0
    min_dist_unvisited[current] = 0
    updateNode(current)
    while end not in visited:
        current = getMinDistUnvisitedNode()
        updateNode(current)


run()
print('Part 1: ' + str(min_dist[end]))


increaseGrid(5)

start = (0, 0)
end = (len(grid[0]) - 1, len(grid) - 1)
visited = set()
min_dist = {}
min_dist_unvisited = {}

run()
print('Part 2: ' + str(min_dist[end]))

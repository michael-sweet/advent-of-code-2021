with open('input.txt') as input_file:
    input = input_file.read()

target = [[int(y) for y in x[2:].split('..')] for x in input[13:].split(', ')]
max_height_reached = 0
target_hit_count = 0

def step(position, velocity):
    x, y = position
    vx, vy = velocity

    x += vx
    y += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    vy -= 1

    return [[x, y], [vx, vy]]

def simulate(velocity):
    global max_height_reached
    global target_hit_count
    position = [0, 0]
    height_reached = max_height_reached

    while True:
        position, velocity = step(position, velocity)
        height_reached = position[1] if position[1] > height_reached else height_reached

        if targetReached(*position):
            max_height_reached = height_reached
            target_hit_count += 1
            return True
        elif targetMissed(*position):
            return False


def targetReached(x, y):
    return (
        x >= target[0][0] and
        x <= target[0][1] and
        y <= target[1][1] and
        y >= target[1][0]
    )

def targetMissed(x, y):
    return (
        x > target[0][1] or
        y < target[1][0]
    )


c = 10
for x in range(0, target[0][1] * c):
    for y in range(target[1][0] * c, -target[1][0] * c):
        simulate([x, y])
        pass

print('Part 1: ' + str(max_height_reached))
print('Part 2: ' + str(target_hit_count))
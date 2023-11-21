with open('input.txt') as input_file:
    input = input_file.read().split('\n')

part1_instructions = []
instructions = []
for line in input:
    state, coords = line.split(' ')
    cuboid = tuple(tuple(int(val) for val in coord[2:].split('..')) for coord in coords.split(','))
    instructions.append((state, cuboid))
    for start, end in cuboid:
        if start >= -50 and start <= 50 and end >= -50 and end <= 50:
            part1_instructions.append((state, cuboid))


LOWER, UPPER = range(2)
X, Y, Z = range(3)


def intersects(a, b):
    for axis in [X, Y, Z]:
        if a[axis][LOWER] > b[axis][UPPER] or a[axis][UPPER] < b[axis][LOWER]:
            return False
    return True


def cut(cuboid, cut_axis, cut_position, cut_bound):
    if (
        cut_position < cuboid[cut_axis][LOWER] or
        cut_position > cuboid[cut_axis][UPPER] or
        cut_position == cuboid[cut_axis][cut_bound]
    ):
        return [cuboid]
    new_cuboids = []
    for bound in [LOWER, UPPER]:
        new_cuboid = [list(coords) for coords in cuboid]
        if cut_bound == LOWER:
            new_cuboid[cut_axis][bound] = cut_position - (0 if bound == LOWER else 1)
        else:
            new_cuboid[cut_axis][bound] = cut_position + (1 if bound == LOWER else 0)
        new_cuboids.append(tuple(tuple(coords) for coords in new_cuboid))
    return new_cuboids


def slice(a, b):
    to_slice = {b}
    for axis in [X, Y, Z]:
        for bound in [LOWER, UPPER]:
            new_cuboids = set()
            for cuboid in to_slice:
                new_cuboids.update(cut(cuboid, axis, a[axis][bound], bound))
            to_slice = new_cuboids
    return to_slice


def difference(a, b):
    a_slice = slice(b, a)
    b_slice = slice(a, b)
    return b_slice.difference(a_slice)


def calculateArea(cuboid):
    area = 1
    for axis in [X, Y, Z]:
        area *= abs(cuboid[axis][UPPER] - cuboid[axis][LOWER]) + 1
    return area


def calculateTotalArea(cuboids):
    area = 0
    for cuboid in cuboids:
        area += calculateArea(cuboid)
    return area


def run(instructions):
    on_set = set()
    for state, cuboid in instructions:
        if len(on_set) == 0:
            on_set.add(cuboid)
            continue
        new_on_set = set()
        for on_cuboid in on_set:
            if intersects(cuboid, on_cuboid):
                new_on_set.update(difference(cuboid, on_cuboid))
            else:
                new_on_set.add(on_cuboid)
        if state == 'on':
            new_on_set.add(cuboid)
        on_set = new_on_set
    return on_set


print('Part 1:', calculateTotalArea(run(part1_instructions)))
print('Part 2:', calculateTotalArea(run(instructions)))
import math

with open('input.txt') as input_file:
    scanners = [[tuple(int(z) for z in y.split(',')) for y in x.split('\n')[1:]] for x in input_file.read().split('\n\n')]

required_beacon_overlap = 12


def calculateDistance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def calculateDirection(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b

    return (x2 - x1, y2 - y1, z2 - z1)


# scanner number => distances between points => points
scanner_distances = []
for scanner in scanners:
    distances = {}
    for a in scanner:
        for b in scanner:
            if a != b:
                distances[calculateDistance(a, b)] = [a, b]
    scanner_distances.append(distances)


# scanner number => overlapping scanner numbers => overlapping points
scanner_overlap = {}
for x, a in enumerate(scanner_distances):
    overlaps = {}
    for y, b in enumerate(scanner_distances):
        if x != y:
            intersect_distances = set(a.keys()).intersection(set(b.keys()))
            overlapping_points = [scanner_distances[y][dist] for dist in intersect_distances]
            overlapping_points = set([item for sublist in overlapping_points for item in sublist])

            if len(overlapping_points) >= required_beacon_overlap:
                common_distance = intersect_distances.pop()
                overlaps[y] = {
                    x: scanner_distances[x][common_distance],
                    y: scanner_distances[y][common_distance]
                }
    scanner_overlap[x] = overlaps


# list of functions that adjust a point for one of the 24 orientations
a, b, c = [1, 2, 3]
reorients = []
for a, b, c in [(a, b, c), (b, c, a), (c, a, b)]:
    for a, b, c in [(a, b, c), (-a, c, b)]:
        for a, b, c in [(a, b, c), (a, -b, -c), (a, -c, b), (a, c, -b)]:
            def reorient(point, a=a, b=b, c=c):
                return (
                    point[abs(a) - 1] * (a / abs(a)),
                    point[abs(b) - 1] * (b / abs(b)),
                    point[abs(c) - 1] * (c / abs(c))
                )
            reorients.append(reorient)

# returns the reorient function that sets the correct orientation of a point relative to an origin
def pickReorientFunction(origin_points, points):
    origin_direction = calculateDirection(*origin_points)
    for reorient in reorients:
        a = reorient(points[0])
        b = reorient(points[1])
        if origin_direction == calculateDirection(a, b):
            return 0, reorient
        elif origin_direction == calculateDirection(b, a):
            return 1, reorient


def transform(origin_point, matching_point, points):
    difference = tuple(origin_point[x] - matching_point[x] for x in range(0, len(origin_point)))
    transformed_points = [tuple(a + b for a, b in zip(point, difference)) for point in points]

    return transformed_points, difference

scanner_pairs_added = set()
def combineScanners(scanner_a):
    global scanner_pairs_added
    beacons = set()
    overlap_a = scanner_overlap[scanner_a]
    absolute_scanners = []
    beacons.update((scanners[scanner_a]))
    for scanner_b, overlap_points in overlap_a.items():
        if frozenset([scanner_a, scanner_b]) not in scanner_pairs_added:
            scanner_pairs_added.add(frozenset([scanner_a, scanner_b]))
            matching_point, reorient = pickReorientFunction(overlap_points[scanner_a], overlap_points[scanner_b])
            relative_scanners, points_b = combineScanners(scanner_b)
            reoriented_points = [reorient(x) for x in points_b]
            tranformed_points, transformed_scanner = transform(overlap_points[scanner_a][0], reorient(overlap_points[scanner_b][matching_point]), reoriented_points)
            relative_scanners, _ = transform(overlap_points[scanner_a][0], reorient(overlap_points[scanner_b][matching_point]), [reorient(x) for x in relative_scanners])
            absolute_scanners.extend(relative_scanners)
            absolute_scanners.append(transformed_scanner)
            beacons.update(tranformed_points)

    return absolute_scanners, beacons


def manhattanDistance(a, b):
    dist = int(sum([abs(a[x] - b[x]) for x in range(len(a))]))
    return dist


absolute_scanners, beacons = combineScanners(0)
absolute_scanners.append((0, 0, 0))

total_distances = []
for x, _ in enumerate(absolute_scanners):
    for y, _ in enumerate(absolute_scanners):
        total_distances.append(manhattanDistance(absolute_scanners[x], absolute_scanners[y]))


print('Part 1:', len(beacons))
print('Part 2:', max(total_distances))

part = 2

with open('input.txt') as depth_file:
    depth_array = depth_file.read().split()
depth_array = list(map(int, depth_array))

if part == 2:
    for i, depth in enumerate(depth_array):
        depth_array[i] = sum(depth_array[i:i+3])

count = 0
prev_depth = False
for i, depth in enumerate(depth_array):
    if prev_depth is False:
        print('{0} (N/A - no previous measurement)'.format(depth))
    elif depth > prev_depth:
        count = count + 1
        print('{0} (increased)'.format(depth))
    elif depth == prev_depth:
        print('{0} (no change)'.format(depth))
    else:
        print('{0} (decreased)'.format(depth))
    prev_depth = depth

print(count)
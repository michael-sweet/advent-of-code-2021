with open('input.txt') as input_file:
    positions = list(map(int, input_file.read().split(',')))

positions.sort()
median_position = positions[int(len(positions) / 2)]
fuel_used = sum(map(lambda x: abs(x - median_position), positions))
print(fuel_used)

def calculateFuel(position, average_position):
    x = abs(position - average_position)
    return int(((x * x) + x) / 2)


with open('input.txt') as input_file:
    positions = list(map(int, input_file.read().split(',')))

average_position = int(sum(positions) / len(positions))
fuel_used = sum(map(lambda p: calculateFuel(p, average_position), positions))
print(fuel_used)

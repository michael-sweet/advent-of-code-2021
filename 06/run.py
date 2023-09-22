def simulateFish(fish, days):
    while days > 0:
        old_fish = fish.copy()
        for x in range(0, 8):
            if x == 0:
                birthing_fish = old_fish[0]
            fish[x] = old_fish[x + 1]
        fish[6] += birthing_fish
        fish[8] = birthing_fish
        days -= 1
    return sum(fish.values())


with open('input.txt') as input_file:
    fish_list = list(map(int, input_file.read().split(',')))

fish = {}
for x in range(0, 8 + 1):
    fish[x] = fish_list.count(x)

print('Part 1: ' + str(simulateFish(fish.copy(), 80)))
print('Part 2: ' + str(simulateFish(fish.copy(), 256)))

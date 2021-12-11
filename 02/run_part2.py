with open('input.txt') as command_file:
    command_array = command_file.read().split('\n')

depth = 0
position = 0
aim = 0

for i, command in enumerate(command_array):
    action, amount = command.split(' ')
    amount = int(amount)

    if action == 'forward':
        position += amount
        depth += aim * amount
    elif action == 'up':
        aim -= amount
    elif action == 'down':
        aim += amount

total = depth * position
print(total)
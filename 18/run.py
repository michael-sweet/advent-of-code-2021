import math
import ast

def explode(snailfish:str):
    explosion_start, explosion_end, left_val, right_val = locateExplosion(snailfish)
    if not explosion_start:
        return snailfish

    snailfish = propagateExplosion(snailfish, left_val, explosion_start, 'left')
    explosion_start, explosion_end, left_val, right_val = locateExplosion(snailfish)
    snailfish = propagateExplosion(snailfish, right_val, explosion_end, 'right')
    explosion_start, explosion_end, left_val, right_val = locateExplosion(snailfish)
    snailfish = snailfish[:explosion_start] + '0' + snailfish[explosion_end:]

    return snailfish


def locateExplosion(snailfish:str):
    depth = 0
    explosion_start = False
    for i, char in enumerate(snailfish):
        depth += 1 if char == '[' else -1 if char == ']' else 0
        if depth > max_depth:
            explosion_start = i
            break

    if not explosion_start:
        return [False, False, False, False]

    explosion_end = snailfish.find(']', explosion_start) + 1
    explosion_pair = snailfish[explosion_start:explosion_end]
    left_val, right_val = explosion_pair[1:-1].split(',')

    return [explosion_start, explosion_end, left_val, right_val]


def propagateExplosion(snailfish:str, value:int, position:int, direction:str):
    len = 0
    start = False
    snailfish_iterable = enumerate(snailfish[position:]) if direction == 'right' else reversed(list(enumerate(snailfish[:position])))

    for i, char in snailfish_iterable:
        try:
            int(char)
            if direction == 'right' and not start:
                start = position + i
            if direction == 'left':
                start = i
            len += 1
        except:
            if len > 0:
                break

    if start:
        snailfish = snailfish[:start] + str(int(snailfish[start:start+len]) + int(value)) + snailfish[start+len:]

    return snailfish


def _split(snailfish:list, complete = False):
    for i, x in enumerate(snailfish):
        if complete:
            return [snailfish, True]
        elif type(x) == int and x >= max_number:
            snailfish[i] = [math.floor(x / 2), math.ceil(x / 2)]
            return [snailfish, True]
        elif type(x) == list:
            snailfish[i], complete = _split(x)

    return [snailfish, complete]


def split(snailfish:list):
    snailfish, _ = _split(snailfish)
    return snailfish


def reduce(snailfish:str):
    while True:
        reduced_snailfish = explode(snailfish)
        if reduced_snailfish == snailfish:
            reduced_snailfish = str(split(ast.literal_eval(snailfish)))
            if reduced_snailfish == snailfish:
                break
        snailfish = reduced_snailfish

    return snailfish


def add(a:str, b:str):
    return reduce('[' + a + ',' + b + ']')


def calculateMagnitude(snailfish:list):
    a, b = snailfish
    if type(a) == list:
        a = 3 * calculateMagnitude(a)
    else:
        a *= 3
    if type(b) == list:
        b = 2 * calculateMagnitude(b)
    else:
        b *= 2

    return a + b


with open('input.txt') as input_file:
    snailfish = input_file.read().split('\n')

max_depth = 4
max_number = 10

total = snailfish[0]
for x in snailfish[1:]:
    total = add(total, x)

magnitude = calculateMagnitude(ast.literal_eval(total))
print('Part 1:', magnitude)

largest_magnitude = 0
for x in snailfish:
    for y in snailfish:
        if x != y:
            res1 = calculateMagnitude(ast.literal_eval(add(x, y)))
            res2 = calculateMagnitude(ast.literal_eval(add(y, x)))
            if res1 > largest_magnitude:
                largest_magnitude = res1
            if res2 > largest_magnitude:
                largest_magnitude = res2

print('Part 2:', largest_magnitude)
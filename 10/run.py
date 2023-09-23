brackets = {
    '(': {'type': 'round', 'opening': True, 'points': 1},
    '[': {'type': 'square', 'opening': True, 'points': 2},
    '{': {'type': 'curly', 'opening': True, 'points': 3},
    '<': {'type': 'angle', 'opening': True, 'points': 4},
    ')': {'type': 'round', 'opening': False, 'points': 3},
    ']': {'type': 'square', 'opening': False, 'points': 57},
    '}': {'type': 'curly', 'opening': False, 'points': 1197},
    '>': {'type': 'angle', 'opening': False, 'points': 25137}
}

with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')


def findCorruptChar(line):
    stack = []
    for char in line:
        if brackets[char]['opening']:
            stack.append(char)
        elif brackets[char]['type'] != brackets[stack.pop()]['type']:
            return [char, None]
    return [None, stack]


corruption_score = 0
incomplete_scores = []
for line in input_array:
    incomplete_score = 0
    corrupt_char, incomplete_stack = findCorruptChar(line)
    if corrupt_char:
        corruption_score += brackets[corrupt_char]['points']
    elif incomplete_stack:
        for char in reversed(incomplete_stack):
            incomplete_score *= 5
            incomplete_score += brackets[char]['points']
        incomplete_scores.append(incomplete_score)

incomplete_scores.sort()
media_incomplete_score = incomplete_scores[int(len(incomplete_scores) / 2)]

print('Part 1: ' + str(corruption_score))
print('Part 2: ' + str(media_incomplete_score))

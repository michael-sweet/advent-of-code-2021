def unformatInputLine(line):
    return [[sorted(y) for y in x.split(' ')] for x in line.split(' | ')]


def resolveSegments(segments):
    results = {}

    for number, length in {1: 2, 4: 4, 7: 3, 8: 7}.items():
        results[number] = [s for s in segments if len(s) == length].pop()

    results[9] = [s for s in segments if len(s) == 6 and not set(results[4]) - set(s)].pop()
    results[0] = [s for s in segments if len(s) == 6 and results[9] != s and not set(results[1]) - set(s)].pop()
    results[6] = [s for s in segments if len(s) == 6 and results[9] != s and results[0] != s].pop()
    results[3] = [s for s in segments if len(s) == 5 and not set(results[1]) - set(s)].pop()
    results[5] = [s for s in segments if len(s) == 5 and not set(s) - set(results[6])].pop()
    results[2] = [s for s in segments if s not in results.values()].pop()

    return results


def resolveOutput(output, segment_results):
    output_result = ''
    for o in output:
        output_result += str([key for key, result in segment_results.items() if o == result].pop())

    return int(output_result)


with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')

total = 0
for input_line in input_array:
    segments, output = unformatInputLine(input_line)
    segment_results = resolveSegments(segments)
    total += resolveOutput(output, segment_results)

print(total)


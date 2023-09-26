def createInsertionDict(input_lines):
    insertion_dict = {}
    for line in input_lines:
        i, o = line.split(' -> ')
        a, b = list(i)
        insertion_dict[a + b] = o
    return insertion_dict


def createPairDict(template):
    pair_dict = {}
    for key, char in enumerate(template):
        if len(template) > key + 1:
            pair = char + template[key + 1]
            if pair not in pair_dict:
                pair_dict[pair] = 0
            pair_dict[pair] += 1
    return pair_dict


def getFrequencies(dict, template):
    freq = {}
    for pair, count in dict.items():
        if pair[0] not in freq:
            freq[pair[0]] = 0
        freq[pair[0]] += count
    end_letter = list(template).pop()
    if end_letter not in freq:
        freq[end_letter] = 0
    freq[end_letter] += 1
    return freq


def run(steps, pair_dict, rules):
    for x in range(0, steps):
        new_pair_dict = {}
        for pair, count in pair_dict.items():
            if pair in rules:
                new_pairs = [pair[0] + rules[pair], rules[pair] + pair[1]]
                for new_pair in new_pairs:
                    if new_pair not in new_pair_dict:
                        new_pair_dict[new_pair] = 0
                    new_pair_dict[new_pair] += count
        pair_dict = new_pair_dict
    return pair_dict



with open('input.txt') as input_file:
    template, rules = input_file.read().split('\n\n')

rules = createInsertionDict(rules.split('\n'))
pair_dict = createPairDict(template)
final_pair_dict = run(40, pair_dict, rules)
frequencies = getFrequencies(final_pair_dict, template)
sorted_freq = sorted(frequencies.values())

print(sorted_freq[-1:].pop() - sorted_freq[:1].pop())

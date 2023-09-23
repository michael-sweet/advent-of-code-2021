with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')

output_lengths = list(map(lambda x: list(map(len, x.split(' | ')[1].split(' '))), input_array))
output_lengths = [item for sublist in output_lengths for item in sublist]

unique_digit_count = 0
for x in [2, 4, 3, 7]:
    unique_digit_count += output_lengths.count(x)

print(unique_digit_count)

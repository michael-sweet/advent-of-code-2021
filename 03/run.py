def getCounts(input_array):
    value_counts = [0] * len(input_array[0])
    for byte in input_array:
        for x, bit in enumerate(byte):
            value_counts[x] += int(bit)
    return value_counts

def getBinaryRate(input_array, common_bit, uncommon_bit):
    value_counts = getCounts(input_array)
    binary_rate = ''
    for count in value_counts:
        if count >= len(input_array) / 2:
            binary_rate += str(common_bit)
        else:
            binary_rate += str(uncommon_bit)
    return binary_rate

def getRating(input_array, common_bit, uncommon_bit):
    input_array = input_array[:]
    byte_len = len(input_array[0])
    for x in range(byte_len):
        binary_rate = getBinaryRate(input_array, common_bit, uncommon_bit)
        input_array_to_remove = []
        for y, input_byte in enumerate(input_array):
            if int(binary_rate[x]) != int(input_byte[x]):
                input_array_to_remove.append(input_byte)
        input_array = list(set(input_array) & set(input_array_to_remove))
        if len(input_array) == 1:
            return input_array[0]
    pass

with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')

gamma_rate_binary = getBinaryRate(input_array, 1, 0)
epsilon_rate_binary = getBinaryRate(input_array, 0, 1)
gamma_rate = int(gamma_rate_binary, 2)
epsilon_rate = int(epsilon_rate_binary, 2)

print('Part 1: {0}'.format(gamma_rate * epsilon_rate))

oxygen_rating_binary = getRating(input_array, 1, 0)
co2_rating_binary = getRating(input_array, 0, 1)
oxygen_rating = int(oxygen_rating_binary, 2)
co2_rating = int(co2_rating_binary, 2)

print('Part 2: {0}'.format(oxygen_rating * co2_rating))

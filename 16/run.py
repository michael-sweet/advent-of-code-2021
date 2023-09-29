import math

with open('input.txt') as input_file:
    input = input_file.read()


def hexToBinary(hex):
    return ''.join([bin(int(h, 16))[2:].zfill(4) for h in hex])


def processPacketHeader(input):
    version = int(input[:3], 2)
    type_id = int(input[3:6], 2)
    input = input[6:]
    return [version, type_id, input]


def processLiteral(input):
    bin_val = ''
    while True:
        group = input[:5]
        bin_val += group[1:]
        input = input[5:]
        if group[0] == '0':
            return int(bin_val, 2), input


def processOperator(input):
    length_type_id = input[:1]
    input = input[1:]
    values = []
    if length_type_id == '0':
        len = int(input[:15], 2)
        current_input = input[15:15+len]
        input = input[15+len:]
        while current_input and int(current_input) != 0:
            value, current_input = processPacket(current_input)
            values.append(value)
    else:
        len = int(input[:11], 2)
        input = input[11:]
        for _ in range(len):
            value, input = processPacket(input)
            values.append(value)
    return values, input


version_sum = 0
def processPacket(input):
    global version_sum
    version, type_id, input = processPacketHeader(input)
    version_sum += version
    if type_id == 4:
        return processLiteral(input)
    else:
        values, input = processOperator(input)
        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = math.prod(values)
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        elif type_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            value = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            value = 1 if values[0] == values[1] else 0
        return [value, input]


value, _ = processPacket(hexToBinary(input))
print('Part 1: ' + str(version_sum))
print('Part 2: ' + str(value))

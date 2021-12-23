def checkCard(card, drawn_numbers):
    for row in card:
        if len(row) == len(list(set(row) & set(drawn_numbers))):
            return True
    for x in range(len(card[0])):
        column = [row[x] for row in card]
        if len(column) == len(list(set(column) & set(drawn_numbers))):
            return True
    return False

def calculateScore(card, drawn_numbers):
    last_drawn_number = drawn_numbers[-1]
    unmarked_card = list(map(lambda row: list(set(row) - set(drawn_numbers)), card))
    return sum(map(sum, unmarked_card)) * last_drawn_number

with open('input.txt') as input_file:
    input_array = input_file.read().split('\n')

all_drawn_numbers = list(map(int, input_array[:1][0].split(',')))
input_array = input_array[1:]

bingo_cards = []
input_array = list(filter(None, input_array))

while len(input_array) > 0:
    bingo_cards.append(list(map(lambda row: list(map(int, filter(None, row.split(' ')))), input_array[:5])))
    input_array = input_array[5:]

first_found = False
for x in range(4, len(all_drawn_numbers)):
    drawn_numbers = all_drawn_numbers[:x]
    for y, card in enumerate(bingo_cards):
        if checkCard(card, drawn_numbers):
            last_drawn_numbers = drawn_numbers
            last_card = card
            del bingo_cards[y]
            if not first_found:
                print('Part 1:', calculateScore(card, drawn_numbers))
                first_found = True
                break

print('Part 2:', calculateScore(last_card, last_drawn_numbers))
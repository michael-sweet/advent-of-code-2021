class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def createInsertionDict(input_lines):
    insertion_dict = {}
    for line in input_lines:
        i, o = line.split(' -> ')
        a, b = list(i)
        insertion_dict[a + b] = o
    return insertion_dict

def createCharLinkedList(input_str):
    prev = None
    for char in reversed(input_str):
        prev = LinkedList(char, prev)
    return prev

def outputLinkedList(pointer):
    while pointer is not None:
        print(pointer.value, end='')
        pointer = pointer.next
    print()

def getFrequencies(pointer):
    freq = {}
    while pointer is not None:
        if pointer.value not in freq:
            freq[pointer.value] = 0
        freq[pointer.value] += 1
        pointer = pointer.next
    return freq


def run(steps, start, rules):
    for x in range(0, steps):
        pointer = start
        while pointer.next is not None:
            a = pointer
            b = pointer.next
            if a.value + b.value in rules:
                new = LinkedList(rules[a.value + b.value], b)
                a.next = new
            pointer = b


with open('input.txt') as input_file:
    template, rules = input_file.read().split('\n\n')

rules = createInsertionDict(rules.split('\n'))

start = createCharLinkedList(template)
run(10, start, rules)
frequencies = getFrequencies(start)
sorted_freq = sorted(frequencies.values())
print(sorted_freq[-1:].pop() - sorted_freq[:1].pop())

with open('input.txt') as input_file:
    starting_positions = [int(x.split(' ')[-1:][0]) for x in input_file.read().split('\n')]

SCORES, POSITIONS = range(2)


def hashGame(game):
    return tuple(game[SCORES]), tuple(game[POSITIONS])


def unhashGame(game):
    return [list(game[SCORES]), list(game[POSITIONS])]


def newGame():
    new_game = [[], []]
    for i in range(2):
        new_game[SCORES].append(0)
        new_game[POSITIONS].append(starting_positions[i])
    return hashGame(new_game)


def rollDice(roll_tracker):
    roll_tracker['roll_count'] += 1
    roll_tracker['last_roll'] = 1 + roll_tracker['last_roll'] if roll_tracker['last_roll'] < 100 else 1
    return roll_tracker['last_roll']


def move(current_position, roll):
    pos = (current_position + roll) % 10
    return pos if pos > 0 else 10


def getWinner(game, threshold):
    for player, score in enumerate(game[SCORES]):
        if score >= threshold:
            return player
    return False


def takeTurn(game, player, roll):
    game = unhashGame(game)
    position = move(game[POSITIONS][player], roll)
    game[POSITIONS][player] = position
    game[SCORES][player] += position
    return hashGame(game)


def playPracticeGame():
    practice_game = newGame()
    roll_tracker = {'roll_count': 0, 'last_roll': 0}
    while True:
        for player in range(2):
            roll = rollDice(roll_tracker) + rollDice(roll_tracker) + rollDice(roll_tracker)
            practice_game = takeTurn(practice_game, player, roll)
            winner = getWinner(practice_game, 1000)
            if winner is not False:
                loser = set(range(2)).difference([winner]).pop()
                return practice_game, roll_tracker, loser


def play(game = newGame(), player = 0, win_log = {}):
    total_wins = [0, 0]
    next_player = 1 if player == 0 else 0
    roll_counts = [x + y + z for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]
    roll_occurances = {element: roll_counts.count(element) for element in set(roll_counts)}

    for roll, count in roll_occurances.items():
        updated_game = takeTurn(game, player, roll)
        winner = getWinner(updated_game, 21)
        if winner is not False:
            total_wins[winner] += count
        elif (updated_game, player) in win_log:
            total_wins = [x + (y * count) for x, y in zip(total_wins, win_log[(updated_game, player)])]
        else:
            wins = play(updated_game, next_player, win_log)
            win_log[(updated_game, player)] = wins
            total_wins = [x + (y * count) for x, y in zip(total_wins, wins)]
    return total_wins


practice_game, roll_tracker, loser = playPracticeGame()
print('Part 1:', practice_game[SCORES][loser] * roll_tracker['roll_count'])
print('Part 2:', max(play()))

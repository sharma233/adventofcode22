#dict that defines what each symbol loses to
GAME_RULES = {
    "Rock":"Paper",
    "Paper":"Scissors",
    "Scissors":"Rock"
}

SHAPE_SCORES = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

OUTCOME_SCORES = {
    "WIN": 6,
    "DRAW": 3,
    "LOSS": 0
}

ENCRYPTION_GUIDE = {
    "A":"Rock",
    "B":"Paper",
    "C":"Scissors",
    "X":"Rock",
    "Y":"Paper",
    "Z":"Scissors"
}

ENCRYPTION_GUIDE_PART_2 = {
    "X": "LOSS",
    "Y": "DRAW",
    "Z": "WIN"
}

def part1():
    score = 0
    with open("inputs/day2/real.txt", "r") as problem_input:
        for line in problem_input:
            outcome = ""
            moves = line.split()
            opp_move = ENCRYPTION_GUIDE.get(moves[0])
            player_move = ENCRYPTION_GUIDE.get(moves[1])

            #win condition
            if(GAME_RULES.get(opp_move) == player_move):
                outcome = "WIN"
            elif(opp_move == player_move):
                outcome = "DRAW"
            else:
                outcome = "LOSS"

            score = score + SHAPE_SCORES.get(player_move) + OUTCOME_SCORES.get(outcome)
    return score

def part2():
    score = 0
    with open("inputs/day2/real.txt", "r") as problem_input:
        for line in problem_input:
            moves = line.split()
            opp_move = ENCRYPTION_GUIDE.get(moves[0])
            outcome = ENCRYPTION_GUIDE_PART_2.get(moves[1])
            player_move = ""

            match outcome:
                case "WIN":
                    player_move = GAME_RULES.get(opp_move)
                case "DRAW":
                    player_move = opp_move
                case "LOSS":
                    player_move = GAME_RULES.get(GAME_RULES.get(opp_move))

            score = score + SHAPE_SCORES.get(player_move) + OUTCOME_SCORES.get(outcome)
    return score

part1_score = part1()
print("PART 1 SCORE: " + str(part1_score))

part2_score = part2()
print("PART 2 SCORE: " + str(part2_score))

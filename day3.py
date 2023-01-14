def calculate_score(char):
    ascii_start = 96 if char.islower() else 38
    return ord(char) - ascii_start

def part1():
    score = 0
    with open("inputs/day3/real.txt", "r") as problem_input:
        for line in problem_input:
            half_len = int(len(line)/2)
            first_set = set(line[0:half_len])
            second_set = set(line[half_len:])
            common_element = first_set.intersection(second_set).pop()
            score += calculate_score(common_element)
    return score


def part2():
    score = 0
    with open("inputs/day3/real.txt", "r") as problem_input:
        lines = problem_input.read().splitlines()
        i = 0
        while i < len(lines):
            first_set = set(lines[i])
            second_set = set(lines[i+1])
            third_set = set(lines[i+2])

            common_element = first_set.intersection(second_set).intersection(third_set).pop()
            score += calculate_score(common_element)
            i += 3
    return score

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))

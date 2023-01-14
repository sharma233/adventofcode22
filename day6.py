def part1():
    with open("inputs/day6/real.txt", "r") as problem_input:
        for line in problem_input:
            return n_unique_characters_set(line, 4)

def part2():
    with open("inputs/day6/real.txt", "r") as problem_input:
        for line in problem_input:
            return n_unique_characters_set(line, 14)

#initial brute force solution
def n_unique_characters(string, n):
    for idx, char in enumerate(string):
        seen = [char]
        for j in range(idx+1, len(string)):
            if len(seen) == n:
                return j
            elif string[j] in seen:
                break
            else:
                seen.append(string[j])

#implementing a secondary set solution
def n_unique_characters_set(string, n):
    for i in range(0, len(string)):
        substring_set = set(string[i:i+n])
        if(len(substring_set) == n):
            return i+n

print("part 1: " + str(part1()))
print("part 2: " + str(part2()))
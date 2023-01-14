def ranges_completely_overlap(range1, range2):
    range1_start, range1_end = range1.split("-")
    range1_range = int(range1_end) - int(range1_start)

    range2_start, range2_end = range2.split("-")
    range2_range = int(range2_end) - int(range2_start)

    if int(range1_start) > int(range2_start):
        return int(range2_end) >= int(range1_end)
    elif int(range1_start) == int(range2_start):
        return (range1_end >= range2_end) or (range2_end >= range1_end)
    else:
        return int(range1_end) >= int(range2_end)

    return False

def ranges_overlap(range1, range2):
    range1_start, range1_end = range1.split("-")
    range1_numbers = []

    range2_start, range2_end = range2.split("-")
    range2_numbers = []

    if int(range1_start) > int(range2_start):
        return int(range1_start) <= int(range2_end)
    elif int(range1_start) == int(range2_start):
        return True
        #return (range1_end >= range2_end) or (range2_end >= range1_end)
    else:
        return int(range1_end) >= int(range2_start)

def part1():
    with open("inputs/day4/real.txt", "r") as problem_input:
        overlapping_ranges = 0
        for line in problem_input:
            assignment1, assignment2 = line.split(",")

            if ranges_completely_overlap(assignment1, assignment2):
                overlapping_ranges += 1
        return overlapping_ranges

def part2():
    with open("inputs/day4/real.txt", "r") as problem_input:
        overlapping_ranges = 0
        for line in problem_input:
            assignment1, assignment2 = line.split(",")

            if ranges_overlap(assignment1, assignment2):
                overlapping_ranges += 1

    return overlapping_ranges

print("part1: " + str(part1()))
print("part2: " + str(part2()))

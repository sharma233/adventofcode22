import re

crate_stacks = {}
instructions = []

def setup():
    with open("inputs/day5/real.txt", "r") as problem_input:
        for line in problem_input:
            line = line.replace("    ", " [X] ")
            for idx, crate in enumerate(re.split(r'(\s+)', line)):
                if re.match(r'\[[A-Z]\]', crate) and crate != "[X]":
                    key = int(idx/2 + 1)
                    if crate_stacks.get(key):
                        crate_stacks.get(key).append(crate)
                    else:
                        crate_stacks[key] = [crate]
            if re.match(r'move [0-9]+ from [0-9]+ to [0-9]+', line):
                instructions.append(re.findall('[0-9]+', line))

def part1():
    for instruction in instructions:
        amount = int(instruction[0])
        from_key = int(instruction[1])
        to_key = int(instruction[2])

        for _ in range(0, amount):
            crate = crate_stacks[from_key].pop(0)
            crate_stacks[to_key].insert(0, crate)

    top_crates = ""
    for i in range(1, len(crate_stacks) + 1):
        top_crates += crate_stacks[i][0]

    print(top_crates)

def part2():
    for instruction in instructions:
        amount = int(instruction[0])
        from_key = int(instruction[1])
        to_key = int(instruction[2])

        crate_stacks[to_key][:0] = crate_stacks[from_key][:amount]
        crate_stacks[from_key] = crate_stacks[from_key][amount:]

    top_crates = ""
    for i in range(1, len(crate_stacks) + 1):
        top_crates += crate_stacks[i][0]

    print(top_crates)

setup()
part1()
part2()
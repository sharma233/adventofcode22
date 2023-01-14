import math

H = {"pos_x": 0, "pos_y": 0}
T = {"pos_x": 0, "pos_y": 0}

#part 2 -- rope[0] is head
rope = []
for i in range(0,10):
    rope.append({"pos_x": 11, "pos_y": 15})

def calculate_distance(head, tail):
    return math.sqrt(pow((head["pos_x"] - tail["pos_x"]), 2) + pow((head["pos_y"] - tail["pos_y"]),2))

def move_h(instruction_dir, head):
    if instruction_dir == "L":
        head["pos_x"] -= 1
    if instruction_dir == "R":
        head["pos_x"] += 1
    if instruction_dir == "U":
        head["pos_y"] += 1
    if instruction_dir == "D":
        head["pos_y"] -= 1

def move_t(head, tail):
    distance = round(calculate_distance(head, tail),0)
    
    if(distance > 1):
        if head["pos_x"] > tail["pos_x"]:
            tail["pos_x"] += 1
        elif head["pos_x"] < tail["pos_x"]:
            tail["pos_x"] -= 1
        if head["pos_y"] > tail["pos_y"]:
            tail["pos_y"] += 1
        elif head["pos_y"] < tail["pos_y"]:
            tail["pos_y"] -= 1

#part2
def move_tails():
    for idx in range(1,len(rope)):
        move_t(rope[idx-1], rope[idx])


def part1():
    with open("inputs/day9/test.txt", "r") as problem_input:
        unique_t_positions = set()
        for line in problem_input:
            instruction = line.split()
            instruction_dir = instruction[0]
            instruction_magn = int(instruction[1])

            for _ in range(0, instruction_magn):
                move_h(instruction_dir, H)
                move_t(H, T)
                unique_t_positions.add((T["pos_x"], T["pos_y"]))
    return len(unique_t_positions)

def part2():
    with open("inputs/day9/real.txt", "r") as problem_input:
        unique_t_positions = set()
        for line in problem_input:
            instruction = line.split()
            instruction_dir = instruction[0]
            instruction_magn = int(instruction[1])

            for _ in range(0, instruction_magn):
                move_h(instruction_dir, rope[0])
                move_tails()
                unique_t_positions.add((rope[9]["pos_x"], rope[9]["pos_y"]))

    return len(unique_t_positions)
    
print("PART 1:")
print(part1())

print("PART 2:")
print(part2())
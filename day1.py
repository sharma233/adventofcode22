elf_list = []
with open("inputs/day1/real.txt", "r") as problem_input:
    current_total = 0
    for current_line in problem_input:
        if current_line != "\n":
            current_total = current_total + int(current_line)
        else:
            elf_list.append(current_total)
            current_total = 0

elf_list.append(current_total)
elf_list.sort()
#part 1
print(elf_list[-1])

#part2
print(elf_list[-1] + elf_list[-2] + elf_list[-3])

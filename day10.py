class CPU:
    cycle = 0
    current_instruction_cycles = 0
    instructions = []
    CRT = []
    done = True
    X = 1

    def set_instruction(self, instruction):
        self.current_instruction = instruction
        self.done = False

    _current_instruction = property(None, set_instruction)

    def draw(self):
        draw_idx = 0
        if((self.cycle) % 40 == 0):
            draw_idx = 0
        else:
            draw_idx = len(self.CRT[-1])
        
        char_to_draw = "."
        if(draw_idx == self.X or draw_idx == self.X-1 or draw_idx == self.X+1):
            char_to_draw = "#"
        
        if(draw_idx == 0):
            self.CRT.append(char_to_draw)
        else:
            self.CRT[-1] += char_to_draw

    def tick(self):
        instruction_parts = self.current_instruction.split()
        match instruction_parts[0]:
            case "noop":
                self.current_instruction_cycles = 0
                self.done = True
            case "addx":
                if self.current_instruction_cycles == 2:
                    self.X += int(instruction_parts[1])
                    self.current_instruction_cycles = 0
                    self.done = True
        self.draw()
        self.current_instruction_cycles += 1
        self.cycle += 1

def part1():
    cpu = CPU()
    with open("inputs/day10/real.txt", "r") as problem_input:
        total = 0
        for line in problem_input:
            cpu.set_instruction(line)
            while(cpu.done != True):
                if(cpu.cycle == 20 or (cpu.cycle % 40 == 20 and cpu.cycle <= 220)):
                    total += (cpu.cycle * cpu.X)
                cpu.tick()
    print(total)
    for row in cpu.CRT:
        print(row)

part1()
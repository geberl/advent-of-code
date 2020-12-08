import copy

instructions = dict()


class Instruction(object):
    def __init__(self, command, arg):
        self.command = command
        self.arg = arg
        self.hit = False


with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        items = line.strip().split(" ")
        instructions[n] = Instruction(items[0], int(items[1]))


def is_endless_loop(ins):
    accumulator = 0
    counter = 0

    while True:
        try:
            instruction = ins[counter]
        except Exception:
            return False, accumulator

        if instruction.hit:
            return True, accumulator
        ins[counter].hit = True

        if instruction.command == "nop":
            counter += 1
        elif instruction.command == "acc":
            accumulator += instruction.arg
            counter += 1
        elif instruction.command == "jmp":
            counter += instruction.arg


for n in range(len(instructions)):
    altered = copy.deepcopy(instructions)
    if altered[n].command == "acc":
        continue
    if altered[n].command == "nop":
        altered[n].command = "jmp"
    if altered[n].command == "jmp":
        altered[n].command = "nop"

    endless, value = is_endless_loop(altered)
    if not endless:
        print(value)
        break

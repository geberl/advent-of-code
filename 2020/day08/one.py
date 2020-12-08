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


accumulator = 0
counter = 0

while True:
    instruction = instructions[counter]

    if instruction.hit:
        print(accumulator)
        break
    instructions[counter].hit = True

    if instruction.command == "nop":
        counter += 1
    elif instruction.command == "acc":
        accumulator += instruction.arg
        counter += 1
    elif instruction.command == "jmp":
        counter += instruction.arg

tree_count = 0

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        if n == 0:
            continue
        if len(line.strip()) == 0:
            continue

        charPos = n*3
        if charPos > len(line.strip()):
            multiples = int(charPos / len(line.strip()))
            charPos = charPos - (multiples * len(line.strip()))

        char = line[charPos]

        if char == "#":
            tree_count += 1

print(tree_count)

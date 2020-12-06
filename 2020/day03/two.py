rightDowns = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

tree_counts = [0, 0, 0, 0, 0]

for e, rightDown in enumerate(rightDowns):
    with open("input.txt") as file_handler:
        processedLines = 1
        for n, line in enumerate(file_handler):
            if n == 0:
                continue
            if len(line.strip()) == 0:
                continue
            if n % rightDown[1] > 0:
                continue

            charPos = processedLines*rightDown[0]
            if charPos >= len(line.strip()):
                multiples = int(charPos / len(line.strip()))
                charPos = charPos - (multiples * len(line.strip()))

            char = line[charPos]

            if char == "#":
                tree_counts[e] += 1

            processedLines += 1

print(tree_counts)

multiplied = 1
for count in tree_counts:
    multiplied = multiplied * count
print(multiplied)

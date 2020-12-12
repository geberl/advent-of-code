data = []

with open("input.txt") as file_handler:
    for line in file_handler:
        data.append(line.strip())

angle = 0
pos = [0, 0]  # N/S , W/E

for d in data:
    instr = d[0]
    param = int(d[1:])

    if instr == "N":
        pos[0] = pos[0] + param
    elif instr == "S":
        pos[0] = pos[0] - param
    elif instr == "E":
        pos[1] = pos[1] + param
    elif instr == "W":
        pos[1] = pos[1] - param
    elif instr == "L":
        angle = angle - param
        if angle < 0:
            angle = angle + 360
    elif instr == "R":
        angle = angle + param
        if angle >= 360:
            angle = angle - 360
    elif instr == "F":
        if angle == 0:
            pos[1] = pos[1] + param
        elif angle == 90:
            pos[0] = pos[0] - param
        elif angle == 180:
            pos[1] = pos[1] - param
        elif angle == 270:
            pos[0] = pos[0] + param
        else:
            print("error")

print(pos)
print(abs(pos[0]) + abs(pos[1]))

import copy

data = []

with open("input.txt") as file_handler:
    for line in file_handler:
        data.append(line.strip())

ship_abs_pos = [0, 0]  # N/S , W/E
wayp_rel_pos = [1, 10]


for d in data:
    instr = d[0]
    param = int(d[1:])

    if instr == "N":
        wayp_rel_pos[0] = wayp_rel_pos[0] + param
    elif instr == "S":
        wayp_rel_pos[0] = wayp_rel_pos[0] - param
    elif instr == "E":
        wayp_rel_pos[1] = wayp_rel_pos[1] + param
    elif instr == "W":
        wayp_rel_pos[1] = wayp_rel_pos[1] - param
    elif instr == "L":
        old_wayp_rel_pos = copy.deepcopy(wayp_rel_pos)
        if param == 90:
            wayp_rel_pos[0] = old_wayp_rel_pos[1] * 1
            wayp_rel_pos[1] = old_wayp_rel_pos[0] * -1
        elif param == 180:
            wayp_rel_pos[0] = old_wayp_rel_pos[0] * -1
            wayp_rel_pos[1] = old_wayp_rel_pos[1] * -1
        elif param == 270:
            wayp_rel_pos[0] = old_wayp_rel_pos[1] * -1
            wayp_rel_pos[1] = old_wayp_rel_pos[0] * 1
        else:
            print("error")
    elif instr == "R":
        old_wayp_rel_pos = copy.deepcopy(wayp_rel_pos)
        if param == 90:
            wayp_rel_pos[0] = old_wayp_rel_pos[1] * -1
            wayp_rel_pos[1] = old_wayp_rel_pos[0] * 1
        elif param == 180:
            wayp_rel_pos[0] = old_wayp_rel_pos[0] * -1
            wayp_rel_pos[1] = old_wayp_rel_pos[1] * -1
        elif param == 270:
            wayp_rel_pos[0] = old_wayp_rel_pos[1] * 1
            wayp_rel_pos[1] = old_wayp_rel_pos[0] * -1
        else:
            print("error")
    elif instr == "F":
        ship_abs_pos[0] = ship_abs_pos[0] + param * wayp_rel_pos[0]
        ship_abs_pos[1] = ship_abs_pos[1] + param * wayp_rel_pos[1]


print(ship_abs_pos)
print(abs(ship_abs_pos[0]) + abs(ship_abs_pos[1]))

# 8266 too low

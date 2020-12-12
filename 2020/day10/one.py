data = []

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        data.append(int(line.strip()))

data.sort()

one_counter = 0
three_counter = 0

previous = 0
for n, d in enumerate(data):
    if previous + 1 == d:
        one_counter += 1
    elif previous + 2 == d:
        pass
    elif previous + 3 == d:
        three_counter += 1
    else:
        print("error")
        break
    previous = d

device_max = max(data) + 3
if previous + 1 == device_max:
    one_counter += 1
elif previous + 2 == device_max:
    pass
elif previous + 3 == device_max:
    three_counter += 1
else:
    print("error")

print(one_counter * three_counter)

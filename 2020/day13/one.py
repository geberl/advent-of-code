current_timestamp = 0
busses = []

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        if n == 0:
            current_timestamp = int(line.strip())
        if n == 1:
            for i in line.strip().split(","):
                if i != "x":
                    busses.append(int(i))

print(current_timestamp)
print(busses)

leave_timestamps = []

for bus in busses:
    multiplier = 2
    while True:
        next_departure = bus * multiplier
        if next_departure >= current_timestamp:
            leave_timestamps.append(next_departure)
            break
        multiplier += 1

for n, bus in enumerate(busses):
    print("bus id %d -> next at %d" % (bus, leave_timestamps[n]))

next_timestamp = min(leave_timestamps)
print(next_timestamp)
next_timestamp_index = leave_timestamps.index(next_timestamp)
print(next_timestamp_index)
selected_bus = busses[next_timestamp_index]
print(selected_bus)

solution = (selected_bus * (next_timestamp - current_timestamp))
print(solution)

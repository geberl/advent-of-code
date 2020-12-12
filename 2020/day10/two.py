data = []

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        data.append(int(line.strip()))

data.sort()

one_counter = 0
three_counter = 0

needs_three = []

previous = 0
for n, d in enumerate(data):
    if previous + 1 == d:
        one_counter += 1
    elif previous + 2 == d:
        pass
    elif previous + 3 == d:
        three_counter += 1
        needs_three.append([previous, d])
    else:
        print("error")
        break
    previous = d

device = max(data) + 3

if previous + 1 == device:
    one_counter += 1
elif previous + 2 == device:
    pass
elif previous + 3 == device:
    three_counter += 1
else:
    print("error")


def find_available(s, e):
    results = []
    if s == e:
        return results
    for item in data:
        if item <= s:
            continue
        if item >= e:
            break
        results.append(item)
    return results


def find_ways(s, e):
    # TODO very ugly solution, basically a lookup table for combinatorics calculated by hand
    available = find_available(s, e)
    delta = e - s

    if delta == 0:
        return 1
    elif delta == 1:
        return 1
    elif delta == 2:
        if len(available) == 0:
            return 1
        elif len(available) == 1:
            return 2
        else:
            raise("unhandled delta 2", available)
    elif delta == 3:
        if len(available) == 0:
            return 1
        elif len(available) == 1:
            return 2
        elif len(available) == 2:
            return 4
        else:
            raise("unhandled delta 3", available)
    elif delta == 4:
        if len(available) == 3:
            return 7
        else:
            raise("unhandled delta 4", available)
    elif delta == 5:
        if len(available) == 2:
            return 2
        else:
            raise("unhandled delta 5", available)
    elif delta == 7:
        if len(available) == 4:
            return 7
        else:
            raise("unhandled delta 7", available)
    else:
        print s, e, delta, available
        raise


needs_three.append((device, device))

end_result = 1
previous_segment_end = 0
for n, segment in enumerate(needs_three):
    start = previous_segment_end
    end = segment[0]
    x = find_ways(start, end)
    end_result = x * end_result
    previous_segment_end = segment[1]

print(end_result)

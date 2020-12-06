seat_ids = []


def binary_partition(start, end, identifier, lower_id, upper_id):
    if start == end:
        return start

    half_range = int((end - start + 1) / 2)

    if identifier[0] == lower_id:
        new_start = start
        new_end = end - half_range
    elif identifier[0] == upper_id:
        new_start = start + half_range
        new_end = end
    else:
        print("error")
        return

    return binary_partition(new_start, new_end, identifier[1:], lower_id, upper_id)


with open("input.txt") as file_handler:
    for line in file_handler:
        row = binary_partition(0, 127, line.strip()[:7], "F", "B")
        col = binary_partition(0, 7, line.strip()[7:], "L", "R")
        seat_id = row * 8 + col
        seat_ids.append(seat_id)


previous_seat_id = min(seat_ids) - 1
for seat_id in sorted(seat_ids):
    if previous_seat_id + 1 != seat_id:
        print(previous_seat_id + 1)
        break
    previous_seat_id = seat_id

busses = dict()

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        if n == 0:
            pass
        if n == 1:
            for m, i in enumerate(line.strip().split(",")):
                if i != "x":
                    busses[int(i)] = m


def get_bus_and_off(position):
    nth_bus_and_off = sorted(busses.items())[position-1]
    nth_bus = nth_bus_and_off[0]
    nth_off = nth_bus_and_off[1]
    return nth_bus, nth_off


def is_match(departure_timestamp, absolute_offset, position, iteration):
    if position < 0:
        return True

    prev_bus_id, prev_off = get_bus_and_off(position - 1)
    previous_departure = absolute_offset + prev_off

    if previous_departure % prev_bus_id == 0:
        return is_match(departure_timestamp, absolute_offset, position - 1, iteration + 1)
    return False


def match_bus_and_previous(position):
    this_bus_id, this_off = get_bus_and_off(position)

    multiplier = 100000000000000 / this_bus_id  # 937, meaning start at 106723585912

    while True:
        this_departure = multiplier * this_bus_id
        bus_one_departure = this_departure - this_off

        if is_match(this_departure, bus_one_departure, position, 0):
            return bus_one_departure

        if multiplier % 10000000 == 0:
            print(this_departure)
        multiplier += 1


res = match_bus_and_previous(len(busses))
print(res)  # 756261495958122
# TODO can't recommend, takes days to run on multiple cores

TARGET = 776203571

data = []

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        data.append(int(line.strip()))


def contiguous_sum(index):
    c_sum = 0
    for i in range(index, len(data)):
        c_sum += data[i]
        if c_sum == TARGET:
            return True, i
        elif c_sum < TARGET:
            pass
        elif c_sum > TARGET:
            return False, i


for start_index in range(len(data)):
    match, end_index = contiguous_sum(start_index)
    if match:
        print("match %d - %d" % (start_index, end_index))
        result_range = data[start_index:end_index+1]
        print(min(result_range) + max(result_range))
        break

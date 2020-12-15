# data = [0, 3, 6]
data = [1, 12, 0, 20, 8, 16]

count = 0
while True:
    if count >= 2020:
        break

    if count < len(data):
        print(count, data[count])
    else:
        last_number = data[count - 1]
        number_already_present = data.count(last_number) - 1
        if number_already_present == 0:
            print(count, number_already_present)
            data.append(number_already_present)
        else:
            difference = 0
            for i, e in enumerate(reversed(data)):
                if i == 0:
                    continue
                if e == last_number:
                    difference = i
                    break
            print(count, difference)
            data.append(difference)
    count += 1

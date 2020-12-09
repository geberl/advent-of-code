PREAMBLE_LENGTH = 25

preamble = []
data = []

with open("input.txt") as file_handler:
    for n, line in enumerate(file_handler):
        if n < PREAMBLE_LENGTH:
            preamble.append(int(line.strip()))
        else:
            data.append(int(line.strip()))

for d in data:
    found = False

    for n in preamble:
        if found:
            break

        for m in preamble:
            if d == n + m:
                # print("%d = %d + %d" % (d, n, m))
                found = True
                break

    if found:
        del(preamble[0])
        preamble.append(d)
    else:
        print("not found: %d" % d)
        break

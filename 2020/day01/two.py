numbers = []

with open("input.txt") as file_handler:
    for line in file_handler:
        numbers.append(line.strip())

found = False
for n in numbers:
    if found:
        break

    for m in numbers:
        if found:
            break

        for o in numbers:
            if int(n) + int(m) + int(o) == 2020:
                print("found: n=%s m=%s o=%s" % (n, m, o))
                print("multiplied: %d" % (int(n) * int(m) * int(o)))
                found = True
                break

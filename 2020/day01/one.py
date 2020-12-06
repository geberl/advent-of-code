numbers = []

with open("input.txt") as file_handler:
    for line in file_handler:
        numbers.append(line.strip())

found = False
for n in numbers:
    if found:
        break

    for m in numbers:
        if int(n) + int(m) == 2020:
            print("found: n=%s m=%s" % (n, m))
            print("multiplied: %d" % int(n)*int(m))
            found = True
            break

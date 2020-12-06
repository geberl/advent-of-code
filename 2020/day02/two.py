valid_passwords = 0

with open("input.txt") as file_handler:
    for line in file_handler:
        segments = line.strip().split(" ")

        firstSecondPod = segments[0]
        firstPos = int(firstSecondPod.split("-")[0])
        secondPos = int(firstSecondPod.split("-")[1])

        letter = segments[1].split(":")[0]

        password = segments[2]

        valid = False
        if password[firstPos - 1] == letter:
            if password[secondPos - 1] != letter:
                valid = True
                valid_passwords += 1
        else:
            if password[secondPos - 1] == letter:
                valid = True
                valid_passwords += 1

        print(firstPos, secondPos, letter, password, valid)

print(valid_passwords)

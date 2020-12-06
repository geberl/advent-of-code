valid_passwords = 0

with open("input.txt") as file_handler:
    for line in file_handler:
        segments = line.strip().split(" ")

        minMaxOccur = segments[0]
        minOccur = int(minMaxOccur.split("-")[0])
        maxOccur = int(minMaxOccur.split("-")[1])

        letter = segments[1].split(":")[0]

        password = segments[2]

        occur = password.count(letter)

        valid = False
        if (occur >= minOccur) and (occur <= maxOccur):
            valid = True
            valid_passwords += 1

        print(minOccur, maxOccur, letter, password, occur, valid)

print(valid_passwords)

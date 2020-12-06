group_answers = set()
sum_yes = 0

with open("input.txt") as file_handler:
    for line in file_handler:
        if len(line.strip()) == 0:
            sum_yes += len(group_answers)
            group_answers = set()

        for char in line.strip():
            group_answers.add(char)

    sum_yes += len(group_answers)

print(sum_yes)

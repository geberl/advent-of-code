def get_group_answers(ga):
    if len(ga) == 0:
        return 0
    elif len(ga) == 1:
        return len(ga[0])
    else:
        return len(ga[0].intersection(*ga[1:]))


group_answers = []
sum_yes = 0

with open("input.txt") as file_handler:
    for line in file_handler:
        if len(line.strip()) == 0:
            sum_yes += get_group_answers(group_answers)
            group_answers = []

        person_answers = set()
        for char in line.strip():
            person_answers.add(char)
        if len(person_answers) > 0:
            group_answers.append(person_answers)

    sum_yes += get_group_answers(group_answers)

print(sum_yes)

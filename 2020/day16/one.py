validators = {
    "departure location": [[45, 609], [616, 954]],
    "departure station": [[32, 194], [211, 972]],
    "departure platform": [[35, 732], [744, 970]],
    "departure track": [[40, 626], [651, 952]],
    "departure date": [[44, 170], [184, 962]],
    "departure time": [[49, 528], [538, 954]],
    "arrival location": [[36, 448], [464, 956]],
    "arrival station": [[48, 356], [373, 972]],
    "arrival platform": [[25, 118], [132, 954]],
    "arrival track": [[43, 703], [719, 965]],
    "class": [[29, 822], [828, 961]],
    "duration": [[25, 131], [151, 967]],
    "price": [[44, 784], [794, 958]],
    "route": [[25, 498], [511, 951]],
    "row": [[44, 905], [916, 973]],
    "seat": [[26, 756], [777, 960]],
    "train": [[36, 803], [819, 954]],
    "type": [[33, 318], [335, 967]],
    "wagon": [[46, 558], [570, 969]],
    "zone": [[47, 249], [265, 972]],
}

other_tickets = []

with open("tickets.txt") as file_handler:
    for line in file_handler:
        other_tickets.append([int(n) for n in line.strip().split(",")])

invalid_ticket_indexes = set()

error_scanning_rate = 0
for n, other_ticket in enumerate(other_tickets):
    for number in other_ticket:
        valid_in_terms_of = []
        for validator_name, validator_ranges in validators.items():
            valid = False
            for validator_range in validator_ranges:
                if number in range(validator_range[0], validator_range[1] + 1):
                    valid = True
                    break

            if valid:
                valid_in_terms_of.append(validator_name)

        if len(valid_in_terms_of) == 0:
            invalid_ticket_indexes.add(n)
            error_scanning_rate += number

print(len(invalid_ticket_indexes))
print(error_scanning_rate)

with open("valid_tickets.txt", "w") as file_handler:
    for n, other_ticket in enumerate(other_tickets):
        if n not in invalid_ticket_indexes:
            as_string = []
            for i in other_ticket:
                as_string.append(str(i))

            file_handler.write(",".join(as_string) + "\n")

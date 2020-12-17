validators = {
    # "departure location": [[45, 609], [616, 954]],  # 3
    # "departure station": [[32, 194], [211, 972]],  # 11
    # "departure platform": [[35, 732], [744, 970]],  # 18
    # "departure track": [[40, 626], [651, 952]],  # 12
    # "departure date": [[44, 170], [184, 962]],  # 13
    # "departure time": [[49, 528], [538, 954]],  # 6
    # "arrival location": [[36, 448], [464, 956]],  # 19
    # "arrival station": [[48, 356], [373, 972]],  # 17
    # "arrival platform": [[25, 118], [132, 954]],  # 10
    # "arrival track": [[43, 703], [719, 965]],  # 15
    "class": [[29, 822], [828, 961]],  # 2
    # "duration": [[25, 131], [151, 967]],  # 5
    # "price": [[44, 784], [794, 958]], 1
    # "route": [[25, 498], [511, 951]],  # 7
    # "row": [[44, 905], [916, 973]],  # 14
    # "seat": [[26, 756], [777, 960]],  # 8
    # "train": [[36, 803], [819, 954]],  # 4
    # "type": [[33, 318], [335, 967]],  # 16
    # "wagon": [[46, 558], [570, 969]],  # 9
    # "zone": [[47, 249], [265, 972]],  # 1
}

my_ticket = [73, 167, 113, 61, 89, 59, 191, 103, 67, 83, 163, 109, 101, 71, 97, 151, 107, 79, 157, 53]

other_tickets = []

with open("valid_tickets.txt") as file_handler:
    for line in file_handler:
        other_tickets.append([int(n) for n in line.strip().split(",")])

fields = dict()
for other_ticket in other_tickets:
    for field_number, field_value in enumerate(other_ticket):
        if field_number not in fields:
            fields[field_number] = {field_value}
        else:
            fields[field_number].add(field_value)

fields_sorted = dict()
for field_number, field_values in fields.items():
    fields_sorted[field_number] = sorted(list(field_values))

field_valids = dict()
for field_number, field_values in fields_sorted.items():
    # print(field_number, min(field_values), max(field_values))
    # print(field_values)

    field_is_valid_in_terms_of = []

    for validator_name, validator_ranges in validators.items():
        # print(" ", validator_name, validator_ranges)

        validator_is_valid_in_all_fields = True

        for field_value in field_values:
            field_value_in_at_least_one_range = False
            for validator_range in validator_ranges:
                if field_value in range(validator_range[0], validator_range[1] + 1):
                    field_value_in_at_least_one_range = True
                    break

            if not field_value_in_at_least_one_range:
                validator_is_valid_in_all_fields = False

        if validator_is_valid_in_all_fields:
            field_is_valid_in_terms_of.append(validator_name)

    field_valids[field_number] = field_is_valid_in_terms_of

for field_number, field_valid in field_valids.items():
    print(field_number, len(field_valid), field_valid)

# TODO make manual elimination method automatical
# Solved by run, comment out item with just one match, run again ...

result = 1
for i in [3, 11, 18, 12, 13, 6]:
    result = result * my_ticket[i]
print(result)

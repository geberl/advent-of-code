import copy
import itertools

rules = dict()
fully_resolved = []

with open("rules_sample.txt") as file_handler:
    for line in file_handler:
        rule = line.strip().split(":")
        key = int(rule[0])

        values = rule[1].strip().split(" ")
        if "|" in values:
            sub_vals = [[]]
            pipe_index = values.index("|")
            for n, value in enumerate(values):
                if n == pipe_index:
                    sub_vals.append([])
                    continue
                sub_vals[-1].append(int(value))
            rules[key] = sub_vals
        elif '"a"' in values:
            rules[key] = "a"
            fully_resolved.append(key)
        elif '"b"' in values:
            rules[key] = "b"
            fully_resolved.append(key)
        else:
            rules[key] = [[int(v) for v in values]]

print(rules)
print(fully_resolved)
print("---")

count = 0
while len(fully_resolved) < len(rules):
    working_rules = copy.deepcopy(rules)

    for key, segments in working_rules.items():
        if key in fully_resolved:
            continue

        all_segment_is_string = True
        for n, segment in enumerate(segments):
            if isinstance(segment, str):
                continue
            else:
                all_segment_is_string = False
                break
        if all_segment_is_string:
            fully_resolved.append(key)
            continue

        for n, segment in enumerate(segments):
            all_items_are_string = True
            for m, item in enumerate(segment):
                if isinstance(item, str):
                    continue
                else:
                    all_items_are_string = False
                    break

            if all_items_are_string:
                rules[key][n] = "".join(segment)
                continue

            for m, item in enumerate(segment):
                if isinstance(item, str):
                    continue

                if isinstance(item, list):
                    all_items_are_string = True
                    for sub_item in item:
                        if isinstance(sub_item, str):
                            all_items_are_string = False
                            break

                    if all_items_are_string:
                        combinations

                    print("foo", item)

                if item in fully_resolved:
                    resolved_segments = rules[item]
                    if len(resolved_segments) > 1:
                        print(item, resolved_segments)
                        # TODO
                        #    combinations = [p for p in itertools.combinations(*resolved_segments)]
                        #    print(combinations)
                        #    continue

                    rules[key][n][m] = rules[item]

    count += 1
    print("after %d" % count, rules)
    if count > 5:
        break

print("---")
print(rules)
print(sorted(fully_resolved))

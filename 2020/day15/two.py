results = {
    1: [1, None],
    12: [2, None],
    0: [3, None],
    20: [4, None],
    8: [5, None],
    16: [6, None],
}

count = len(results)
last_number = 16
spoken_first = True

while True:
    if count >= 30000000:
        break

    seen_at_before = results[last_number][1]
    if seen_at_before is None:
        results[0] = [count + 1, results[0][0]]
        last_number = 0
    else:
        seen_at = results[last_number][0]
        difference = seen_at - seen_at_before
        if difference in results:
            results[difference] = [count + 1, results[difference][0]]
        else:
            results[difference] = [count + 1, None]
        last_number = difference

    count += 1

print(last_number)

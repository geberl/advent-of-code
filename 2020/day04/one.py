totalValid = 0

with open("input.txt") as file_handler:
    results = dict()

    for n, line in enumerate(file_handler):
        if len(line.strip()) == 0:

            if "byr" in results:
                if "iyr" in results:
                    if "eyr" in results:
                        if "hgt" in results:
                            if "hcl" in results:
                                if "ecl" in results:
                                    if "pid" in results:
                                        totalValid += 1

            results.clear()
            continue

        keyVals = line.strip().split(" ")
        for keyVal in keyVals:
            key = keyVal.split(":")[0]
            val = keyVal.split(":")[1]
            results[key] = val

print(totalValid)

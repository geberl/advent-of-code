def valid_byr(value):
    if len(value) != 4:
        return False
    if not value.isdigit():
        return False
    if int(value) < 1920:
        return False
    if int(value) > 2002:
        return False
    return True


def valid_iyr(value):
    if len(value) != 4:
        return False
    if not value.isdigit():
        return False
    if int(value) < 2010:
        return False
    if int(value) > 2020:
        return False
    return True


def valid_eyr(value):
    if len(value) != 4:
        return False
    if not value.isdigit():
        return False
    if int(value) < 2020:
        return False
    if int(value) > 2030:
        return False
    return True


def valid_hgt(value):
    if value.endswith("cm"):
        cm_value = value.split("cm")[0]
        if not cm_value.isdigit():
            return False
        if (int(cm_value) >= 150) and (int(cm_value) <= 193):
            return True
        return False

    if value.endswith("in"):
        in_value = value.split("in")[0]
        if not in_value.isdigit():
            return False
        if (int(in_value) >= 59) and (int(in_value) <= 76):
            return True
        return False

    return False


def valid_hcl(value):
    if not value.startswith("#"):
        return False
    if len(value[1:]) != 6:
        return False
    for char in value[1:]:
        if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
            return False
    return True


def valid_ecl(value):
    if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return True


def valid_pid(value):
    if len(value) != 9:
        return False
    if not value.isdigit():
        return False
    return True


totalValid = 0

with open("input.txt") as file_handler:
    results = dict()

    for n, line in enumerate(file_handler):
        if len(line.strip()) == 0:

            if "byr" in results and valid_byr(results["byr"]):
                if "iyr" in results and valid_iyr(results["iyr"]):
                    if "eyr" in results and valid_eyr(results["eyr"]):
                        if "hgt" in results and valid_hgt(results["hgt"]):
                            if "hcl" in results and valid_hcl(results["hcl"]):
                                if "ecl" in results and valid_ecl(results["ecl"]):
                                    if "pid" in results and valid_pid(results["pid"]):
                                        totalValid += 1

            results.clear()
            continue

        keyVals = line.strip().split(" ")
        for keyVal in keyVals:
            key = keyVal.split(":")[0]
            val = keyVal.split(":")[1]
            results[key] = val

print(totalValid)

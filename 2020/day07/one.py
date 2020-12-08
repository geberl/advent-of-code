results = set()


def parse_file():
    with open("input.txt") as file_handler:
        new_options = set()
        for line in file_handler:
            if line.strip().startswith("shiny gold "):
                continue

            if "shiny gold" in line.strip():
                words = line.strip().split(" ")
                key = "%s %s" % (words[0], words[1])
                results.add(key)

            for result in results:
                if result in line.strip():
                    words = line.strip().split(" ")
                    key = "%s %s" % (words[0], words[1])
                    new_options.add(key)

        results.update(new_options)


before_result_len = len(results)
while True:
    parse_file()
    now_result_len = len(results)
    if before_result_len == now_result_len:
        break
    else:
        before_result_len = now_result_len

print(len(results))

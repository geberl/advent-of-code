results = dict()


def get_contents(string):
    contents = dict()
    words = string.split(" ")
    for n, word in enumerate(words):
        if word.isdigit():
            key = "%s %s" % (words[n+1], words[n+2])
            contents[key] = int(word)

    return contents


def parse_file():
    with open("input.txt") as file_handler:
        for line in file_handler:
            words = line.strip().split(" ")
            key = "%s %s" % (words[0], words[1])
            results[key] = get_contents(line.strip())


def sum_bags(start_color):
    bags = 1

    contents = results[start_color]
    for cont_color, cont_num in contents.iteritems():
        sub_bags = sum_bags(cont_color)
        bags += sub_bags * cont_num

    return bags


parse_file()
num = sum_bags("shiny gold")
print(num-1)

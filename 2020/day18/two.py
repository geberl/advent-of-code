expressions = []

with open("input.txt") as file_handler:
    for line in file_handler:
        expressions.append(line.strip())


def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    Source: https://scipython.com/blog/parenthesis-matching-in-python/
    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs


def resolve_additions(s):
    expr_split = s.split(" ")
    plus_indexes = []
    for m, item in enumerate(expr_split):
        if item == "+":
            plus_indexes.append(m)

    while len(plus_indexes) > 0:
        for plus_index in plus_indexes:
            summand_one_index = plus_index - 1
            summand_two_index = plus_index + 1
            sum_expr = expr_split[summand_one_index] + " + " + expr_split[summand_two_index]
            sum_res = solve(sum_expr)

            expr_split[summand_one_index] = str(sum_res)
            del (expr_split[plus_index])
            del (expr_split[plus_index])  # pos changes through previous del!
            break

        plus_indexes = []
        for m, item in enumerate(expr_split):
            if item == "+":
                plus_indexes.append(m)

    return " ".join(expr_split)


def solve(s):
    if "+" in s:
        if "*" in s:
            s = resolve_additions(s)

    expr_split = s.split(" ")

    while len(expr_split) >= 3:
        segment_to_evaluate = expr_split[0:3]
        segment_to_evaluate_str = " ".join(segment_to_evaluate)
        res_segment = eval(segment_to_evaluate_str)

        expr_split[0] = str(res_segment)
        del (expr_split[1])
        del (expr_split[1])  # pos changes through previous del!

    return " ".join(expr_split)


sum_expressions = 0

for n, expression in enumerate(expressions):
    print(n, " ->", expression)
    paras = find_parentheses(expression)

    while len(paras) > 0:
        paras_on_level = []

        for start, end in paras.items():
            inner = expression[start:end+1]
            without_start_end = inner[1:-1]

            if "(" in without_start_end:
                continue
            paras_on_level.append([start, end, without_start_end])

        for start, end, sub_expr in paras_on_level:
            sub_res = solve(sub_expr)
            expression_left = expression[0:start]
            expression_right = expression[end+1:]

            expression = expression_left + sub_res + expression_right
            break  # indexes are wrong after first replacement, start over

        paras = find_parentheses(expression)

    res = solve(expression)
    print("   ->", res)
    sum_expressions += int(res)

print(sum_expressions)

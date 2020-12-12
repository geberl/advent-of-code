import copy

data = dict()


class Seat:
    def __init__(self, row, col, empty=True):
        self.row = row
        self.col = col
        self.empty = empty

    def is_empty(self):
        return self.empty

    def occupy(self):
        self.empty = False

    def leave(self):
        self.empty = True

    def count_full_nearby(self, parent):
        if self.row == 0:
            start_row = 0
        else:
            start_row = self.row - 1

        if self.row < number_of_rows - 1:
            end_row = self.row + 1
        else:
            end_row = self.row

        if self.col > 0:
            start_col = self.col - 1
        else:
            start_col = self.col

        if self.col < number_of_cols:
            end_col = self.col + 1
        else:
            end_col = self.col

        count = 0

        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if j in parent[i]:
                    adj_seat = parent[i][j]
                    if not adj_seat.is_empty():
                        count += 1

        return count


number_of_cols = 0

with open("sample.txt") as file_handler:
    for n, line in enumerate(file_handler):
        if number_of_cols == 0:
            number_of_cols = len(line.strip())

        if n not in data:
            data[n] = dict()

        for m, char in enumerate(line.strip()):
            if char == "L":
                if m not in data[n]:
                    data[n][m] = dict()
                data[n][m] = Seat(n, m)

number_of_rows = len(data)


def run_sim(old_state):
    new_state = copy.deepcopy(old_state)

    for row_number, row_content in old_state.iteritems():
        for col_number, col_content in row_content.iteritems():
            if col_content.is_empty():
                if col_content.count_full_nearby(old_state) == 0:
                    new_state[row_number][col_number].occupy()
            else:
                if col_content.count_full_nearby(old_state) > 4:
                    new_state[row_number][col_number].leave()

    return new_state


def visualize(state):
    for _, row_content in state.iteritems():
        line_content = ""

        for col_num in range(0, number_of_cols):
            if col_num not in row_content:
                line_content += "."
            else:
                if row_content[col_num].is_empty():
                    line_content = line_content + "L"
                else:
                    line_content = line_content + "#"

        print(line_content)


def is_identical(s1, s2):
    for row_num, row_content in s1.iteritems():
        for col_num, col_content in row_content.iteritems():
            if col_content.empty != s2[row_num][col_num].empty:
                return False
    return True


def count_occupied(s):
    count = 0
    for row_num, row_content in s.iteritems():
        for col_num, col_content in row_content.iteritems():
            if not col_content.empty:
                count += 1
    return count


start_state = copy.deepcopy(data)

sim_count = 0
while True:
    new_state = run_sim(start_state)

    if is_identical(new_state, start_state):
        print("stable after", sim_count)
        break
    else:
        start_state = copy.deepcopy(new_state)
    sim_count += 1


visualize(new_state)
print(count_occupied(new_state))

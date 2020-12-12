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

    @classmethod
    def sees_left(cls, row, col, parent):
        if col == 0:
            return 0

        if col-1 not in parent[row]:
            return cls.sees_left(row, col-1, parent)
        elif parent[row][col-1].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_right(cls, row, col, parent):
        if col == number_of_cols - 1:
            return 0

        if col+1 not in parent[row]:
            return cls.sees_right(row, col+1, parent)
        elif parent[row][col+1].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_up(cls, row, col, parent):
        if row == 0:
            return 0

        if col not in parent[row-1]:
            return cls.sees_up(row-1, col, parent)
        elif parent[row-1][col].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_down(cls, row, col, parent):
        if row == number_of_rows - 1:
            return 0

        if col not in parent[row+1]:
            return cls.sees_down(row+1, col, parent)
        if parent[row+1][col].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_up_left(cls, row, col, parent):
        if (row == 0) or (col == 0):
            return 0

        if col-1 not in parent[row-1]:
            return cls.sees_up_left(row-1, col-1, parent)
        elif parent[row-1][col-1].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_up_right(cls, row, col, parent):
        if (row == 0) or (col == number_of_cols -1):
            return 0

        if col+1 not in parent[row-1]:
            return cls.sees_up_right(row - 1, col + 1, parent)
        elif parent[row-1][col+1].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_down_left(cls, row, col, parent):
        if (row == number_of_rows - 1) or (col == 0):
            return 0

        if col - 1 not in parent[row + 1]:
            return cls.sees_down_left(row + 1, col - 1, parent)
        elif parent[row + 1][col - 1].is_empty():
            return 0
        else:
            return 1

    @classmethod
    def sees_down_right(cls, row, col, parent):
        if (row == number_of_rows - 1) or (col == number_of_cols - 1):
            return 0

        if col + 1 not in parent[row + 1]:
            return cls.sees_down_right(row + 1, col + 1, parent)
        elif parent[row+1][col+1].is_empty():
            return 0
        else:
            return 1

    def count_full_nearby(self, parent):
        left = self.sees_left(self.row, self.col, parent)
        right = self.sees_right(self.row, self.col, parent)
        up = self.sees_up(self.row, self.col, parent)
        down = self.sees_down(self.row, self.col, parent)

        up_left = self.sees_up_left(self.row, self.col, parent)
        up_right = self.sees_up_right(self.row, self.col, parent)
        down_left = self.sees_down_left(self.row, self.col, parent)
        down_right = self.sees_down_right(self.row, self.col, parent)

        return left + right + up + down + up_left + up_right + down_left + down_right


number_of_cols = 0

with open("input.txt") as file_handler:
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
                if col_content.count_full_nearby(old_state) >= 5:
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

new_state = run_sim(start_state)

sim_count = 0
while True:
    new_state = run_sim(start_state)

    if is_identical(new_state, start_state):
        print("stable after", sim_count)
        break
    else:
        start_state = copy.deepcopy(new_state)
    sim_count += 1

print(count_occupied(new_state))

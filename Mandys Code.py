grid = []
gridline_length = 0
symbols = []
potential_parts_list = []
sum_of_valid_part_numbers = 0

class Potential_part:
    def __init__(self, value, row, index, length):
        self.value = value
        self.row = row
        self.index = index
        self.length = length

def validate_part(grid, part):
    validity = False
    if part.row == 0:
        row_start = 0
        row_end = 1
    elif part.row == (len(grid) - 1):
        row_start = -1
        row_end = 0
    else:
        row_start = -1
        row_end = 1

    if part.index == 0:
        index_start = 0
        index_end = index_start + part.length + 1
    elif part.index + part.length + 1 > gridline_length - 1:
        index_start = -1
        index_end = index_start + part.length + 1
    else:
        index_start = -1
        index_end = index_start + part.length + 2

    for r in range(row_start, (row_end +1)):
        # print(f"row iteration {r}")
        for item in range(index_start, (index_end)):
            # print(f"index iteration {item}")
            character = grid[part.row + r][part.index + item]
            # print(character)
            if character in symbols:
                print(character, part.value, part.row, part.index)
                validity = True
            else:
                # print("No adjacent symbols")
                pass
    return validity



with open ("puzzle_data_of_the_day.txt", encoding="UTF-8", mode="r") as file:
    reader = file.readlines()

    for line in range(len(reader)):
        # print(reader[line])
        row = []
        gridline_length = len(reader[line])
        for char in range(gridline_length):
            # print(reader[line][char])
            number = reader[line][char]
            row.append(number)
            if not (reader[line][char].isdigit() or reader[line][char] == '.' or reader[line][char] == '\n') and reader[line][char] not in symbols:
                symbols.append(reader[line][char])
            if reader[line][char].isdigit() and reader[line][char-1].isdigit() == False:
                current_length = 0
                number_as_string = ""
                while reader[line][char+current_length].isdigit():
                    number_as_string += reader[line][char+current_length]
                    current_length += 1
                # print(number_as_string)
                # print(number, current_length)
                part = Potential_part(int(number_as_string), line, char, current_length)
                # print(part.value)
                potential_parts_list.append(part)
        grid.append(row)

# print(gridline_length) = 140

for part in potential_parts_list:
    # print(f"Part is {part.value}; row is {part.row}, index is {part.index}")
    validity = validate_part(grid, part)
    if validity == True:
        # valid_parts_list.append(part)
        print(f"{part.value} on row {part.row} is a valid part")
        sum_of_valid_part_numbers += part.value

# print(f"{grid} this is the grid")
# print(len(grid))
print(sum_of_valid_part_numbers)


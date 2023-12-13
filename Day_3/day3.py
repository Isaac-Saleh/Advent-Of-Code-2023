with open("puzzle_input_day3.txt") as file:
    lines = file.readlines()


def look_for_symbols(si, ei, index):
    grid_row = grid[index]

    if 0 < index < len(grid) - 1 and (ei < len(grid_row)):
        adjacent_cells = [grid[index - 1][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index + 1][max(0, si - 1): min(ei + 2, len(grid_row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if not (cell.isdigit() or cell == '.'):
                    return True
    elif index == 0:
        adjacent_cells = [grid[index][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index + 1][max(0, si - 1): min(ei + 2, len(grid_row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if not (cell.isdigit() or cell == '.'):
                    return True
    elif index == len(grid) - 1:
        adjacent_cells = [grid[index - 1][max(0, si - 1): min(ei + 2, len(grid_row))],
                  grid[index][max(0, si - 1): min(ei + 2, len(grid_row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if not (cell.isdigit() or cell == '.'):
                    return True
    return False


""" Program initiates Below """

grid = []
for line in lines:
    row = line.strip()
    grid.append(row)


part_numbers = []
current_number = ''
for index, row in enumerate(grid):
    for i, item in enumerate(row):
        if item.isdigit():
            current_number += item
            end_index = i
            start_index = end_index - len(current_number) + 1
        elif current_number:
            validity = look_for_symbols(start_index, end_index, index)
            if validity:
                part_numbers.append(current_number)
                current_number = ''
            else:
                current_number = ''
    if current_number:
        validity = look_for_symbols(start_index, end_index, index)
        if validity:
            part_numbers.append(current_number)
            current_number = ''
        else:
            current_number = ''
ans = 0
for part_number in part_numbers:
    ans += int(part_number)

print(f"Answer to Part-1: {ans}")

""" PART 2 - DAY 3 - ADVENT OF CODE """

with open("puzzle_input_day3.txt") as file:
    lines = file.readlines()


def touches_star(start_index, end_index, index):
    grid_row = grid[index]
    si = start_index
    ei = end_index
    if 0 < index < len(grid) - 1 and (ei < len(grid_row)):
        adjacent_cells = [grid[index - 1][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index + 1][max(0, si - 1): min(ei + 2, len(grid_row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if cell == '*':
                    return True

    elif index == 0:
        adjacent_cells = [grid[index][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index + 1][max(0, si - 1): min(ei + 2, len(grid_row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if cell == '*':
                    return True
    elif index == len(grid) - 1:
        adjacent_cells = [grid[index - 1][max(0, si - 1): min(ei + 2, len(grid_row))],
                          grid[index][max(0, si - 1): min(ei + 2, len(grid_row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if cell == '*':
                    return True
    return False

def find_star(index, start_index, end_index, number):
    si = start_index
    ei = end_index
    if 0 < index < (len(grid) - 1) and (ei < len(grid[index])):
        adjacent_rows = grid[index - 1], grid[index], grid[index + 1]
        for r, row_cells in enumerate(adjacent_rows):
            for j, cell in enumerate(row_cells):
                if (cell == '*') and ((si - 1) <= j <= (ei + 1)):
                    key = ((index + r - 1), j)
                    if key in values:
                        values[key] *= int(number)
                        parts_to_sum.append(values[key])
                    else:
                        values[key] = int(number)
    elif index == 0:
        adjacent_rows = [grid[index], grid[index + 1]]
        for r, row_cells in enumerate(adjacent_rows):
            for j, cell in enumerate(row_cells):
                if (cell == '*') and ((si - 1) <= j <= (ei + 1)):
                    key = (r, j)
                    if key in values:
                        values[key] *= int(number)
                        parts_to_sum.append(values[key])
                    else:
                        values[key] = int(number)
    elif index == len(grid) - 1:
        adjacent_rows =  grid[index - 1], grid[index]
        for r, row_cells in enumerate(adjacent_rows):
            for j, cell in enumerate(row_cells):
                if (cell == '*') and ((si - 1) <= j <= (ei + 1)):
                    key = ((index + r - 1), j)
                    if key in values:
                        values[key] *= int(number)
                        parts_to_sum.append(values[key])
                    else:
                        values[key] = int(number)


""" Program initiates Below """

grid = []
for line in lines:
    row = line.strip()
    grid.append(row)

values = {}
parts_to_sum = []
current_number = ''
for index, row in enumerate(grid):
    for i, item in enumerate(row):
        if item.isdigit():
            current_number += item
            end_index = i
            start_index = end_index - len(current_number) + 1
        elif current_number:
            validity = touches_star(start_index, end_index, index)
            if validity:
                find_star(index, start_index, end_index, current_number)
                current_number = ''
            else:
                current_number = ''
    if current_number:
        validity = touches_star(start_index, end_index, index)
        if validity:
            find_star(index, start_index, end_index, current_number)
            current_number = ''
        else:
            current_number = ''


print(f"Answer to Part-2: {sum(parts_to_sum)}")

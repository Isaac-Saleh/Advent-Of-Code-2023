with open("puzzle_input_day3.txt") as file:
    lines = file.readlines()

def look_for_symbols(si, ei, index):
    row = grid[index]
    # for cell in row:
    if 0 < index < len(grid) - 1 and (ei < len(row)):
        adjacent_cells = [grid[index - 1][max(0, si - 1): min(ei + 2, len(row))],
                          grid[index][max(0, si - 1): min(ei + 2, len(row))],
                          grid[index + 1][max(0, si - 1): min(ei + 2, len(row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if not (cell.isdigit() or cell == '.'):
                    return True
    elif index == 0:
        adjacent_cells = [grid[index][max(0, si - 1): min(ei + 2, len(row))],
                          grid[index + 1][max(0, si - 1): min(ei + 2, len(row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if not (cell.isdigit() or cell == '.'):
                    return True
    elif index == len(grid) - 1:
        adjacent_cells = [grid[index - 1][max(0, si - 1): min(ei + 2, len(row))],
                  grid[index][max(0, si - 1): min(ei + 2, len(row))]]
        for row_cells in adjacent_cells:
            for cell in row_cells:
                if not (cell.isdigit() or cell == '.'):
                    return True

    return False

""" Program initates Below """

grid = []
for line in lines:
    row = list(line.strip())
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
ans = 0
for part_number in part_numbers:
    print(f"{part_number} to add")
    ans += int(part_number)
    print(f"{ans} = new total")


with open("puzzle_input_day3.txt", 'r') as file:
    lines = file.readlines()


def find_parts_in_gears(line):
    parts_in_gears = {}
    current_number = ""
    for i, char in enumerate(line):
            if char.isdigit():
                current_number += char
            elif current_number:
                if len(current_number) == 3:
                    key = i - 2
                    parts_in_gears[key] = current_number
                    current_number = ''
                if len(current_number) == 2:
                    key = i - 1
                    parts_in_gears[key] = current_number
                    current_number = ''
                if len(current_number) == 1:
                    key = i
                    parts_in_gears[key] = current_number
                    current_number = ''
    return parts_in_gears


def line_contains_symbol(line):
    symbol_in_gears = {}
    line_to_check = line.strip()
    for i,  char in enumerate(line_to_check):
        if not (char.isdigit() or char == '.'):
            key = i
            symbol_in_gears[key] = char

    return symbol_in_gears


def sort_to_compare_lines(lines):
    for line in lines:
        dict_parts = find_parts_in_gears(line)
        dict_symbols = line_contains_symbol(line)
        combined_dict = dict_parts | dict_symbols
        sorted_dict = sorted(combined_dict.items())
        print(sorted_dict)






# for line in lines:
#     dict_parts = find_parts_in_gears(line)
#     dict_symbols = line_contains_symbol(line)
#     combined_dict = dict_parts | dict_symbols
#     sorted_dict = sorted(combined_dict.items())
#     print(sorted_dict)



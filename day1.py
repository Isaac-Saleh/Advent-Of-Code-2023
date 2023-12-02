with open('puzzle_input.txt', 'r') as file:
    lines = file.readlines()


"""Part 1 Day 1 Advent of Code"""


def find_number_in_line(line):
    numbers_in_line = []
    for char in line:
        if char.isdigit():
            numbers_in_line.append(char)
    first = numbers_in_line[0]
    last = numbers_in_line[-1]
    line_value = first + last
    return int(line_value)


total_value = 0
for line in lines:
    value_in_line = find_number_in_line(line)
    total_value = total_value + value_in_line
print(total_value)

"""Part 2 Day 1 - Advent of Code"""


def find_number_words(array):
    string = ''.join(array)
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    found_numbers = {}
    for word in number_words:
        start_index = 0
        while word in string[start_index:]:
            key = string.index(word, start_index)
            found_numbers[key] = str(number_words.index(word) + 1)
            start_index = key + 1

    return found_numbers


def find_all_numbers_in_line(array):
    numbers_in_line = {}
    for i, char in enumerate(array):
        if char.isdigit():
            key = i
            numbers_in_line[key] = char
    return numbers_in_line


def get_first_and_last(array):
    first = array[0]
    last = array[-1]
    a_value = first + last
    actual_first = a_value[1]
    actual_last = a_value[-1]
    actual_value = actual_first + actual_last
    return actual_value


total_value = 0
for line in lines:
    dictionary_1 = find_number_words(line)
    dictionary_2 = find_all_numbers_in_line(line)
    if dictionary_1 is not None:
        combined_dictionary = dictionary_1 | dictionary_2
    else:
        combined_dictionary = dictionary_2
    sorted_dict = sorted(combined_dictionary.items())
    value = get_first_and_last(sorted_dict)
    total_value = total_value + int(value)

print(total_value)





















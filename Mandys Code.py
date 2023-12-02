import csv

# PART ONE
# calibration_values = []

# with open ("calibration.txt", encoding="UTF-8", mode="r") as file:
#     reader = file.readlines()

#     for line in reader:
#         line = line.strip()
#         digits_in_line = []
#         for char in range(0, len(line)):
#             if line[char].isdigit():
#                 digits_in_line.append(line[char])
#         value = digits_in_line[0] + digits_in_line[len(digits_in_line) - 1]
#         calibration_values.append(int(value))
#     print(sum(calibration_values))


# PART 2
sum_calibration_values = 0


def word_to_number(line, char):
    if char <= (len(line) - 5):
        if line[char] == "t" and line[char + 1] == "h" and line[char + 2] == "r" and line[char + 3] == "e" and line[
            char + 4] == "e":
            return "3"

        if line[char] == "s" and line[char + 1] == "e" and line[char + 2] == "v" and line[char + 3] == "e" and line[
            char + 4] == "n":
            return "7"

        if line[char] == "e" and line[char + 1] == "i" and line[char + 2] == "g" and line[char + 3] == "h" and line[
            char + 4] == "t":
            return "8"

    if char <= (len(line) - 4):
        if line[char] == "f":
            if line[char + 1] == "o" and line[char + 2] == "u" and line[char + 3] == "r":
                return "4"

            if line[char + 1] == "i" and line[char + 2] == "v" and line[char + 3] == "e":
                return "5"
        if line[char] == "n" and line[char + 1] == "i" and line[char + 2] == "n" and line[char + 3] == "e":
            return "9"

    if char <= (len(line) - 3):
        if line[char] == "o" and line[char + 1] == "n" and line[char + 2] == "e":
            return "1"
        if line[char] == "t" and line[char + 1] == "w" and line[char + 2] == "o":
            return "2"
        if line[char] == "s" and line[char + 1] == "i" and line[char + 2] == "x":
            return "6"
    else:
        return


with open("puzzle_input.txt", encoding="UTF-8", mode="r") as file:
    reader = file.readlines()

    for line in reader:
        # line = line.strip()
        digits_in_line = []

        for char in range(0, len(line)):
            if line[char].isdigit():
                digits_in_line.append(line[char])
            else:
                digit = word_to_number(line, char)
                if digit != None:
                    digits_in_line.append(digit)
        value = digits_in_line[0] + digits_in_line[len(digits_in_line) - 1]
        print(value)
        sum_calibration_values += (int(value))
        print(sum_calibration_values)

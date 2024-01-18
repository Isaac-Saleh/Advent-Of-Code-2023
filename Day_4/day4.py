with open("puzzle_input_day4.txt") as file:
    lines = file.readlines()

total = 0
for i, line in enumerate(lines):
    numbers = (line.split(':')[1])
    winning_numbers = sorted(map(int, numbers.split("|")[0].split()))
    your_numbers = sorted(map(int, numbers.split("|")[1].split()))

    matching_numbers = []
    for num in winning_numbers:
        if num in your_numbers:
            matching_numbers.append(num)
    points = 1
    for item in matching_numbers:
        points *= 2
    if not matching_numbers:
        points = 0
    card_point = (points / 2)
    total = total + card_point
print(total)






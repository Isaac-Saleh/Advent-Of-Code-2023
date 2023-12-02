with open ('puzzle_input_day2.txt') as file:
    lines = file.readlines()

""" PART 1 - Day 2 - ADVENT OF CODE """

MAX_RED = [12, 'red']
MAX_GREEN = [13, 'green']
MAX_BLUE = [14, 'blue']


valid_game_ids = []


for line in lines:
    red = []
    green = []
    blue = []
    game_array = []
    first_split = line.split(':')
    game_id = int(first_split[0].strip('Game '))
    game_array.append(game_id)
    game_data = first_split[1].strip()
    game_array.append(game_data)
    cubes = game_array[1]
    revealed_cubes = cubes.split(';')
    for element in revealed_cubes:
        hands = element.strip().split(", ")
        for item in hands:
            hand = item.split(" ")
            number= int(hand[0])
            colour = hand[1]
            if colour == MAX_RED[1]:
                red.append(number)
            if colour == MAX_GREEN[1]:
                green.append(number)
            if colour == MAX_BLUE[1]:
                blue.append(number)
    if max(red) > MAX_RED[0] or max(blue) > MAX_BLUE[0] or max(green) > MAX_GREEN[0]:
        pass
    else:
        valid_game_ids.append(game_id)
print(sum(valid_game_ids))


""" PART 2 - DAY 2 - ADVENT OF CODE """

sum_of_powers = 0

for line in lines:
    red = []
    green = []
    blue = []
    game_array = []
    first_split = line.split(':')
    game_id = int(first_split[0].strip('Game '))
    game_array.append(game_id)
    game_data = first_split[1].strip()
    game_array.append(game_data)
    cubes = game_array[1]
    revealed_cubes = cubes.split(';')
    for element in revealed_cubes:
        hands = element.strip().split(", ")
        for item in hands:
            hand = item.split(" ")
            number= int(hand[0])
            colour = hand[1]
            if colour == 'red':
                red.append(number)
            if colour == 'green':
                green.append(number)
            if colour == 'blue':
                blue.append(number)
    max_red_needed = max(red)
    max_green_needed = max(green)
    max_blue_needed = max(blue)
    power_of_game = max_blue_needed * max_green_needed * max_red_needed
    sum_of_powers += power_of_game

print(sum_of_powers)















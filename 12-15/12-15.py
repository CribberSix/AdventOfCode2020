def update_x_with(x, current_turn):
    global numbers
    try:
        last_spoken_at = numbers[x]
        temp = last_spoken_at[1]
        numbers[x] = [temp, current_turn]
    except KeyError:  # first time the number was being said
        numbers[x] = [-1, current_turn]


# ______ PART 1 ______
# numbers = {0: [-1, 1], 3: [-1, 2], 6: [-1, 3]}
# last_num = 6
# turn = 3

# ______ PART 2 ______
numbers = {14: [-1, 1], 1: [-1, 2], 17: [-1, 3], 0: [-1, 4], 3: [-1, 5], 20: [-1, 6]}
last_num = 20
turn = 6

while True:
    turn += 1
    # get last nums from dict

    last_spoken_at = numbers[last_num]
    if -1 in last_spoken_at:  # last_num occured only once
        update_x_with(0, turn)
        last_num = 0
    else:  # last_num occurred at least twice in the past
        ls = numbers[last_num]
        last_num = ls[1] - ls[0]
        update_x_with(last_num, turn)

    if turn % 1000000 == 0:
        print(f"Turn {turn} - {last_num}")

    if turn == 30000000:
        print(f"Turn {turn} - {last_num}")
        break

print("Finished!")

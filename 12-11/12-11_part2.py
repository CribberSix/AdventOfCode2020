import sys
seats = [s[:-1] for s in open('input.txt').readlines()]


def are_valid_indizes(map, c_tuple):
    return len(map[0]) - 1 >= c_tuple[0] >= 0 and 0 <= c_tuple[1] <= len(map) - 1


def check_direction(map, x, y, xd, yd):
    """
    Checks seats in one direction until we find a seat.
    """
    if not are_valid_indizes(map, (x + xd, y + yd)):
        return 0

    if map[y + yd][x + xd] == '.':
        return check_direction(map, x + xd, y + yd, xd, yd)
    elif map[y + yd][x + xd] == 'L':
        return 0
    elif map[y +yd][x + xd] == '#':
        return 1


def count_adjacent_part2(map, x, y):
    directions = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            directions.append((i, j))
    directions.remove((0,0))

    occupied = 0
    for d in directions:
        occupied += check_direction(map, x, y, d[0], d[1])
    return occupied


def fill_the_seats(map):
    new_layout = []
    for y, row in enumerate(map):
        new_row = ""
        for x, seat in enumerate(row):
            if seat == 'L' and count_adjacent_part2(map, x, y) == 0:
                new_row = new_row + '#'
            else:
                new_row = new_row + seat

        new_layout.append(new_row)
    return new_layout


def empty_the_seats(map):
    changed = 0
    new_layout = []
    for y, row in enumerate(map):
        new_row = ""
        for x, seat in enumerate(row):
            if seat == '#' and count_adjacent_part2(map, x, y) >= 5:
                new_row = new_row + 'L'
                changed += 1
            else:
                new_row = new_row + seat
        new_layout.append(new_row)
    return changed, new_layout


changes = 1
iteration = 0
while changes > 0:
    iteration += 1
    print(f"{iteration}. Iteration.")
    seats = fill_the_seats(seats)
    changes, seats = empty_the_seats(seats)

print(f"No more changes after {iteration} iterations.")

occupied_seats = 0
for row in seats:
    for seat in row:
        if seat == "#":
            occupied_seats += 1

print(occupied_seats)

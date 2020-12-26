import sys

input = [x[:-1] for x in open('input.txt').readlines()]
gen_cube = {0: input}


def get_active_neighbours(x, y, z):
    global gen_cube
    active = 0
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            for zi in range(z-1, z+2):
                if not (xi == x and yi == y and zi == z):  # not the same
                    if 0 <= xi < len(gen_cube[0][0]) and 0 <= yi < len(gen_cube[0]) and zi in gen_cube:  # if indizes exist
                        if gen_cube[zi][yi][xi] == '#':
                            active += 1
    return active


for slice in gen_cube:
    z = slice

    new_slice = []
    for i, row in enumerate(gen_cube[slice]):
        y = i
        new_row = []
        for j, char in enumerate(row):
            x = j
            neighbours = get_active_neighbours(x, y, z)
            if gen_cube[z][y][x] == '#' and neighbours in [2,3]:
                new_char = '#'
                # new_row.append('#')
            elif gen_cube[z][y][x] == '.' and neighbours == 2:
                new_char = '#'
                # new_row.append('#')
            else:
                new_char = '.'
                # new_row.append('.')
            print(x, y, z, new_char)
            new_row.append(new_char)
        new_slice.append(new_row)

for x in new_slice:
    print(x)
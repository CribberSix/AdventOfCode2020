

movements = [(s[0], int(s[1:-1])) for s in open('input.txt').readlines()]

waypoint_x_axis = 0
waypoint_y_axis = 0
facing = 1

compass = ['N', 'E', 'S', 'W']


def move_dir(direction, steps):
    global waypoint_x_axis, waypoint_y_axis
    if direction == 'N':
        y_axis -= steps
    elif direction == 'S':
        y_axis += steps
    elif direction == 'E':
        x_axis += steps
    elif direction == 'W':
        x_axis -= steps


def move_right():
    global facing
    facing += 1
    facing = facing % len(compass)


def move_left():
    global facing
    facing -= 1
    if facing == -1:
        facing = len(compass) - 1

for move in movements:
    print(repr(move))

    if move[0] in compass:
        move_dir(move[0], move[1])
    elif move[0] == 'F':
        move_dir(compass[facing], move[1])
    elif move[0] == 'R':
        times = int(move[1] / 90)
        for x in range(times):
            move_right()
    elif move[0] == 'L':
        times = int(move[1] / 90)
        for x in range(times):
            move_left()

manhatten_distance = abs(waypoint_x_axis) + abs(waypoint_y_axis)
print(f"The manhatten distance is {manhatten_distance}.")


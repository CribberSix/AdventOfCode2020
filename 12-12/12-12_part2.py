movements = [(s[0], int(s[1:-1])) for s in open('input.txt').readlines()]

waypoint_x_axis = 10
waypoint_y_axis = 1
ship_x_axis = 0
ship_y_axis = 0

compass = ['N', 'E', 'S', 'W']


def move_waypoint(direction, steps):
    global waypoint_x_axis, waypoint_y_axis
    if direction == 'N':
        waypoint_y_axis += steps
    elif direction == 'S':
        waypoint_y_axis -= steps
    elif direction == 'E':
        waypoint_x_axis += steps
    elif direction == 'W':
        waypoint_x_axis -= steps


def rotate_right_old():
    global waypoint_x_axis, waypoint_y_axis

    x = waypoint_x_axis
    y = waypoint_y_axis
    print("Right: ", waypoint_x_axis, waypoint_y_axis)
    if x >= 0 and y >= 0:  # 1. Quadrant -> 2. Quadrant
        print("Rotate 1-2")
        waypoint_x_axis = y
        waypoint_y_axis = -x
    elif x >= 0 and y <= 0:  # 2. Quadrant -> 3. Quadrant
        print("Rotate 2-3")
        waypoint_x_axis = y
        waypoint_y_axis = - x
    elif x <= 0 and y <= 0:  # 3.Quadrant -> 4. Quadrant
        print("Rotate 3-4")
        waypoint_x_axis = y
        waypoint_y_axis = abs(x)
    elif x <= 0 and y >= 0:  # 4. Quadrant -> 1. Quadrant
        print("Rotate 4-1")
        waypoint_x_axis = y
        waypoint_y_axis = abs(x)
    else:
        print("Final: ", x, y)
        raise ValueError("This should not be possible anymore.")
    print("Rotated to: ", waypoint_x_axis, waypoint_y_axis)


def rotate_left_old():
    global waypoint_x_axis, waypoint_y_axis

    x = waypoint_x_axis
    y = waypoint_y_axis
    print("Left: ", waypoint_x_axis, waypoint_y_axis)

    if x >= 0 and y >= 0:  # 1. Quadrant -> 4. Quadrant
        print("Rotate 1-4")
        waypoint_x_axis = -y
        waypoint_y_axis = x
    elif x <= 0 and y >= 0:  # 4. Quadrant -> 3. Quadrant
        print("Rotate 4-3")
        waypoint_x_axis = -y
        waypoint_y_axis = x
    elif x <= 0 and y <= 0:  # 3.Quadrant -> 2. Quadrant
        print("Rotate 3-2")
        waypoint_x_axis = abs(y)
        waypoint_y_axis = x
    elif x >= 0 and y <= 0:  # 2. Quadrant -> 1. Quadrant
        print("Rotate 2-1")
        waypoint_x_axis = abs(y)
        waypoint_y_axis = x
    else:
        print("Final: ", x, y)
        raise ValueError("This should not be possible anymore.")
    print("Rotated to: ", waypoint_x_axis, waypoint_y_axis)


def rotate_left():
    global waypoint_x_axis, waypoint_y_axis
    x = waypoint_x_axis
    y = waypoint_y_axis
    waypoint_x_axis = -1 * y
    waypoint_y_axis = x


def rotate_right():
    global waypoint_x_axis, waypoint_y_axis
    x = waypoint_x_axis
    y = waypoint_y_axis
    waypoint_x_axis = y
    waypoint_y_axis = -1 * x


def move_ship(steps):
    global ship_x_axis, ship_y_axis, waypoint_x_axis, waypoint_y_axis
    ship_x_axis += (steps * waypoint_x_axis)
    ship_y_axis += (steps * waypoint_y_axis)


for move in movements:
    print(repr(move))

    if move[0] in compass:
        move_waypoint(move[0], move[1])
    elif move[0] == 'F':
        move_ship(move[1])
    elif move[0] == 'R':
        times = int(move[1] / 90)
        for x in range(times):
            rotate_right()
    elif move[0] == 'L':
        times = int(move[1] / 90)
        for x in range(times):
            rotate_left()

print(f"Final axis is {ship_x_axis}, {ship_y_axis}")
manhatten_distance = abs(ship_x_axis) + abs(ship_y_axis)
print(f"The manhatten distance is {manhatten_distance}.")

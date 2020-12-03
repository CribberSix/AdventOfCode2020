# get input
with open("input.txt", "r") as f:
    input = list(f)
input_cleaned = [x[:-1] for x in input]


def check_slope(right, down):
    index_x = 0
    index_y = 0
    tree_counter = 0

    for i, row in enumerate(input_cleaned):
        if index_y > i:
            continue
        if row[index_x] == '#':
            tree_counter += 1

        index_x += right
        index_y += down
        try:  # check if we need to extend the map for the next step downwards
            row[index_x]
        except IndexError:
            print("Add new columns")
            for i in range(len(input_cleaned)):
                input_cleaned[i] += input_cleaned[i]
    print(f"Slope with {right} right and {down} down has {tree_counter} trees.")
    return tree_counter


x1 = check_slope(1, 1)
x2 = check_slope(3, 1)
x3 = check_slope(5, 1)
x4 = check_slope(7, 1)
x5 = check_slope(1, 2)

print(x1 * x2 * x3 * x4 * x5)
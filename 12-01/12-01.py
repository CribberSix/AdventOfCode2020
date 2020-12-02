
# get input from file
with open("input_part1.txt", "r") as f:
    input = list(f)
input_cleaned = [int(x[:-1]) for x in input]

for x in input_cleaned:
    for y in input_cleaned:
        if x + y == 2020:
            print(f"Ergebnis ist {x * y} mit den Zahlen {x} und {y}.")


# get input from file
with open("input_part2.txt", "r") as f:
    input = list(f)
input_cleaned = [int(x[:-1]) for x in input]


for x in input_cleaned:
    for y in input_cleaned:
        for z in input_cleaned:
            if z + x + y == 2020:
                print(f"Ergebnis ist {x * y * z} mit den Zahlen {x}, {y} und {z}.")


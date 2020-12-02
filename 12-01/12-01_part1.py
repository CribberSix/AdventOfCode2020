
# get input from file
with open("input_part1.txt", "r") as f:
    input = list(f)
input_cleaned = [int(x[:-1]) for x in input]

for x in input_cleaned:
    for y in input_cleaned:
        if x + y == 2020:
            print(f"Ergebnis ist {x * y} mit den Zahlen {x} und {y}.")
            break
    else:
        continue
    break

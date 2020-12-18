import datetime

input = [s[:-1] for s in open('input.txt').readlines()]
busses = input[1].split(',')

timetable = []
max_bus = (-1,-1)
t = 0
for b in busses:
    if b != 'x':
        timetable.append((int(b), t ))
        if int(b) > max_bus[0]:
            max_bus = (int(b), t)
    t += 1

print(f"max_bus: {max_bus}")
print(f"Timetable: {timetable}")
print(f"Normalize with {max_bus[1]} for the max bus to make the biggest possible steps while brute-forcing.")
timetable_normalized = []
for t in timetable:
    timetable_normalized.append( (t[0], t[1] - max_bus[1]) )
print(f"timetable_normalized: {timetable_normalized}")

test = 1000
t0 = datetime.datetime.now()
last = t0

for i in range(100000000000252, 1000000000000000000000000, max_bus[0]):
    if i > test:  # Show progress once in a while - while brute-forcing.
        print(f"Working at {i} ...")
        print(f"\t\t\tOverall Runtime: {round((datetime.datetime.now() - t0).total_seconds())} seconds.")
        print(f"\t\t\tRuntime since last: {round((datetime.datetime.now() - last).total_seconds())} seconds.")
        last = datetime.datetime.now()
        if test < 10000000000000:
            test = test * 10
        else:
            test = test + 100000000000

    truths = 0
    for b in timetable_normalized:
        if (i + b[1]) % b[0] == 0:
            truths += 1
        else:
            break
    if truths == len(timetable_normalized):
        print(f"FOUND i: {i - max_bus[1]}")
        break

print("Finished.")
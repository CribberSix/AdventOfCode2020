
input = [s[:-1] for s in open('input.txt').readlines()]

earlierst = int(input[0])
busses = [int(x) for x in input[1].split(',') if x != 'x']

busses_timetable = []
for b in busses:
    t = 0
    while t < earlierst:
        t += b
    busses_timetable.append((b,t))


best_bus = (0,1000000000000)
for b in busses_timetable:
    if b[1] - earlierst < best_bus[1] - earlierst:
        best_bus = b

print(f"I have to wait {best_bus[1] - earlierst} minutes.")
print(f"Minutes multiplied with bus number {best_bus[0]} results in {(best_bus[1] - earlierst) * best_bus[0]}.")

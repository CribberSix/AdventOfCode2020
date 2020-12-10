
def is_valid(sublist, res) -> bool:
    for x in sublist:
        for y in sublist:
            if x != y and x + y == res:
                return True
    return False


def find_first_notsum(input, preamble=25):
    for i in range(preamble, len(input)):
        k = is_valid(input[i - preamble:i], input[i])
        if not k:
            print(f"First number which is not a sum of the previous {preamble}: {input[i]}.")
            return input[i]


# get input
with open("input.txt", "r") as f:
    input = list(f)
input = [int(x[:-1]) for x in input]

invalid_num = find_first_notsum(input)

end = False
for i, x in enumerate(input):
    mylist = [x]
    summe = x
    for y in input[i+1:]:
        if x == y:
            continue
        summe += y
        mylist.append(y)
        if summe == invalid_num:
            print("Found the first continuous list of numbers that add to the invalid_num.")
            end = True
            break
        elif summe > invalid_num:
            break
    if end:
        break

print(f"The smallest plus largest number is {min(mylist) + max(mylist)}.")
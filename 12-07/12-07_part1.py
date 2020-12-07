import re

# get input
with open("input.txt", "r") as f:
    input = list(f)
input = [x[:-1] for x in input]

# parse input
list_of_bags = []
for line in input:
    t = line.split("contain")
    bag = t[0][:-5].strip(" ")
    contains = t[1].split(",")
    if t[1] == ' no other bags.':
        continue

    temp = []
    for x in contains:
        m = re.search(r"(\d) ([a-z]* [a-z]*)", x)
        number = m.group(1)
        color = m.group(2).strip(" ")
        temp.append(color)

    list_of_bags.append((bag, temp))

# search for shiny gold in bags
can_contain_gold = []
for x in list_of_bags:
    if 'shiny gold' in x[1]:
        can_contain_gold.append(x[0])

# search for bags (which can contain shiny gold) in the rest of bags
# append if not yet in my can_contain_gold list
for i in range(1000):
    print(i)
    c = 0  # counter how many new ones we added this iteration
    for x in list_of_bags:
        for y in can_contain_gold:
            if y in x[1] and x[0] not in can_contain_gold:
                can_contain_gold.append(x[0])
                c += 1
    if c == 0:
        break  # if we couldn't add any new ones, we break early.

unique = list(set(can_contain_gold))
print(unique)
print("Elements in list: " + str(len(unique)))


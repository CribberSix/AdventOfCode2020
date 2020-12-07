import re

# get input
with open("input.txt", "r") as f:
    input = list(f)
input = [x[:-1] for x in input]  # remove linebreak char at the end

# parse input
list_of_bags = []
for line in input:
    t = line.split("contain")
    bag = t[0][:-5].strip(" ")
    contains = t[1].split(",")
    if t[1] == ' no other bags.':
        continue

    temp = []  # temp list for sub bags
    for x in contains:
        m = re.search(r"(\d) ([a-z]* [a-z]*)", x)
        number = m.group(1)
        color = m.group(2).strip(" ")
        temp.append((color, number))

    list_of_bags.append((bag, temp))

# für jede Tasche aus bags_to_buy muss ich alle subtaschen (mit Anzahl) hinzufügen.
# Für jede Subtasche schaue ich iterativ nach welche subtaschen diese hat, und füge sie hinzu.
bags_to_buy = []
current = ['shiny gold']  # we start with our shiny gold bag.
for i in range(1000):
    c = 0
    newly_added = []
    for bag in current:  # Für jede Tasche
        for potential in list_of_bags:  # suche ich diese in der gesamten Liste
            if bag == potential[0]:  # -> gefunden!
                for subbag in potential[1]:  # für jede Tasche die wiederum in dieser enthalten ist
                    for _ in range(int(subbag[1])):
                        newly_added.append(subbag[0])  # füge ich jede Subtaschen in der entsprechenden Anzahl hinzu

    bags_to_buy = bags_to_buy + current  # bags for which we already looked for subbags we add to the final list
    current = newly_added  # for newly added bags, we need to look for further subbags.
    if len(current) == 0:
        print(f"{i} iterations needed to exhaust current list.")
        break  # break early

print("bags_to_buy: " + str(bags_to_buy))
print(f"We need to buy {len(bags_to_buy) - 1} bags.")   # we subtract our shiny gold bag as we only want to find subs.

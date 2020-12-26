import re

input = [s[:-1] for s in open('input.txt').readlines()]

my_ticket = []
number_of_rules = 20
tickets_active = False
valid_numbers = []  # part 1
invalid_numbers = []  # part 1
valid_tickets = []  # part 2

rules = []
for i, line in enumerate(input):
    if tickets_active:  # check for valid tickets
        ticket = [int(x) for x in line.split(",")]
        valid_t = True
        for num in ticket:  # check every number on the ticket for validity
            if num not in valid_numbers:
                invalid_numbers.append(num)  # part 1
                valid_t = False  # part 2
        if valid_t:
            valid_tickets.append(ticket)

    if i < number_of_rules:
        # Get valid numbers for the rule
        m = re.findall(r"((\d+)-(\d+))", line)
        rule_numbers = []
        for triple in m:
            for x in range(int(triple[1]), int(triple[2]) + 1):
                valid_numbers.append(x)  # part 1
                rule_numbers.append(x)  # part 2

        # get name of the rule
        rule_name = re.search(r"^(\w+ ?\w*)", line)
        # print(test.group(1), temp)
        rules.append((rule_name.group(1), rule_numbers))

    if line == 'nearby tickets:':
        tickets_active = True
    elif line == 'your ticket:':
        my_ticket = [int(x) for x in input[i+1].split(",")]

print(f"Part 1 Solution: sum of invalid numbers: {sum(invalid_numbers)}")


# figure out which index of the valid tickets is which rule.
result = []
while len(result) < number_of_rules:
    for index in range(0, len(valid_tickets[0])):
        # for each index, we determine the correct rule.
        current_rules = rules.copy()
        for t in valid_tickets:  # for every ticket
            for r in current_rules:  # for every rule
                if t[index] not in r[1]:  # we check whether the current number is valid
                    current_rules.remove(r)

        if len(current_rules) == 1:
            # if we have only 1 possible rule left, it must be it - otherwise, start over again.
            # print(f"Field {index} ist {current_rules[0][0]}.")
            result.append((current_rules[0][0], index))
            rules.remove(current_rules[0])


ret = 1
for x in result:
    if x[0][:3] == 'dep':
        ret = ret * my_ticket[x[1]]
print("\nPart 2 Solution: departure numbers from my tickets multiplied: " + str(ret))

import re

input = [s[:-1] for s in open('input.txt').readlines()]

my_ticket = []
number_of_rules = 20
tickets_active = False
valid_numbers = []  # part 1
invalid_numbers = []  # part 1
valid_tickets = []  # part 2
rules = []  # part 2


# Parse the rules and tickets to figure out which numbers (part1) / tickets (part2) are invalid / valid.
for i, line in enumerate(input):

    if i < number_of_rules: # Parse the rules
        m = re.findall(r"((\d+)-(\d+))", line)
        rule_numbers = []
        for triple in m:
            for x in range(int(triple[1]), int(triple[2]) + 1):
                valid_numbers.append(x)  # part 1
                rule_numbers.append(x)  # part 2

        rule_name = line.split(":")[0]
        rules.append((rule_name, rule_numbers))

    elif tickets_active:  # check for valid tickets
        ticket = [int(x) for x in line.split(",")]
        ticket_is_valid = True
        for num in ticket:  # check every number on the ticket for validity
            if num not in valid_numbers:
                invalid_numbers.append(num)  # part 1
                ticket_is_valid = False  # part 2
        if ticket_is_valid:
            valid_tickets.append(ticket)

    elif line == 'nearby tickets:':
        tickets_active = True  # all following are tickets now.

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
            # if we have only 1 possible rule left, it must be it.
            print(f"Field {index} ist {current_rules[0][0]}.")
            result.append((current_rules[0][0], index))
            rules.remove(current_rules[0])


ret = 1
for x in result:
    if x[0][:3] == 'dep':
        ret = ret * my_ticket[x[1]]
print("\nPart 2 Solution: departure numbers from my tickets multiplied: " + str(ret))

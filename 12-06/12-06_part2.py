# get input
with open("input.txt", "r") as f:
    input = list(f)
input = [x[:-1] for x in input]


# Parse into lists of groups
groups = []
current_group = []
list_of_letters = []
for row in input:
    if row == '':  # group ended
        groups.append(current_group)
        current_group = []
    else:
        current_group.append(row)
if len(current_group) > 0:
    groups.append(current_group)  # append last group


result = 0
for group in groups:
    # for each group we test which letter appears in every item
    for i, item in enumerate(group):

        if i == 0: # we start with the set of letters from the first item
            current_yes = [char for char in item]

        else:  # for all subsequent group members
            for char in current_yes[:]:  # we test whether every char in current_yes
                if char not in item:  # appears in the member
                    current_yes.remove(char)  # if the char does not appear in the member, we remove it from current_yes

    result = result + len(current_yes)  # we add the number of remaining current_yes

print("__________________")
print(f"FINAL: {result}")

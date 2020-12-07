# get input
with open("input.txt", "r") as f:
    input = list(f)
input = [x[:-1] for x in input]

# Parse
groups = []
current_group = ""
for row in input:
    if row == '':  # group ended
        groups.append(current_group)
        current_group = ""
    else:
        current_group = current_group + row

if current_group != '':
    groups.append(current_group)  # append last group


# get distinct letters for each group
cleaned = [''.join(set(x)) for x in groups]

# count remaining letters in all groups and sum
i = 0
for x in cleaned:
    i += len(x)
print(i)  # 6726

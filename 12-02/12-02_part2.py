# get input
with open("input_part1.txt", "r") as f:
    input = list(f)
input_cleaned = [x[:-1] for x in input]

# parse input lines into dictionaries
input_parsed = []
for d in input_cleaned:
    interrim = d.split(' ')
    my_range = interrim[0].split('-')
    letter = interrim[1][0]
    pw = interrim[2]
    input_parsed.append({'pos_one': int(my_range[0]),
                         'pos_two': int(my_range[1]),
                         'letter': letter,
                         'pw': pw
                         })


def is_valid(current_dict):
    p1 = current_dict['pos_one'] - 1  # no index zero concept
    p2 = current_dict['pos_two'] - 1  # no index zero concept

    if (current_dict['pw'][p1] == current_dict['letter'] and current_dict['pw'][p2] != current_dict['letter']) or \
            (current_dict['pw'][p1] != current_dict['letter'] and current_dict['pw'][p2] == current_dict['letter']):
        return 1
    else:
        return 0


# count valid passwords
valid_pws = 0
for d in input_parsed:
    v = is_valid(d)
    if v == 1:
        t = 'valid'
    else:
        t = 'invalid'
    print(f"Dict {d} is {t}.")
    valid_pws += is_valid(d)

print(f"Alltogether {valid_pws} passwords were valid.")

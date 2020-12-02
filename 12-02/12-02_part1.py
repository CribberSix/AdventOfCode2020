# get input
with open("input_part1.txt", "r") as f:
    input = list(f)
input_cleaned = [x[:-1] for x in input]

# parse input into dictionaries for each line
input_parsed = []
for x in input_cleaned:
    interrim = x.split(' ')
    my_range = interrim[0].split('-')
    letter = interrim[1][0]
    pw = interrim[2]
    input_parsed.append({'range_start': int(my_range[0]),
                         'range_end': int(my_range[1]),
                         'letter': letter,
                         'pw': pw
                         })


def is_valid(current_dict):
    if current_dict['range_start'] <= count_occurences(current_dict['letter'], current_dict['pw']) <= current_dict['range_end']:
        return 1
    else:
        return 0


def count_occurences(char, longstring):
    i = 0
    for x in longstring:
        if x == char:
            i += 1
    return i

valid_pws = 0
for d in input_parsed:
    if is_valid(d):
        t = 'valid'
    else:
        t = 'invalid'
    print(f"Dict {d} is {t}.")
    valid_pws += is_valid(d)

print(f"Alltogether {valid_pws} passwords were valid.")

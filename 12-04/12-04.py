import ast
import re

# get input
with open("input.txt", "r") as f:
    input = list(f)
input_cleaned = [x[:-1] for x in input]

input_parsed = []
cp = ""
for x in input_cleaned:
    if x == "":
        input_parsed.append(cp)
        cp = ""
    else:
        cp = cp + " " + x
input_parsed.append(cp)

p = ["{" + x.replace(" ", "', '").replace(":", "':'")[2:] + "'}" for x in input_parsed]
dicts = [ast.literal_eval(x) for x in p]

valid = 0
invalid = 0
for x in dicts:
    try:
        missing = x['byr']
        missing = x['iyr']
        missing = x['eyr']
        missing = x['hgt']
        missing = x['hcl']
        missing = x['ecl']
        missing = x['pid']
        valid += 1
    except KeyError:
        invalid += 1
print(f"Task 1 - invalid: {invalid}")
print(f"Task 1 - valid: {valid}")


def is_valid(d):
    try:
        # birth year
        if not(1920 <= int(d['byr']) <= 2002):
            return 0
        # issue year
        if not (2010 <= int(d['iyr']) <= 2020):
            return 0
        # expiration year
        if not (2020 <= int(d['eyr']) <= 2030):
            return 0

        if d['hgt'][-2:] == 'cm':
            if not (150 <= int(d['hgt'][:-2]) <= 193):
                return False
        elif d['hgt'][-2:] == 'in':
            if not (59 <= int(d['hgt'][:-2]) <= 76):
                return False
        else:
            return False

        if not re.match('^#([a-f]|[0-9]){6}$', d['hcl']):
            return False

        if not d['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False

        if not re.match('^[0-9]{9}$', d['pid']):
            return False

        return True
    except KeyError:
        return False


c = 0
for x in dicts:
    c += is_valid(x)
print()
print(f"Task 2 - valid: {c}")

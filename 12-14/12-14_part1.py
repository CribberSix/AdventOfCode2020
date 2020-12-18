import re


def turn_into_bit(number):
    return "{:036b}".format(number)


def turn_into_int(bitstring_):
    return int(bitstring_, 2)


def write_to_memory(memoryposition, value):
    global memory, mask
    bitstring = turn_into_bit(value)
    # print("Bitstring: "  +repr(bitstring))
    # print("Mask:      " + repr(mask))
    bitstring_masked = ''
    for i, item in enumerate(bitstring):
        if mask[i] != 'X':
            bitstring_masked = bitstring_masked + mask[i]
        else:
            bitstring_masked = bitstring_masked + item
    # print("Masked:    " + repr(bitstring_masked))
    # print("______________")
    memory[str(memoryposition)] = bitstring_masked


input = [s[:-1] for s in open('input.txt').readlines()]

memory = {}
for line in input:
    if line[:4] == 'mask':  # update the mask
        mask = line[7:]
    else:  # memory command
        m = re.search(r"^mem\[(\d+)\] = (\d+)$", line)
        memory_loc = m.group(1)  # string for dict key
        value = int(m.group(2))  # integer
        write_to_memory(memory_loc, value)

sum_of_nums = 0
for key in memory:
    sum_of_nums += turn_into_int(memory[key])

print(f"sum_of_nums: {sum_of_nums}")

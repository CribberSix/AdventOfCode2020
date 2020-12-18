import re


def turn_into_bit(number):
    return "{:036b}".format(number)


def turn_into_int(bitstring_):
    return int(bitstring_, 2)


def get_memory_loc(mem, mask):#
    """
    This needs to be optimizied so much...
    """
    locs = []
    memory_current = ""
    for i, letter in enumerate(mask):
        if letter == '0':
            memory_current = memory_current + mem[i]
        elif letter == '1':
            memory_current = memory_current + '1'
            mem = mem[:i] + '1' + mem[i+1:]  # write fixed change to memory-address
            mask = mask[:i] + '0' + mask[i+1:]  # overwrite to not-handle for further recursive loops
        elif letter == 'X':
            mask = mask[:i] + '0' + mask[i+1:]  # overwrite as we already handled it
            mem_c1 = mem[:i] + "1" + mem[i+1:]  # write first option to memory-address
            mem_c2 = mem[:i] + "0" + mem[i+1:]  # write second option to memory-address
            locs = locs + get_memory_loc(mem_c1, mask)
            locs = locs + get_memory_loc(mem_c2, mask)
            return locs

    locs.append(memory_current)
    return locs


def write_to_memory(memory_loc, value, mask):
    global memory_final
    memory_locations = []
    # calculate every memory position based on original memory_loc + mask
    memlocs = get_memory_loc(memory_loc, mask)
    #cleaned_mems = []
    #for x in memlocs:
    #    print(x)
    #    if not '_' in x:
    #        cleaned_mems.append(x)
    #cleaned_mems = list(set(cleaned_mems))
    #for x in cleaned_mems:
    #    print("mems:       " + x + "  -> " + str(turn_into_int(x)))

    for x in memlocs:
        memory_final[turn_into_int(x)] = value



input = [s[:-1] for s in open('input.txt').readlines()]
memory_final = {}
for line in input:
    if line[:4] == 'mask':  # update the mask
        print("_________ NEW MASK _________")
        mask = line[7:]
    else:  # memory command
        m = re.search(r"^mem\[(\d+)\] = (\d+)$", line)
        memory_loc = turn_into_bit(int(m.group(1)))  # bit-string for mem-value
        value = int(m.group(2))
        print("memory_loc: " + str(memory_loc))
        print("mask:       " + str(mask))
        write_to_memory(memory_loc, value, mask)



sum_of_nums = 0
for key in memory_final:
    sum_of_nums += memory_final[key]

print(f"sum_of_nums: {sum_of_nums}")

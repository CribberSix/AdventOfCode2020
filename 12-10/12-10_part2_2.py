numbers = [int(s) for s in open('input.txt').readlines()]
numbers.append(0)
numbers.sort()

# first attempt : mathematical - failed.
# second attempt : brute force (memory error, then optimized & takes foerver)
# third attempt: recursive - takes forever.
# fourth atempt: recursive with saving the number of paths from number x in the list. works. whoop.

num_of_paths_starting_from = {}

def mycount(numbers):
    currently_last = numbers[-1]
    if currently_last in num_of_paths_starting_from:  # already calculated
        # no need to go back into it again, just return the result
        return num_of_paths_starting_from[currently_last]

    if len(numbers) <= 2:
        # print(f"Path ends here - only 0, 1 or 2 items in the list: {nums}")
        return 1

    paths = 0
    # next guy before me
    if currently_last - numbers[-2] <= 3:  # can I still connect to the next one?
        #print(f"I - {nums[-1]} - can directly connect to {nums[-2]} in {nums} and have {paths} paths.")
        paths += mycount(numbers[:-1])   # yes - then give me all possibilities AFTER YOU.

    # can I skip one?
    if len(numbers) >= 3 and currently_last - numbers[-3] <= 3:
        #print(f"I - {nums[-1]} - can skip 1 to connect to {nums[-3]} in {nums}")
        paths += mycount(numbers[:-2])

    # can I skip two?
    if len(numbers) >= 4 and currently_last - numbers[-4] <= 3:
        #print(f"I - {nums[-1]} - can skip 2 to connect to {nums[-4]} in {nums}")
        paths += mycount(numbers[:-3])

    #print(f"I - {nums[-1]} finally return with {paths} paths.")
    num_of_paths_starting_from[currently_last] = paths
    # I save how many paths number x has after going through all possible paths downwards from it,
    # so I dont have to walk the tree back down again
    return paths


print(mycount(numbers))


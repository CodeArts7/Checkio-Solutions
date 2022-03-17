from itertools import islice


with open('text', 'r') as example:  # using this function gives us an opportunity to print only what we need
    header = islice(example, 3)  # not using the whole file

    for line in header:
        print(line, end=" ")
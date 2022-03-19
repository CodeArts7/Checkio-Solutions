from itertools import filterfalse


def fl(n):
    if n > 2:
        return True
    return False


card_values = ['Ace', 'King', 'Queen', 'Jack']
numbers = [0, 1, 2, 3, 5, 6, 7, 8]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]


result = filterfalse(fl, numbers)

for item in result:
    print(item)
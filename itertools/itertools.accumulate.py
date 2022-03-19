from itertools import accumulate


card_values = ['Ace', 'King', 'Queen', 'Jack']
numbers = [0, 1, 2, 3, 5, 6, 7, 8]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]


result = accumulate(numbers)

for item in result:
    print(item)
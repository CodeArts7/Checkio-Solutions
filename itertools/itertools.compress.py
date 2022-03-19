from itertools import compress


card_values = ['Ace', 'King', 'Queen', 'Jack']
numbers = [0, 1, 2, 3, 5, 6, 7, 8]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

result = compress(card_values, selectors)

for item in result:
    print(item)

#  the difference between itertools.compress and buid-in filter()nis that you need to create the function beforehand
def fl(number):
    if number % 2 == 0:
        return True
    return False


result_two = filter(fl, numbers)

for item_two in result_two:
    print(result_two)
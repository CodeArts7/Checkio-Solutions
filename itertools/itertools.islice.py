from itertools import islice


card_values = ['Ace', 'King', 'Queen', 'Jack']
numbers = [0, 1, 2, 3, 5, 6, 7, 8]
names = ['Corey', 'Nicole']

sliced = islice(numbers, 3)
improved_sliced = islice(numbers, 2, 5)
final = islice(numbers, 1, 3, 2)

print(list(sliced))
print(list(improved_sliced))
print(list(final))
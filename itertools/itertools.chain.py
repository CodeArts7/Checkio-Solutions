from itertools import chain


card_values = ['Ace', 'King', 'Queen', 'Jack']
number_of_wins = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

combined = chain(card_values, number_of_wins, names)
print(list(combined))
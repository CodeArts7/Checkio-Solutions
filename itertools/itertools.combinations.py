from itertools import combinations
# the whole difference between itertools.permutations is that here the order doesn't matter


card_values = ['Ace', 'King', 'Queen', 'Jack']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = combinations(card_values, 2)  # try out itertools.permutations to see the difference
for cards in result:
    print(cards)
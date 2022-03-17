from itertools import product


card_values = ['Ace', 'King', 'Queen', 'Jack']
pin_code_numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = product(pin_code_numbers, [1])  # here we multiply our iter object on itself
result_two = product(pin_code_numbers, repeat=4)  # here we added a repeat argument,
# we multiply our iter object on itself
for guess in result:
    print(guess)

for guess_two in result_two:
    print(guess_two)
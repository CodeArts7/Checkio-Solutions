from itertools import permutations


def function_one(string):
    words = string.split()
    result = " "
    for item in permutations(words):
        result += " ".join(item) + "\n"
    return result


string = input("Enter your search: ")
print(function_one(string))
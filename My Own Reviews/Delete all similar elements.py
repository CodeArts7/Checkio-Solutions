from typing import Iterable


# we can delete all similar symbols using print(list(set(items))), but the order might be random
def compress(items: list) -> Iterable:
    result = []
    for symbol in items:
        if symbol not in result:
            result.append(symbol)
    return result


print(list(compress([
    5, 5, 5,
    4, 5, 6,
    6, 5, 5,
    7, 8, 0,
    0])))
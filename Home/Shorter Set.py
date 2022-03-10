def remove_min_max(data: set, total: int) -> set:
    if total > 0:
        a = list(sorted(data))
        del a[0:total]
        del a[-total:]
        return set(a)
    else:
        return data

print('Example:')
print(remove_min_max({4,5,6,7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()

print("The first mission is done! Click 'Check' to earn cool rewards!")
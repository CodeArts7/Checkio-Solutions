from itertools import repeat


counter = repeat(2, times=4)

#squares = map(pow, range(10), repeat(2))
#print(list(squares))
print(list(counter))
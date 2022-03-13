from functools import partial


# our first function that contains two arguments: a, b
def fun(a: int, b: int) -> int:
    return a - b

# but we need to add another or new arguments not changing or writing a new function, so we use partial here
p = partial(fun, 5)

# and as for print we gonna use partial that calls as a function:
print(p())
# the result would be 2

# also we can create a partial that would contain two arguments each one from two different functions, like here:
# one from p and another from p_o
def fun2(p_o):
    return partial(p_o, 5)


p_o = fun2(p)

# after we call "print(p_o())"


# that how it would look like if we call using two different arguments
# P.S. don't forget that our functions takes only two arguments, so then delete one before using this method
def multiply(a, b):
    return a * b


p = partial(multiply, 9)



def multiply_two(p_o):
    return partial(p, 3)


p_o = multiply_two(p)

print(p_o())
# Make two utilities functions

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


# Passing in a function into another function

def function_plus_one(func, num1, num2):
    return func(num1, num2) + 1

print(function_plus_one(add, 5, 6))

# Returning a function from another function


# ------- LAMBDA -----------

# A lambda function is a small anonymous function that can take
# any number of arguments, but it can only have one expression.

# It works like a regular function but is defined using the
# lambda keyword instead of def. Lambda functions are often
# used for short, simple operations that fit on one line.


# Syntax: lambda arguments: expression
# Example 1: A regular function that adds two numbers.
# flake8 prefers this over assigning a lambda to a variable.
def add(x, y):
    return x + y


result = add(5, 3)
print("The sum is:", result)

# filter
# Example 2: Using a lambda function with filter() to
# keep only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]

# filter(function, iterable) => keep the elements for which
# the function returns True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# map
# Example 3: Using a lambda function with map() to square
# each number in a list
# map(function, iterable) => apply the function to every item
# of the iterable and return the transformed results
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# ------- LAMBDA -----------

# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

# It works like a regular function but is defined using the lambda keyword instead of def. Lambda functions are often used for short, simple operations that can be defined in a single line of code.

# Syntax: lambda arguments: expression
# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print("The sum is:", result)

# filter
# Example 2: Using a lambda function with the filter() function to filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
# filter(function, iterable) => filter out the elements from the iterable for which the function returns True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# map
# Example 3: Using a lambda function with the map() function to square each number in a list
# map(function, iterable) => apply the function to every item of the iterable and return a list of the results
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# List comprehensions are a concise way to create lists.
# They combine an expression with a for clause and optional
# if conditions inside square brackets.

numbers = [1, 2, 3, 4, 5]

squared_numbers = [x * x for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# With an if condition
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# List comprehensions are a concise way to create lists. They consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

numbers = [1, 2, 3, 4, 5]

squared_numbers = [x * x for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# With an if condition
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

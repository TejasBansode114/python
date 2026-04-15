# --------- List is a collection which is ordered and changeable. Allows duplicate members.---------

numbers = [1, 2, 3, 4, 5]

numbers.append(6)  # Adds 6 to the end of the list
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

numbers.insert(0, 0)  # Inserts 0 at index 0
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6]

numbers.remove(3)  # Removes the first occurrence of 3
print(numbers)  # Output: [0, 1, 2, 4, 5, 6]

numbers.pop()  # Removes and returns the last item
print(numbers)  # Output: [0, 1, 2, 4, 5]

numbers[2] = 10  # Updates the value at index 2 to 10
print(numbers)  # Output: [0, 1, 10, 4, 5]

# --------- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.---------

point = (10, 20)
print(point[0])  # Output: 10

# point[0] = 30  # This will raise a TypeError because tuples are immutable


# --------- Set is a collection which is unordered and unindexed. No duplicate members.---------
fruits = {"apple", "banana", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

fruits.add("orange")  # Adds 'orange' to the set
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits.remove("banana")  # Removes 'banana' from the set
print(fruits)  # Output: {'apple', 'cherry', 'orange'}


# --------- Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.---------
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])  # Output: Alice
person["age"] = 31  # Updates the value of 'age' to 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
person["country"] = "USA"  # Adds a new key-value pair to the dictionary
print(
    person
)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

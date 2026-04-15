number = [1, 2, 3, 4, 5]

# --------- Iterators are objects that can be iterated upon, meaning that you can traverse through all the values. They implement the iterator protocol, which consists of the methods __iter__() and __next__().---------
iterator = iter(number)  # Create an iterator from the list

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 5

print("-------------------------------------------------------------")
# print(next(iterator))  # This will raise a StopIteration exception because there are no more items to iterate


# Generator --


def count_up(n):
    for i in range(n):
        yield i  # Yield the current value of i and pause the function


gen = count_up(5)  # Create a generator object

for number in gen:
    print(number)  # Output: 0, 1, 2, 3, 4

# ===== *args =====
# *args lets you pass a variable number of non-keyword
# arguments to a function. It collects extra positional
# arguments into a tuple.


# *args => allow to accept any number of positional arguments
# If you aren't sure how many inputs a user might
def add(*args):
    total = 0

    for num in args:
        total += num
    return total


result = add(1, 2, 3, 4, 5)
print("Sum:", result)


# ===== **kwargs =====
# **kwargs lets you pass a variable number of keyword
# arguments to a function. It collects extra keyword
# arguments into a dictionary.


# ** --> Take any arguments passed with an equal sign and put them in a dictionary
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Tej", age=30, city="New York", profession="Developer")


# *args (Extra values)

# **kwargs (Extra labeled values)


def make_pizza(size, *toppings, **delivery_info):
    print(f"Size: {size}")
    print(f"Toppings: {toppings}")
    print(f"Delivery: {delivery_info}")


make_pizza("Large", "Cheese", "Corn", address="Pune", tip=5)

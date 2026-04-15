# 1. THE BLUEPRINT: Think of a class as a template for a person.
class Person:
    # 2. THE CONSTRUCTOR: This special method runs automatically
    # when you create a new person.
    # 'self' represents the specific object being created.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 3. THE METHOD: A function that belongs to this person.
    def greet(self):
        # 'self.name' and 'self.age' access the object's unique data.
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# 4. INSTANTIATION: Creating an actual object (p1) based on
# the blueprint (Person).
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# 5. EXECUTION: Calling the method on that specific object.
print(p1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(p2.greet())  # Output: Hello, my name is Bob and I am 25 years old.


class Demo:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


d = Demo()  # Output: Constructor called

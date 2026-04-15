# FUNCTIONS - A function is a block of code that performs a specific task. It can take inputs, called parameters, and can return an output. Functions help to organize code, make it reusable, and improve readability.
# def -> defines a function
def greet():
    print("Hello! Welcome to Python programming.")


# Calling the function
greet()

#---------------------------------------------------------------------------------------------------------------------
# Function with parameters
def greet_user(name):  # name is a parameter
    print("Hello, " + name + "! Welcome to Python programming.")


# Calling the function with an argument
greet_user("Tejas")

#---------------------------------------------------------------------------------------------------------------------

# Function with return value
def add(a, b):
    return a + b  # This will return the sum of a and b


# calling the function with arguments
result = add(5, 3)
print("The sum is:", result)

#---------------------------------------------------------------------------------------------------------------------

# Arguments( *args and **kwargs)




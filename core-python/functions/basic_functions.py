# ===== BASIC FUNCTION =====
# def -> function keyword
def greet(name):
    print("Hello", name)


# Calling the function
greet("Tej")


# ===== RETURN FUNCTION =====
def add(a, b):
    return a + b


result = add(10, 20)
print("Sum:", result)


# ===== DEFAULT PARAM =====
def welcome(name="User"):
    print("Welcome", name)


welcome()
welcome("Tej")

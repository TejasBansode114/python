# ==== PRINT ====
print("Hello, World!")
print("Welcome to Python programming.")

# ==== VARIABLES ====
name="Tejas"
age=25
hight=5.9
is_devloper=True

print("Name:", name)
print("Age:", age)
print("Height:", hight)
print("Is Developer:", is_devloper)

# ==== USER INPUT ====
#Input function is used to take input from the user. It always returns a string.
user_name = input("Enter your name: ")

#To convert the input to an integer, we can use the int() function. This is necessary because the input function returns a string, and we want to work with the age as a number.    
user_age = int(input("Enter your age: "))

print("Hello, " + user_name + "! You are " + str(user_age) + " years old.")
class InvaliAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvaliAgeError("Age must be at least 18.")
    return "Age is valid."


try:
    age = int(input("Enter your age: "))
    print(check_age(age))

except InvaliAgeError as e:
    print("Invalid age:", e)
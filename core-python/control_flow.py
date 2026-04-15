# ======== IF ELSE (Voting)=========

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# =======IF ELSE (Make Logic =========

mark = int(input("Enter your mark: "))

if mark >= 90:
    print("Grade: A")
# elif = else if
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
# else = else
else:
    print("Fail")

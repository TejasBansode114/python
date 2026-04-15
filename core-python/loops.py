# ------Print number form 1 to 5 -------

# (1, 10) means start from 1 and go up to 9 (10 is not included)
for i in range(1, 10):
    print(i)

# While loop
count = 1
while count <= 5:
    print(count)
    count += 1  # This is equivalent to count = count + 1

# loop with condition
for i in range(1, 11):
    if i % 2 == 0:  # Check if the number is even
        print("This are the even numbers", i)
    else:
        print("This are the odd numbers", i)

# Break and continue
# Break exits the loop when a condition is met.
# In this example, the loop stops when i is equal to 5.
for i in range(1, 11):
    if i == 5:
        break  # This will exit the loop when i is 5
    print(i)

# Continue skips the current iteration and moves to the next one.
# In this example, when i is equal to 3, the print is skipped.
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# Count vowels
text = input("Enter a string: ")
vowel_count = 0
for char in text:
    if char.lower() in "aeiou":
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)

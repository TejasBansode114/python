# ---------Recursion------------
# A function that calls itself is called a recursive function.


# Example 1: A recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))

try:
    # try → risky code
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    # EXCEPT → handling the exception
    print("Cannot divide by zero ❌")

except ValueError:
    # EXCEPT → handling the exception
    print("Invalid input ❌")

finally:
    # FINALLY → code that will always execute
    print("Execution completed ✅")

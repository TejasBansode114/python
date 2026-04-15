#Encapsulation - Wrapping data and methods that operate on the data within a single unit (class) and restricting access to some of the object's components.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(1500)
print(account.get_balance())  # Output: 1500


#Abstraction - Hiding the complex implementation details and showing only the necessary features of an object.

class Car:
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

my_car = Car()
my_car.start_engine()  # Output: Engine started
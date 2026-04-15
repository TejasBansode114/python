# Same method → different behavior
class Dog:
    def speak(self):
        print("Dog barks")


class Cat:
    def speak(self):
        print("Cat meows")


def make_animal_speak(animal):
    animal.speak()  # This will call the speak method of the specific animal passed in


make_animal_speak(Dog())  # Output: Dog barks
make_animal_speak(Cat())  # Output: Cat meows

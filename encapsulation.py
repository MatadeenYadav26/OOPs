class Animal:

    __name = "Lion"

    def speak(self):
        print("I willl roar.")

obj = Animal()

obj.name = "Zebra"

# print(obj.name)
# obj.__speak()

# print(obj.__name)


class Human(Animal):
    def say(self):
        print(f"Hello , my name is {super().__name}")

obj = Human()

obj.say()
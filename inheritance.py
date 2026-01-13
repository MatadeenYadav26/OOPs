class Animal:   #Parent Class , Super Class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Your name is {self.name} and your age is {self.age}.")


class Human(Animal): #Child class , sub class #all the methods and attributes under animal class will be accessed by human class too #inheritence
    def __init__(self, name, age, number , bloodgroup):
        super().__init__(name, age)
        self.number = number
        self.bloodgroup = bloodgroup

class Robot(Human):
    def __init__(self, name, age, number, bloodgroup,imei):
        super().__init__(name, age, number, bloodgroup)
        self.imei = imei


obj1 = Animal("Lion",12)
obj2 = Human("Aman",21,81828277272,"B+")

obj2.info()


Multiple inheritence

class Animal:
    name = "Lion"

class Human:
    name = "Aman"

class Robots(Animal,Human):
    pass

Hierarchial Inheritence:

class Animal:
    pass

class Human(Animal):
    pass

class Robot(Animal):
    pass
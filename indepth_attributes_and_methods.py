class Animal:
    gender = "Male" #class Attribute : why : Because it is not using any object/instance.
    def __init__(self,name,age):
        self.name = name #instance attribute : why : because they are created using an instance or object.
        self.age = age #instance attribute

    # def speak():
    #     print("Lion is Roaring.")

    def info(self):  #instance method
        print("This is a method.")

    @classmethod
    def clsmethod(cls): #This is a class method
        print(f"{cls.gender} is your Gender.")

    @staticmethod
    def stmethod():
        print("Hello , I am a static method.")


obj = Animal("Lion",15)
obj.info()
obj.clsmethod()
obj.stmethod()
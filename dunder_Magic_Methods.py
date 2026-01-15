# class students:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def __str__(self):
#         return f"{self.name} is your name and {self.marks} is your marks."


# obj = students("Aman",79)

# print(obj)

# class Shopping:
#     def __init__(self,items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)
    
# obj = Shopping(["car" , "Milk","bread"])
# obj2 = Shopping(['apple','banana'])

# print(len(obj))
# print(len(obj2))


#     def result(self):
#         pass

# obj1 = Number(12)
# obj2 = Number(32)

# print(obj1.number + obj2.number)

#Method-2 : __add__
class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, custom):
        return self.number + custom.number


# creating objects
obj1 = Number(10)
obj2 = Number(20)

# adding objects
print(obj1 + obj2)

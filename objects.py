class Factory:
    a = 12 #attribute
    def hello(s): #method
        print("Hello")
    
obj = Factory()
print(obj.a)
obj2 = Factory()
obj2.hello()
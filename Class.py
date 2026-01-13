class Factory:
    a = 12 #attribute
    def hello(): #method
        print("Hello")
    
    print("I am getting Initialized") #class gets initialized only once

print(Factory.a)
Factory.hello()
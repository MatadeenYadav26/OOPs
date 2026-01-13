# class Factory:
#     def __init__(self):
#         print("Hello i will run no matter what!")

# Factory()

class Factory:
    def __init__(self,materials,zips,pockets):
        self.materials = materials
        self.zips = zips
        self.pockets = pockets
    
    def showdetails(self):
        print(self.materials,self.pockets,self.zips)

Reebok = Factory("Leather",3,3)
Campus = Factory("silk",2,3)

Campus.showdetails()
Reebok.showdetails()
#Learn How Super Class Constructor Run in Sub Class During Inheritance
class Uet(object):
    def __init__(self): #Parent Class Constructor
        self.departs=31
        print("Total Departments in UET",self.departs)
        print("UET is Public University")
        print("UET os 103 Years Old")
class Ibm(Uet):       #Child Class
    def show(self):
        print("IBM is Public Department")

a=Ibm() #Child Class Object 
#When We declare the Object of Child Class the Constructor of Child Class Run on this Spot by default
print("Parent Class Instance Variable",a.departs)
print()
a.show()
#Concept of Single Inheritance
class Uet(object): #Base/Super/Old/Father Class
    uetgate=5
    def show(self):
        print("UET is a Public University")
    @classmethod
    def clssmethod(cls):
        print("Total Gates",cls.uetgate)
    @staticmethod
    def sticmethod(m):
        print("The Total departments",m)
class Ibm(Uet): #Derived/Sub/new/child Class
    ibmhod="Dr.Nasir Malik"
    def disp(self):
        print("The IBM is Public department")
    @classmethod
    def showw(cls):
        print("The name of IBM Hod",cls.ibmhod)
    @staticmethod
    def views(n):
        print("UnderGraduate Programs in IBM",n)

a=Ibm() #Object of Derived/Sub/new/child Class that Access all the members of Base/Super/Old/Father Class 
print("Access Parent Class Members with the help of Child Class Object")
print("Run Base Class Variable with Derived class Name",Ibm.uetgate)
a.show()
a.clssmethod()
Ibm.clssmethod()
a.sticmethod(31)
print()
print("Access Child Class Members with the help of Child Class Object")
print("Run Derived Class variable with Derived Class Name",Ibm.ibmhod)
a.disp()
a.showw()
Ibm.showw()
a.views(2)
print()
print("Access Parent Class Members with the help of Parent Class Object")
b=Uet() #Object of Base/Super/Old/Father Class  
print(b.uetgate)
print(Uet.uetgate)
b.show()
b.clssmethod()
b.sticmethod(31)


    
    
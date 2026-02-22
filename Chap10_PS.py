#Problem 2

class Calculator:
    def __init__(self,value):
        self.val=value
        self.sq=value**2
        self.cube=value**3
        self.sq_root=value**0.5
c=Calculator(4)
print(f"The Solutions for {c.val}'s\nSquare is {c.sq}\ncube is {c.cube}\nand square root is {c.sq_root}")
#Works Perfectly YAYY!!

#Problem 3

class DEmo:
    a=99
o=DEmo()
print(o.a)#Prints 99(Class attribute) bcoz there is no instance attribute set rn
o.a=88#Setting instance attribute
print(o.a)#Prints 88(Instance attribute bcoz it has high priority)
print(DEmo.a)#The class attribute isnt changed so 99 here

#Problem 4
class Calculator:
    def __init__(self,value):
        self.val=value
        self.sq=value**2
        self.cube=value**3
        self.sq_root=value**0.5
    @staticmethod#To tell the compiler that this function below doesn't require 'self'
    def hello():
        print("Kya hal chal???")
m=Calculator(4)
print(f"The Solutions for {m.val}'s\nSquare is {m.sq}\ncube is {m.cube}\nand square root is {m.sq_root}")
m.hello()
#Done

#Problem 5(Bit hard)
'''from random import randint #to directly import
class Train:
    def __init__(self,t_id,fr,to):
        self.t_id=t_id
        self.fr=fr
        self.to=to
    def book(self):
        print(f"\nTicket booked in train no.:{self.t_id}\nFrom:{self.fr} to: {self.to}\n")
    def GetStatus(self):
        print(f"Train with train no.:{self.t_id} is running on time\n")
    def fare(self):
        print(f"\nTicket fare in train no.:{self.t_id}\nFrom:{self.fr} to: {self.to} is: {randint(1000,88888)}\n")

pok=Train(55,"Hyderabad","Vizag")
pok.book()
pok.GetStatus()
pok.fare()'''

#Self is not compulsury we can name it anything but for readability purposes we use 'self'
class Employee:
    Job_stat="General Worker"
    Salary=90000
    Floor_no=5
    def __init__(self,Name):#dunder method:Automatically called method everytime a new object is created!
    #Take the passed value and saves it in "self.name"
        print("I am ME")
        self.name=Name
    def fun(self):#Requires an argument 'self'
        print(f"\t\tPokmon trainer stat:{self.Job_stat} and salary={self.Salary}")
    @staticmethod#To make the comp know this function doesnt require an attribute
    def Hello():
        print("\n\t\t\tHello future Pokemon Master!\n")
# mujju=Employee()#init will run
# mujju.Hello()
# print("\n")
# mujju.fun()
# print("\n")
x=Employee("Xavier")#init will run and the given value will be recieved by init
print(x.name)
m=Employee("Magneto")#init will run
print(m.name)
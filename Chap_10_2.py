class Employee:
    Job_stat="General Worker"
    Salary=90000
    Floor_no=5
    def fun(self):#Requires an argument 'self'
        print(f"\t\tPokmon trainer stat:{self.Job_stat} and salary={self.Salary}")
    @staticmethod#To make the comp know this function doesnt require an attribute
    def Hello():
        print("\n\t\t\tHello future Pokemon Master!\n")
mujju=Employee()
mujju.Hello()
print("\n")
mujju.fun()
print("\n")

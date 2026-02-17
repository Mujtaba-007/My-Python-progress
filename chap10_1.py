class Employee:#'Employee' is a class
    Job_stat="General Worker"#Job_stat,Salary,Floor_no-> Class Attributes
    Salary=90000
    Floor_no=5
mujju=Employee()#'mujju' is an object here
mujju.name="Mujtaba Hussain"#instance/Object attribute!
print("\n")
print(mujju.name,"'s salary= ",mujju.Salary+10000,"\n")
#Instance attributes have high preference during assigning and retrieving data!!!
#ex:-
'''
class Employee:
    Job_stat="General Worker"Attributes
    Salary=90000
    Floor_no=5
mujju=Employee()
mujju.Floor_no=3
print(mujju.Floor_no)
This will simply print 3 instead of 5 bcoz Instance attributes have high preference than class attributes during assigning and retrieving data
'''
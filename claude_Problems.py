#this is me solving Claude AI given python problems till OOPs in python


#My answer for Q1(3/10)
'''def slugify(title):
    title(str.replace(" ","-"),str.replace("!",""))
    #I dont remember how to convert them to lower case nor do ik how to make the extra spaces go away
title="Hello World! This is Python"
slugify(title)
'''
#correct/Claude answer for Q1
'''
def slugify(title):
    return title.strip().lower().replace(" ", "-").replace("!", "")

title = input("Enter Text: ")#Made it an input based Q
print(slugify(title))  # hello-world-this-is-python
'''

#My answer for Q2(5/10)
'''pok=[120, 450, 30, 890, 210, 75]
for i in range (0,6):
    if(pok[i]>100):
        print(pok[i])'''
#Claude's answer for 2
'''
pok = [120, 450, 30, 890, 210, 75]
result = sorted([p for p in pok if p > 100], reverse=True)
print(result)  # [890, 450, 210, 120]
    
'''
#My Answer for Q3(1/10)
'''
users = [#Rewritten
  {"name": "Alice", "role": "admin"},
  {"name": "Bob", "role": "user"},
  {"name": "Carol", "role": "admin"}
]
grouped={}
for a in users:
    # role=a.role<--Mistake
    # name=a.name<--Mistake
#    if a[role] not in grouped[]:  <--Mistake
        grouped[role]=[]
    grouped[role].append(name)
'''  

#Answer 3 by claude.ai
'''
users = [
  {"name": "Alice", "role": "admin"},
  {"name": "Bob", "role": "user"},
  {"name": "Carol", "role": "admin"}
]

grouped = {}
for u in users:
    role = u["role"]
    name = u["name"]
    if role not in grouped:
        grouped[role] = []        # create the list if role seen for first time
    grouped[role].append(name)   # add name to that role's list

print(grouped)  # {"admin": ["Alice", "Carol"], "user": ["Bob"]}
'''

#My answer for Q4(4/10)
'''
def ping():
    print("Ping!")
def repeat(func, n):
    if(n==1):
        return func
    else:
        func
        return repeat(func,n-1)
        
repeat(ping(),9)
'''
#fix:
'''def ping():
    print("Ping!")
def repeat(func, n):
    if(n==1):
        return func()
    else:
        func()#Here braces are necessary as we want to call the function!
        return repeat(func,n-1)
        
repeat(ping,9) #If i put ping() then function isnt sent its called!.
'''
#Claude.ai shorted solution
'''
def repeat(func, n):
    for i in range(n):
        func()

repeat(ping, 9)'''


#My answer for Q5(3/10)
'''f=open("data.txt")
p=f.read()
print(p)
if f==-1:
    print("Error file not found")
b=f.readlines()
print(b)
f.close()'''

#Claude.ai given answer:
'''
try:
    with open("data.txt") as f:
        lines = f.readlines()
        print(len(lines))  # prints number of lines
except FileNotFoundError:
    print("Error: file not found")'''

#Question 6
class BankAccount:
    def __init__(self, owner):
        self.owner = owner    # store the owner's name
        self.balance = 0      # start with 0 balance
    def deposit(self, amount):
        self.balance += amount  # add to balance
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def __str__(self):
        return f"{self.owner}'s account: ₹{self.balance}"


# Testing it
acc = BankAccount("Alice")
print(acc)              # Alice's account: ₹0

acc.deposit(500)
print("Account after depositing 500rs: ",acc)              # Alice's account: ₹500

acc.withdraw(200)
print("Account after Withdrawing 200rs: ",acc)              # Alice's account: ₹300

acc.withdraw(400)       # Insufficient funds
print("Account after Withdrawing 400rs: ",acc)              # Alice's account: ₹300
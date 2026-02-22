#Problem 5(Bit hard)
from random import randint #to directly import
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
pok.fare()
#Parts of an Object Oriented Programming Language: Encapsulation, Abstraction, Inheritance and Polymorphism
#Puttng Object Oriented program in the form of a Pokemon
#Pikachu - [Pokemon(Class)], [Name, type, health-(Attributes)],[Attack(),dodge(),evolve()- methods]



class Football:
    def __init__(self,name,position,country):
        self.name=name
        self.position=position
        self.country=country
    
    def club(self):
        if self.name=="Messi":
            print(self.name,"-","Club:","FC Barcelona")
        elif self.name=="Ronaldo":
            print(self.name,"-","Club:","FC Juventus")

messi=Football("Messi","Attacking Midfielder","Argentina")
ronaldo=Football("Ronaldo","Forward","Portugal")

messi.club()
ronaldo.club()



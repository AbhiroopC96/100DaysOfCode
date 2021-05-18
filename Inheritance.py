class Company():
    def company_name(self):
        print("I work for ABC networks.")

class Employee(Company):
    def __init__(self):
        print("I am an Employee at ABC")
        self.floor="Floor-E"

class Manager(Company):
    def __init__(self):
        print("I am a manager at ABC")
        self.floor="Floor-M"


e=Employee()
#e.company_name()

#m=Manager()
#m.company_name()


print(isinstance(e,Company))

print(isinstance(e,Employee))

print(isinstance(e,Manager))

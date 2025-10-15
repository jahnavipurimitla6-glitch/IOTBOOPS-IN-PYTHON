class Employee:
    def __init__(self,name):
        self.name = name


    def display_name(self):
        print(self.name)

emp = Employee("Jahn")
emp.display_name()
print(emp.name)

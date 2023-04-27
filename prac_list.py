class Employee:


    empCount=0


    def __init__(self, name, salary):

        self.name=name
        self.salary=salary
        self.empCount += 0

    def displayCount(self):
        print("Total Employee %d" %Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name , "Salary:", self.salary)

emp1 = Employee("Hari","500000")
emp2 = Employee("Shyam","5000000")

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" %Employee.empCount)





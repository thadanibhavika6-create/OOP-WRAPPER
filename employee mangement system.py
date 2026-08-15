class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name)
        print("Age",self.age)

class Employee(person):
    def __init__(self,name,age,emp_id,salary):
        person.__init__(self,name,age)
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        person.display(self)
        print("Employee_id",self.emp_id)
        print("salary",self.salary)

class manger(Employee):
    def __init__(self,name,age,emp_id,salary,department):
        Employee.__init__(self,name,age,emp_id,salary)
        self.department=department
    def display(self):
        Employee.display(self)
        print("department",self.department)

# main program
person_obj=None
employee_obj=None
manager_obj=None

print("-------Python OOP Project: Employee mangament system-------")
print()
while True:
    print("Choose an Operation:")
    print("1.Create a Person")
    print("2.Create an Employee")
    print("3.Create a Manger")
    print("4.Show a Details")
    print("5.Exit")
    print()
    Choice=input("Enter your Choice:")
    print()
    if Choice=="1":
        name=input("Enter a name:")
        age=int(input("enter a age:"))
        print()
        person_obj=person(name,age)
        print(f"Person created with name:{name},and age:{age}")

        print()

        print("------Choose another Operation------")
        print()
    elif Choice=="2":
        print()
        name=input("Enter a name:")
        age=int(input("enter a age:"))
        emp_id=int(input("Enter a id:"))
        salary=int(input("Enter a Salary:"))
        employee_obj = Employee(name,age,emp_id,salary)
        print(f"Employee created with name:{name},age:{age},emp_id:{emp_id},and salary:{salary}")
        print("------Choose another Operation---")
    elif Choice=="3":
        name=input("Enter a name:")
        age=int(input("enter a age:"))
        emp_id=int(input("Enter a id:"))
        salary=int(input("Enter a Salary:"))
        department=input("Enter a Department:")
        manager_obj = manger(name,age,emp_id,salary,department)
        print(f"Manger created with name:{name},age:{age},emp_id:{emp_id},salary:{salary},Department:{department}")

        print("---Choose another Operation---")
    elif Choice=="4":
        print("Choose details to show:")
        print("1.Person")
        print("2.Employee")
        print("3.Manger")
        Choice=input("Enter your choice: ")
        if Choice=="1" and person_obj is not None:
            person_obj.display()
        elif Choice=="2" and employee_obj is not None:
            employee_obj.display()
        elif Choice=="3" and manager_obj is not None:
            manager_obj.display()
        else:
            print("Invalid Selection")

    elif Choice=="5":
        print("Exiting the program.All resources have been freed")
        print()
        print("Goodbye!")
        break
    else:
        print("Invalid choice,Please choose correct option")
        print()

    
       



        
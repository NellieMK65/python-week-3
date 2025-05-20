# One to Many
# Many to Many

# A department can have many employees
class Department:
    employees = []

    def __init__(self, name):
        self.name = name
        # instance attribute to store all employees related to the department
        Department.employees = []

    # instance method that can add an employee to the department
    def add_employee(self, employee):
        # store the employee instance inside the the employee list
        # self.employees.append(employee)
        Department.employees.append(employee)

    @classmethod
    def add_employees(cls, *args):
        for employee in args:
            Department.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee {self.name}"

classroom = Department("Classroom")
# mercy = Employee("Mercy")
# brian = Employee("Brian")
# james = Employee("James")
# evening_checkout = Employee("Kuria")
# classroom.add_employee(Employee("Mercy"))
# classroom.add_employee(Employee("Brian"))
# classroom.add_employee(Employee("James"))
# classroom.add_employee(Employee("Kuria"))

Department.add_employees(Employee("Mercy"), Employee("Brian"), Employee("James"), Employee("Kuria"), Employee("OpenAI"))

print("Classroom employees", Department.employees)

hr = Department("Human Resource")
johnson = Employee("Johnson")
mitchelle = Employee("Mitchelle")
hr.add_employee(johnson)
hr.add_employee(mitchelle)

print("HR department", Department.employees)

class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method -> behaviors
    def reading(self):
        print("read")

class Student(Person):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        super().__init__(name, age)

    # polymorphism -> overriding the parent methods
    def reading(self):
        print(f"Student with id {self.student_id} is reading")

student = Student("Brian", 20, 1)
student.reading()

class Parent(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def pay_fees(self):
        pass

parent = Parent("Jane", 39)
parent.reading()
parent.pay_fees()

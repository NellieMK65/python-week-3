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


# Many to Many (Student and Courses)

class Student:
    def __init__(self, name):
        self.name = name
        # this will be used to store a list of courses a student can do
        self.courses = []

    def enroll(self, course):
        # only course if it does not exist
        if course not in self.courses:
            self.courses.append(course)
            # add a reverse relationship
            course.students.append(self)
        # else:
        #     raise ValueError(f"Student {self.name} has is already enrolled to course {course.title}")



    def __repr__(self):
        return f"Student {self.name} has courses {[c.title for c in self.courses]}"


class Course:
    def __init__(self, title):
        self.title = title
        # this can be used to store all students that belong to a course
        self.students = []

    def __repr__(self):
        return f"Course {self.title} has students: {[s.name for s in self.students]}"

sd = Course("Software Engineering")
devops = Course("Devops")

eugene = Student("Eugene")
eugene.enroll(sd)
eugene.enroll(sd)
eugene.enroll(devops)

trevor = Student("Trevor")
trevor.enroll(devops)

print(eugene)
print(sd)
print(devops)


class Artist:
    all_artists = []

    def __init__(self, name):
        self.name = name
        self.albums = []
        self.all_artists.append(self)

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            album.artists.append(self)


    def __repr__(self):
        return f"Artist {self.name} has albums {[a.title for a in self.albums]}"

class Album:
    def __init__(self, title):
        self.title = title
        self.artists = []

    def get_all_artists(self):
        print(self.artists)

    def __repr__(self):
        return f"Album {self.title} by artists: {[a.name for a in self.artists]}"

artist = Artist("Kulindeezy")
artist2 = Artist("Beyonce")
artist3 = Artist("Ruth")
artist4 = Artist("Bett")
print("All artists", [a.name for a in Artist.all_artists])

album1 = Album("Cowboy carter")
# print(album1.get_all_artists())
album2 = Album("What a time to be alive")

album3 = Album("The book of jones")

artist.add_album(album1)
artist2.add_album(album1)
artist2.add_album(album2)

print(album1)
print(album2)
print(artist2)
print(artist)


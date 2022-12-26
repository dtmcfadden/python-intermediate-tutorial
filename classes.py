# Wonderful World of Object Oriented Python

school = {
    "name": "Hogwarts",
    "students": ["Harry Potter", "Draco Malfoy", "Luna Lovegood"],
    "courses": ["Potions", "Magical History", "Magical Creatures"],
    "coutnry": "United Kingdom"
}


class School:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.students = []
        self.courses = []

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("Can only add of type Course")
        self.courses.append(course)

    def enroll_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Can only enroll a type Student")
        self.students.append(student)

    @classmethod
    def can_enroll(cls, student):
        if student.age >= 12 and student.age <= 18:
            return True
        return False

    @property
    def teachers(self):
        teachers = set()
        for course in self.courses:
            teachers.add(course.teacher)
        return list(teachers)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, student_id, age):
        super().__init__(first_name, last_name)
        self.student_id = student_id
        self.age = age


class Teacher(Person):
    pass


class Course:
    def __init__(self, title, teacher, credits):
        self.title = title
        if not isinstance(teacher, Teacher):
            raise TypeError("Can only enroll a type Teacher")
        self.teacher = teacher
        self.credits = credits

    def __str__(self):
        return f"{self.title} - {self.teacher}"

    def __repr__(self):
        return f"{self.title} - {self.teacher}"

    def __lt__(self, other_course):
        return self.credits < other_course.credits

    def __gt__(self, other_course):
        return self.credits > other_course.credits


hogwarts = School(name="Hogwarts", country="United Kingdom")

# students
harry_potter = Student("Harry", "Potter", "234", 13)
draco_malfoy = Student("Draco", "Malfoy", "93284", 25)
hogwarts.enroll_student(harry_potter)
hogwarts.enroll_student(draco_malfoy)

# teachers
snape = Teacher("Severus", "Snape")
slughorn = Teacher("Horace", "Slughorn")

# courses
potions = Course("Potions", slughorn, 100)
magical_history = Course("Magical History", snape, 80)
hogwarts.add_course(potions)
hogwarts.add_course(magical_history)

print("Hogwarts Courses", hogwarts.courses)
print("Hogwarts Students", hogwarts.students)
print("Hogwarts Teachers", hogwarts.teachers)

print(School.can_enroll(harry_potter))
print(School.can_enroll(draco_malfoy))

print("potions < magical_history", potions < magical_history)
print("potions > magical_history", potions > magical_history)

# print(hogwarts.students)

# print(harry_potter)

# name = "Hogwarts"
# students = ["Harry Potter", "Draco Malfoy", "Luna Lovegood"]
# courses = ["Potions", "Magical History", "Magical Creatures"]
# coutnry = "United Kingdom"


# print(School.name)

# hogwarts = School()
# sports_school = School()

# print(hogwarts.courses)
# sports_school.name = "Sports School"
# print(sports_school.name)
# print(hogwarts.name)

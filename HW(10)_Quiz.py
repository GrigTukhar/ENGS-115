class Student:
    def __init__(self, name,code):
        self.name = name
        self.code = code
        self.courses = []

    def addCourse(self,name):
        new_course = Course(name)
        self.courses.append(new_course)

    def addAssignment(self,course,name,deadline):


class Course:
    def __init__(self,name):
        self.name = name
        self.assignments =[]

    def addAssignment(self,course,name,deadline):
        new_assignment = Assignment(name,deadline)
        self.assignments.append(new_assignment)

class Assignment:
    def __init__(self,name,deadline):
        self.name = name
        self.deadline = deadline
        self.grade = -1

def main():
    student = Student("Grigor Tukharyan","AUA-098")
    student.addCourse("ENGS115")



main()

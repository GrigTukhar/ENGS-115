class Student:
    def __init__(self, name,code):
        self.name = name
        self.code = code
        self.courses = []

    def addCourse(self,name):
        new_course = Course(name)
        self.courses.append(new_course)
        print(name ,"course has been added")

    def addAssignment(self,coursetitle,name,deadline):
        for course in self.courses:
            if course.name == coursetitle:
                course.addAssignment(name, deadline)
                print(name, "assignment has been added to course",coursetitle,"with a deadline of",deadline)

    def Grade(self, coursetitle, assignmenttitle, grade):
        for course in self.courses:
            if course.name == coursetitle:
                for assignment in course.assignments:
                    if assignmenttitle == assignment.name:
                        assignment.Grade(grade)
                        print(grade,"is the new grade for",assignmenttitle,"assignment in",coursetitle,"course")

    def getAssignGrade(self, coursetitle, assignmenttitle):
        for course in self.courses:
            if course.name == coursetitle:
                for assignment in course.assignments:
                    if assignment.name == assignmenttitle:
                        print("The grade for assignment",assignmenttitle,"in course",coursetitle,"is",assignment.grade)
                        return(assignment.grade)


    def getCourseGrade(self, coursename):
        for course in self.courses:
            if course.name == coursename:
                sum = 0
                for assignment in course.assignments:
                    sum = sum + self.getAssignGrade(course.name, assignment.name)
                grade = sum/len(course.assignments)
                print("The grade for the course", coursename,"is",grade)
                return(grade)

    def getFullGrade(self):
        sum = 0
        for course in self.courses:
            sum = sum + self.getCourseGrade(course.name)
        grade = sum/len(self.courses)
        print("The grade for all classes is", grade)



class Course:
    def __init__(self,name):
        self.name = name
        self.assignments =[]

    def addAssignment(self,name,deadline):
        new_assignment = Assignment(name,deadline)
        self.assignments.append(new_assignment)

class Assignment:
    def __init__(self,name,deadline):
        self.name = name
        self.deadline = deadline
        self.grade = -1

    def Grade(self, grade):
        self.grade = grade

def main():
    student = Student("Grigor Tukharyan","AUA-098")
    student.addCourse("ENGS115")
    student.addAssignment("ENGS115", "Project", "13/10/19")
    student.Grade("ENGS115", "Project", 90)
    student.getAssignGrade("ENGS115", "Project")
    student.getCourseGrade("ENGS115")
    student.getFullGrade()



main()

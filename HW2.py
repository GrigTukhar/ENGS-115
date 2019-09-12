class Student:

    def __init__(self,ID,firstName,lastName,phone,gender,birthdate,gradeHW,gradeParticipation,gradeQuiz,gradeFinal):
        self.ID = ID
        self.fullName = firstName +" "+lastName
        self.email = firstName +"." +lastName + "@aua.am"
        self.phone = phone
        self.gender = gender
        self.birthdate = birthdate
        self.gradeHW = gradeHW
        self.gradeParticipation = gradeParticipation
        self.gradeQuiz = gradeQuiz
        self.gradeFinal = gradeFinal

    def getPersonalInfo(self):
        print(self.ID)
        print(self.fullName)
        print(self.email)
        print(self.phone)
        print(self.gender)
        print(self.birthdate)
        print("__________________________")
    def getCurrentGrade(self):
        print(self.fullName)
        print("HW: ",self.gradeHW,"%")
        self.gradeHW = (self.gradeHW*0.15)
        print("Participation: ",self.gradeParticipation,"%")
        self.gradeParticipation = (self.gradeParticipation*0.15)
        print("Quiz: ", self.gradeQuiz,"%")
        self.gradeQuiz = (self.gradeQuiz*0.30)
        print("Final: ", self.gradeFinal,"%")
        self.gradeFinal = (self.gradeFinal*0.40)
        self.fullGrade = round(self.gradeHW+self.gradeQuiz+self.gradeParticipation+self.gradeFinal)
        print("Full Grade: ",self.fullGrade,"%")
        print("__________________________")

def main():
    st1 = Student("AUA123", "Gor", "Isoyan", 123456, "M", "01/01/2019", 90, 85, 93, 50)
    st2 = Student("AUA456", "Ani", "Zadikian", 654321, "F", "01/01/2018", 56, 79, 91, 85)

    st1.getPersonalInfo()
    st2.getPersonalInfo()

    st1.getCurrentGrade()
    st2.getCurrentGrade()

main()

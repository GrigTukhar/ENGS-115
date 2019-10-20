class Node:
    def __init__(self, name,gpa):
        self.name = name
        self.gpa = gpa
        self.next = None

class Student:
    def __init__(self):
        self.__head=None
        self.items=0

    def setHead(self, name,gpa):
        self.items += 1
        self.__head=Node(name,gpa)

    def display(self):
        print("\nShowing all Students:")
        printval = self.__head
        while printval is not None:
            print(printval.name,printval.gpa)
            printval=printval.next

    def append(self,name,gpa):
        self.items += 1
        temp = self.__head
        while temp.next is not None:
            temp = temp.next
        newDay = Node(name,gpa)
        temp.next = newDay

    def addAtBeginning(self,name,gpa):
        self.items += 1
        newDay = Node(name,gpa)
        newDay.next = self.__head
        self.__head = newDay

    def highGPA(self):
        print("\nShowing all Students with a GPA higher than 3.4:")
        printval = self.__head
        while printval is not None:
            if printval.gpa >= 3.4:
                print(printval.name, printval.gpa)
            printval = printval.next

    '''def sortList(self):
        n = self.items
        for i in range(n):
            old_temp=self.__head
            if old_temp !=0:
                for z in range(i):
                    old_temp = old_temp.next
            max = old_temp
            temp = old_temp
            for b in range(i+1,n):
                temp = temp.next
                if max.gpa<temp.gpa:
                    max = temp
            print(max.gpa)
            if i == n-1:
                max_temp = max
                old_temp.next = None
            elif i==1:
                max_temp = max
                self.__head = max
                max= max_temp
            else:
                max_temp = max
                old_temp= max
                max.next = max_temp
'''



def main():
    students = Student()
    students.setHead("Grigor",4.0)
    students.append("Erik",2.0)
    students.append("David", 3.5)
    students.addAtBeginning("Gor",3.0)
    students.display()
    students.highGPA()
    #students.sortList()
    #students.display()


main()

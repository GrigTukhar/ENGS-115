class Classroom:

    classroomIDs =[]

    def  __init__(self, roomnumber, numberofseats):
        Classroom.classroomIDs.append(roomnumber)
        self.roomnumber = roomnumber
        self.numberofseats = numberofseats
        self.schedule = []

    def getClassRoomInfo(self):
        print("Room Number: ",self.roomnumber)
        print("Number of Seats: ",self.numberofseats)

    def isValid(self, start, end):
        for key in self.schedule:
            if not(end < key["start"] or start > key["end"]):
                return False
        return True

    def reserve(self, start, end):
        if(self.isValid(start,end)):
            timeslot ={"start":start,"end":end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @classmethod
    def getAvailableRooms(cls):
        return str.join(",", cls.classroomIDs)

    @staticmethod
    def isValidSlot(start,end):
        return start<end

def main():
    r1 = Classroom("201E PAB",40)
    r2 = Classroom("314W PAB", 50)
    r3 = Classroom("114W PAB", 30)

    while True:
        chosenID = input("Choose a classroom to reserve ("+Classroom.getAvailableRooms()+"): ")
        if chosenID == r1.roomnumber:
            chosenclass = r1
            break
        elif chosenID == r2.roomnumber:
            chosenclass = r2
            break
        elif chosenID == r3.roomnumber:
            chosenclass = r3
            break
        else:
            print("This classroom does not exist, try again")

    choice ="x"
    while choice != "no":
        choice = input("Would you like to add to schedule (yes, no): ")
        if choice == "yes":
            start = int(input("Please enter the start time: "))
            end = int(input("Please enter the end time: "))
            while not Classroom.isValidSlot(start,end):
                print("Invalid slot, please try again")
                start = int(input("Please enter the start time: "))
                end = int(input("Please enter the end time: "))
            while not(chosenclass.reserve(start,end)):
                print("This time interval is booked, choose another")
                start = int(input("Please enter the start time: "))
                end = int(input("Please enter the end time: "))

            print("Reserved from",start,"to",end)
        elif choice =="no":
            print("Thank you for using openroom.am, here is your schedule for",chosenclass.roomnumber,":")
        else:
            print("Invalid input, please try again")
    print(chosenclass.schedule)

main()

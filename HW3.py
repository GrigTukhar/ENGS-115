class Classroom:

    def  __init__(self, roomnumber, numberofseats):
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

def main():
    r1 = Classroom(201,40)
    choice ="x"
    while choice != "no":
        choice = input("Would you like to add to schedule (yes, no): ")
        if choice == "yes":
            start = int(input("Please enter the start time: "))
            end = int(input("Please enter the end time: "))

            while not(r1.reserve(start,end)):
                print("This time interval is booked, choose another")
                start = int(input("Please enter the start time: "))
                end = int(input("Please enter the end time: "))
        elif choice =="no":
            print("Thank you for using openroom.am")
        else:
            print("Invalid input, please try again")
    print(r1.schedule)

main()

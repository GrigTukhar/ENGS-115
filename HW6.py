class Room:

    roomIDs = {}
    roomsbyType = []

    def __init__(self,type, roomID, capacity):
        self.capacity = capacity
        self.roomID = roomID
        self.type = type
        Room.roomIDs[roomID] = self
        Room.roomsbyType.append(self)

    def print(self):
        print(self.type,":", self.roomID, ", capacity:", self.capacity)

    @classmethod
    def getRoomByType(cls, type):
        for room in cls.roomsbyType:
            if room.type == type:
                room.print()

    @classmethod
    def getRoomById(cls, ID):
        if ID in cls.roomIDs:
            return cls.roomIDs[ID]
        print("The room cannot be found")
        return False

class Classroom(Room):

    type = "classroom"

    def __init__(self, capacity, roomID):
        super().__init__(Classroom.type, capacity, roomID)
        self.schedule = []

    def Reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break

        return is_free


    def getAvailableClassRooms(cls):
        ids = []
        for key in cls.classrooms:
            ids.append(key)
        return str.join(",", ids)


    @staticmethod
    def isValidSlot(start, end):
        return start < end


class Office(Room):

    type = "office"

    def __init__(self, capacity, roomID):
        super().__init__(Office.type, capacity, roomID)
        self.faculty = []

    def ReserveOffice(self, firstname, lastname):
        fullname = firstname + " " + lastname
        self.faculty.append(fullname)

def main():

    Classroom("208E PAB", 60)
    Classroom("314W PAB", 30)
    Office("114W PAB", 40)
    Office("118W PAB", 40)


    Room.getRoomByType("classroom")
    while True:
        Room.getRoomByType(Classroom.type)
        Room.getRoomByType(Office.type)

        ID = input("\nPlease enter either the ID of the room, or exit: ")
        if ID in Room.roomIDs.keys():
            currRoom = Room.getRoomById(ID)
            if currRoom.type == Classroom.type:
                x="x"
                while  x!= "no":
                    print("The schedule for", currRoom.roomID, ": ", currRoom.schedule)
                    x = input("Would you like to reserve? (yes,no): ")
                    if(x =="yes"):
                        start = int(input("Please insert the start time: "))
                        end = int(input("Please insert the end time: "))
                        if Classroom.isValidSlot(start, end):
                            if Classroom.isFree(currRoom, start, end) == False:
                                print("This time interval is booked, choose another")
                            else:
                                Classroom.Reserve(currRoom, start, end)
                        else:
                            print("Invalid slot, please try again")
                    elif (x == "no"):
                        break
                    else:
                        print("Please try again")

            elif currRoom.type == Office.type:
                y = 0
                if y < currRoom.capacity:
                    x="x"
                    while x != "no":
                        print("The faculty of the office", currRoom.roomID, ": ", currRoom.faculty)
                        x =input("Would you like to reserve? (yes,no): ")
                        if x =="yes":
                            firstname = input("please insert your first name: ")
                            lastname = input("please insert your last name: ")
                            Office.ReserveOffice(currRoom, firstname, lastname)
                        elif (x == "no"):
                            break
                        else:
                            print("Please try again")
                if y == currRoom.capacity:
                    print("The office is full, try another office")
        elif ID == 'exit':
            break
        else:
            print("No such room exists")

main()

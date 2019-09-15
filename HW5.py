class Room:

    rooms = {}

    def __init__(self, capacity, roomID):
        self.capacity = capacity
        self.roomID = roomID
        self.schedule = []
        Room.rooms[roomID] = self
        print(Room.rooms)

    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break

        return is_free

    def Reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @classmethod
    def getAvailableRooms(cls):
        ids = []
        for key in cls.rooms:
            ids.append(key)
        return str.join(",", ids)

    @classmethod
    def getRoomById(cls, ID):
        if ID in cls.rooms.keys():
            return cls.rooms[ID]
        print("The room cannot be found")
        return False

    @classmethod
    def getCurrentScheduleOfAllRooms(cls):
        for key in cls.rooms:
            currRoom = cls.rooms[key]
            print(currRoom.roomID)
            print("Capacity:",currRoom.capacity)
            print("Schedule:",currRoom.schedule,"\n")

    @staticmethod
    def isValidSlot(start, end):
        return start < end

class Classroom(Room):

    classrooms = {}
    def __init__(self, capacity, roomID):
        super(Classroom).__init__(capacity, roomID)

    def getAvailableClassRooms(cls):
        ids = []
        for key in cls.classrooms:
            ids.append(key)
        return str.join(",", ids)

    def getTheSubject(self):
        currSubject = input("Please enter the subject: ")
        return currSubject


class Office(Room):

    offices = {}
    def __init__(self, capacity, roomID):
        super(Office).__init__(capacity, roomID)

    def getAvailableOffices(cls):
        ids = []
        for key in cls.offices:
            ids.append(key)
        return str.join(",", ids)

    def getTeacher(self):
        currTeacher = input("Please enter Teacher's name: ")
        return currTeacher

def main():

    Classroom(60, "208E PAB")
    Classroom(30, "314W PAB")
    Office(40, "114W PAB")
    Office(40, "118W PAB")

    print("Hello, here you can reserve a classroom. Available IDs are:\n", Classroom.getAvailableRooms(),"\n")

    while True:

        Classroom.getCurrentScheduleOfAllRooms()

        classroomID = input("Please select a room ID from above")
        currClassroom = Classroom.getRoomById(classroomID)

        start = int(input("Please insert the starting time"))
        end = int(input("Please insert the ending time"))

        if (Classroom.isValidSlot(start, end)):
            if currClassroom.isFree(start, end) == False:
                print("Not available for ", currClassroom.roomID)
            else:
                currClassroom.Reserve(start, end)
                print("You just reserved the classroom", currClassroom.roomID, " from ", start, " to ", end)

                print(currClassroom.schedule)

        else:
            print("The slot is invalid")

main()

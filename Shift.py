import Resident

class Shift:
    
    day = "Day"
    shortCall = "ShortCall"
    night = "Night"
    allShifts = [day, shortCall, night]
    
    def __init__(self, time, residentsAvailable):
        self.time = time
        self.residentAssigned = Resident.Resident("Unassigned", "PGY0")
        self.residentsAvailable = residentsAvailable[:]

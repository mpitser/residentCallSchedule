import Resident

class Shift:
        
    def __init__(self, time, residentsAvailable):
        self.time = time
        self.residentAssigned = Resident.Resident("Unassigned", "PGY0")
        self.residentsAvailable = residentsAvailable[:]

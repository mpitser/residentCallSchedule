class Resident:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.vacationDays = []
        self.offserviceMonths = []
        
    def addVacationDays(self, vacationDays):
        self.vacationDays = vacationDays
        
    def addOffserviceMonths(self, offserviceMonths):
        self.offserviceMonths = offserviceMonths

class Resident:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.vacationDays = []
        self.offserviceMonths = []
        self.monthsWithVacation = [] # Months in which a vacation day is taken
        
    def addVacationDays(self, vacationDays):
        self.vacationDays = vacationDays
        
    def addOffserviceMonths(self, offserviceMonths):
        self.offserviceMonths = offserviceMonths
        
    def addMonthWithVacation(self, monthWithVacation):
        self.monthsWithVacation.append(monthWithVacation)

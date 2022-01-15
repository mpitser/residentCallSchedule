import Day
import Shift
import Resident
import datetime

#inputs: CSV file with resident names, vacation dates, off service months, PGY
#        CSV file with shifts and days
#preset parameters: Friday availability, weeks of night float, chunk size of night float, divide holidays evenly

#import CSV files and make data structures
def main():
    print "Welcome to the Resident Call Schedule Generator!"
    importFromCSV()
    
    # Get this info from CSV:
    res1 = Resident.Resident("Res1", "PGY1")
    res1.addOffserviceMonths(["October", "March"])
    res1.addVacationDays([datetime.date(2023, 6, 30)])
    res2 = Resident.Resident("Res2", "PGY2")
    res3 = Resident.Resident("Res3", "PGY3")
    allResidents = [res1, res2, res3]
    startDate = datetime.date(2022, 7, 1)
    endDate = datetime.date(2023, 6, 30)
    
    dates = makeListOfDates(startDate, endDate, allResidents)
    updateAvailability(dates, allResidents)
    assignHolidays()
    assignNightFloat()
    assignFridays()
    assignOpenShifts()
    exportToCSV()
    
    #PRINT AVAILABILITY
    for date in dates:
       for shift in date.shifts:
            print date.day, shift.time, shift.residentAssigned.name, shift.residentsAvailable[0].name
    
    return

#import data from CSV files
def importFromCSV():
    print "Importing data from CSV files"
    return
    
def makeListOfDates(startDate, endDate, residents):
    print "Making list of all shift dates"
    
    
    allDates = []
    currentDay = startDate
    
    # Add all dates between Start and End dates
    while True:
        shifts = [Shift.Shift("Day", residents), Shift.Shift("ShortCall", residents), Shift.Shift("Night", residents)]
        allDates.append(Day.Day(currentDay, shifts))
        currentDay += datetime.timedelta(days=1)
        if currentDay > endDate:
            break
    return allDates
    
#Update Availability
def updateAvailability(dates, residents):
    print "Updating resident availability"
   
    # remove vacation days
    for date in dates:
        for resident in residents:
            #print "Checking if", resident.name, "can work on", date.day
            for vacationDay in resident.vacationDays:
                if vacationDay == date.day:
                    print "it's a vacation"
                    for shift in date.shifts:
                        for residentAvailable in shift.residentsAvailable:
                            if residentAvailable.name == resident.name:
                                shift.residentsAvailable.remove(residentAvailable)
                                print "removing", residentAvailable.name
    #remove offservice months
    #remove Fridays for PGY1s
    return

#assign holidays
def assignHolidays():
    print "Assigning Holidays"
    return
    
#assign night float
def assignNightFloat():
    print "Assigning Night Float"
    return
    
#assign Fridays
def assignFridays():
    print "Assigning Fridays"
    return

#divide the rest evenly
def assignOpenShifts():
    print "Assigning all open shifts"
    return

#export data to a CSV file
def exportToCSV():
    print "Exporting data to CSV file"
    return

main()

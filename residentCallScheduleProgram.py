import Day
import Shift
import Resident
import Month
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
    #assignNightFloat(allResidents, dates)
    assignFridays()
    assignOpenShifts()
    exportToCSV()
    
    #PRINT AVAILABILITY
    #for date in dates:
    #for shift in date.shifts:
    #print date.day, shift.time, shift.residentAssigned.name, [availableResident.name for availableResident in shift.residentsAvailable]
    
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

def removeResidentFromShifts(date, resident, shiftsToRemove):
    for shift in date.shifts:
        for residentAvailable in shift.residentsAvailable:
            if residentAvailable.name == resident.name and shift.time in shiftsToRemove:
                shift.residentsAvailable.remove(residentAvailable)
                #print "removing", residentAvailable.name
 
#Update Availability
def updateAvailability(dates, residents):
    print "Updating resident availability"
   
    for date in dates:
        for resident in residents:
        
            # remove vacation days
            for vacationDay in resident.vacationDays:
                if vacationDay == date.day:
                    print "it's a vacation"
                    removeResidentFromShifts(date, resident, Shift.Shift.allShifts)
                    resident.addMonthWithVacation(date.day.strftime("%B"))
                    
            #remove offservice months
            for offserviceMonth in resident.offserviceMonths:
                if date.day.strftime("%B") == offserviceMonth:
                    print "it's an offservice month"
                    removeResidentFromShifts(date, resident, Shift.Shift.allShifts)
                    
            #remove Fridays for PGY1s
            if resident.year == "PGY1":
                if date.day.strftime('%A') == "Friday":
                    print "it's a PGY1 Friday."
                    removeResidentFromShifts(date, resident, [Shift.Shift.night])
                    
    return

#assign holidays
def assignHolidays():
    print "Assigning Holidays"
    return
    
#assign night float
def assignNightFloat(residents, dates):
    print "Assigning Night Float"
    
    # make a list of who is available for certain months
    months = [Month.Month("January", residents), Month.Month("February", residents), Month.Month("March", residents), Month.Month("April", residents), Month.Month("May", residents), Month.Month("June", residents), Month.Month("July", residents), Month.Month("August", residents), Month.Month("September", residents), Month.Month("October", residents), Month.Month("November", residents), Month.Month("December", residents)]
    
    #Remove resident if they are offservice OR they have a vacation during the month
    for resident in residents:
        for month in months:
            if month.month in resident.offserviceMonths:
                print resident.name, "is offservice in", month.month
                month.residentsAvailable.remove(resident)
            elif month.month in resident.monthsWithVacation:
                print resident.name, "has vacation time in", month.month
                month.residentsAvailable.remove(resident)
    #for month in months:
        #print [residentAvailable.name for residentAvailable in month.residentsAvailable]
    
    
    
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

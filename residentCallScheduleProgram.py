import Day
import Shift
import datetime

#inputs: CSV file with resident names, vacation dates, off service months, PGY
#        CSV file with shifts and days
#preset parameters: Friday availability, weeks of night float, chunk size of night float, divide holidays evenly

#import CSV files and make data structures
def main():
    print "Welcome to the Resident Call Schedule Generator!"
    importFromCSV()
    
    # Get this info from CSV:
    startDate = datetime.date(2022, 7, 1)
    endDate = datetime.date(2023, 6, 30)
    dates = makeListOfDates(startDate, endDate)
    #for date in dates:
    #   for shift in date.shifts:
    #        print date.day, shift.time, shift.resident
    
    assignHolidays()
    assignNightFloat()
    assignFridays()
    assignOpenShifts()
    exportToCSV()
    return

#import data from CSV files
def importFromCSV():
    print "Importing data from CSV files"
    return
    
def makeListOfDates(startDate, endDate):
    print "Making list of all shift dates"
    
    allDates = []
    currentDay = startDate
    
    # Add all dates between Start and End dates
    while True:
        shifts = [Shift.Shift("Day", "Unassigned"), Shift.Shift("ShortCall", "Unassigned"), Shift.Shift("Night", "Unassigned")]
        allDates.append(Day.Day(currentDay, shifts))
        currentDay += datetime.timedelta(days=1)
        if currentDay > endDate:
            break
    return allDates
    
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

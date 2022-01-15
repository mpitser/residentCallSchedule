#!/usr/bin/env python3
import Day
import datetime

#inputs: CSV file with resident names, vacation dates, off service months, PGY
#        CSV file with shifts and days
#preset parameters: Friday availability, weeks of night float, chunk size of night float, divide holidays evenly

#import CSV files and make data structures
def main():
    print "Welcome to the Resident Call Schedule Generator!"
    importFromCSV()
    
    # Get this info from CSV:
    startDate = datetime.datetime(2022, 7, 1)
    endDate = datetime.datetime(2023, 6, 30)
    makeListOfDates(startDate, endDate)
    
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
    allDates.append(startDate)
    allDates.append(endDate)
    
    for date in allDates:
        print date
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

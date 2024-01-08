# Importing os and csv so we can read csv file "budget_data.csv"
import os
import csv
import pandas as pd

# Set path to csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Translates the file into a readable format to be used by python
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
# Reads the first row of headers and prints the headers as actual headers in the output
    csv_header = next(csvreader)

#Lists to store values 
    date = []
    newDate = []
    newStringVal = []
    avgList = []
# Reads each row of data after the header
    for row in csvreader:
        # Add data to the new list(it is printed as a string so you have to convert later)
        newStringVal.append(row[1])
        # Add data to the date array(Will stay a String)
        date.append(row[0]) 

#Supposed to print to the txt file.
file = 'Analysis/analysis.txt'
with open(file, 'w', newline = '') as txt_file:  
    txt_file.write("This is an entry")
#Print header to output 
    print("Financial Analysis")
    txt_file.write("Financial Analysis")
    print("-------------------")
    txt_file.write("-------------------")

# Count the months in date.
    print(f'Total Months:    {len(date)}')
# Create a newintlist to store integer values from String list
NewIntList = [eval(i) for i in newStringVal]
# Add all values together and print total
totalprofits = sum(NewIntList)
# Print Total Profits
print("Total:           $",totalprofits)
# Calculate differences between values in newIntList. This iterates through the list and finds the difference btwn adjacent vals
avgList = [NewIntList[i+1] - NewIntList[i] for i in range(len(NewIntList)-1)]
# Declare a variable for the average change
AvgChng = sum(avgList)/len(avgList)
# Print into the Terminal and round to cents
print(f'Average Changes: $, {round(AvgChng, 2)}')


# Zipped lists into summary with variables date and NewIntList
summary =  list(zip(date, NewIntList))
# For loop that will append into newDate , but skipping the first value
for i in range(1, len(summary)):
    newDate.append(date[i])
# Zipped list into new summary with variables newDate and avgList
newSummary = list(zip(newDate, avgList))
# Sets a variable to call the newDate key separate from the avgList Key, but still attached to max/min.
maxSummary = max(newSummary, key=lambda x: x[1])
minSummary = min(newSummary, key = lambda x: x[1])
# FINAL PRINT LINES
print(f"Greatest Increase in Profits: {maxSummary[0]}, ${max(avgList)}")
print(f"Greatest Decrease in Profits: {minSummary[0]}, ${min(avgList)}")

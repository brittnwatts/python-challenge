# Importing os and csv so we can read csv file "budget_data.csv"
import os
import csv
import pandas as pd

# Set path to csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
# Reads the first row of headers and skips the first row
    csv_header = next(csvreader)
# Set file path for txt
    analysis_file = ("Analysis\PyBank_analysis.txt")
#Lists to store values 
    date = []
    newDate = []
    newStringVal = []
    avgList = []
# opens file path and determines that code must be run while open so it will print the output to txt_file
    with open(analysis_file, 'w', newline = '') as txt_file:  
        txt_file.write(f"\nFinancial Analysis\n\n")
        txt_file.write(f"-------------------------\n\n")
    # For row in csv reader, do calculations and print to terminal and txt_file
        for row in csvreader:
        # Add data to the new list(it is printed as a string so you have to convert later)
            newStringVal.append(row[1])
        # Add data to the date array(Will stay a String)
            date.append(row[0]) 
#Print header to output 
        print(f"\nFinancial Analysis\n")
        print(f"-----------------------\n")
# Count the months in date.
        print(f'Total Months: {len(date)}\n')
        txt_file.write(f'Total Months: {len(date)}\n\n')
# Create a newintlist to store integer values from String list
        NewIntList = [eval(i) for i in newStringVal]
# Add all values together and print total
        totalprofits = sum(NewIntList)
# Print Total Profits
        print(f"Total: ${totalprofits}\n")
        txt_file.write(f'Total: ${totalprofits}\n\n')
# Calculate differences between values in newIntList. This iterates through the list and finds the difference btwn adjacent vals
        avgList = [NewIntList[i+1] - NewIntList[i] for i in range(len(NewIntList)-1)]
# Declare a variable for the average change
        AvgChng = sum(avgList)/len(avgList)
# Print into the Terminal and round to cents
        print(f'Average Changes: ${round(AvgChng, 2)}\n')
        txt_file.write(f'Average Changes: ${round(AvgChng, 2)}\n\n')
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
# FINAL PRINT LINES!!!!!
        print(f"Greatest Increase in Profits: {maxSummary[0]} (${max(avgList)})\n")
        print(f"Greatest Decrease in Profits: {minSummary[0]} (${min(avgList)})\n")
        txt_file.write(f"Greatest Increase in Profits: {maxSummary[0]} (${max(avgList)})\n\n")
        txt_file.write(f"Greatest Decrease in Profits: {minSummary[0]} (${min(avgList)})")
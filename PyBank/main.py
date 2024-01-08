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

#Lists to store headers "Date" and "Profit/Losses"
    date = []
    profit = []
    losses = []
    newStringVal = []
    avgList = []
# Reads each row of data after the header
    for row in csvreader:
        # Add data to the new list
        newStringVal.append(row[1])
        # Add data to the date array
        date.append(row[0]) 

file = 'Analysis/analysis.txt'
with open(file, 'w', newline = '') as txt_file:  
    txt_file.write("This is an entry")

#Print header to output 
    print("Financial Analysis")
    txt_file.write("Financial Analysis")
    print("-------------------")
    txt_file.write("-------------------")
# count the months in date.
    print(f"Total Months:     ",len(date))
    txt_file.write(f"Total Months:     ",len(date))

#Create a new list to store integer values from String list
NewIntList = [eval(i) for i in newStringVal]
#add all values together and print total
totalprofits = sum(NewIntList)
#calculate differences between values in newIntList
avgList = [NewIntList[i+1] - NewIntList[i] for i in range(len(NewIntList)-1)]

#print Total Profits
print("Total:           $",totalprofits)
txt_file.write("Total:           $",totalprofits)
# Declare a variable for the average change
AvgChng = sum(avgList)/len(avgList)
# Print into the Terminal
print(f"Average Changes: $", round(AvgChng, 2))
txt_file.write(f"Average Changes: $", round(AvgChng, 2))


# Print max of difference list


newDate = []
# Zipped lists into summary   

summary =  list(zip(date, newDate, avgList, NewIntList))
#print originall summary
for date in summary:
    for i in date[0]:
        newDate.append[date[i+1]]
        print(newDate)
print(f"Max of diff list: $", newDate, max(avgList))
txt_file.write
# Print min of difference list
print(f"Min of diff list: $", newDate, min(avgList))
txt_file.write
#For loop
#for avgList in summary:
    #max_Val = max(summary)
    #min_Val = min(summary)
    #max_Val = max(summary, key=lambda x: x[1])
    #min_Val = min(summary, key=lambda x: x[1])
#find the greatest increase in profits and print with the date attached
#print(f"Greatest increase in profits:", max_Val)
#find the greatest decrease in profits and print with the date attached
#print(f"Greatest decrease in profits:", min_Val)
#print(max_Val)
#print(min_Val)



# Printing results into a text file.

#open a txt file for writing
    

# Importing os and csv so we can read csv file "budget_data.csv"
import os
import csv
import pandas as pd

# Set path to csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Translates the file into a readable format to be used by python
with open (csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
# Reads the first row of headers and prints the headers as actual headers in the output
    csv_header = next(csvreader)

#Lists to store headers "Date" and "Profit/Losses"
    date = []
    profit = []
    losses = []
    newStringVal = []
    summary =[]
    avgList = []
# Reads each row of data after the header
    for row in csvreader:
        # Add data to the new list
        newStringVal.append(row[1])
        # Add data to the date array
        date.append(row[0]) 

#Print header to output 
print("Financial Analysis")
print("-------------------")
# count the months in date.
print(f"Total Months:     ",len(date))


#Create a new list to store integer values from String list
NewIntList = [eval(i) for i in newStringVal]
#add all values together and print total
totalprofits = sum(NewIntList)
#calculate differences between values in newIntList
avgList = [NewIntList[i+1] - NewIntList[i] for i in range(len(NewIntList)-1)]
print(avgList)

#print Total Profits
print("Total:           $",totalprofits)

# Declare a variable for the average change
AvgChng = sum(avgList)/len(avgList)
# Print into the Terminal
print(f"Average Changes: $", round(AvgChng, 2))



# Print max of difference list
print(f"Max of diff list: $", max(avgList))
# Print min of difference list
print(f"Min of diff list: $", min(avgList))
# Zipped lists into summary   

summary =  list(zip(date, avgList))
#print originall summary
print(summary)


#For loop
for avgList in summary:
    max_Val = max(summary)
    min_Val = min(summary)
#find the greatest increase in profits and print with the date attached
print(f"Greatest increase in profits:", max_Val)
#find the greatest decrease in profits and print with the date attached
print(f"Greatest decrease in profits:", min_Val)


        
        
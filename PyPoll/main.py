import os
import csv
import pandas as pd

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
# Create open lists to store items
    ballotID = []
    county = []
    candidate = []
    # Declare variables to do if then checks
    stockham = 'Charles Casper Stockham'
    degette = "Diana DeGette"
    doane = "Raymon Anthony Doane"
# For loop for iterating through rows in CSV file
    for row in csvreader:
        # Append lists with csv data so you can work with it
        ballotID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
file = 'Analysis/analysis.txt'
with open(file, 'w', newline = '') as txt_file:  
    txt_file.write("This is an entry")
# Create a variable to count the number of votes and print
countRow = len(ballotID)
print("Election Results")
print("----------------------------")
print(f"Total Votes:   ", countRow)
print("----------------------------")

#Candidates if statements to check the length of their votes compared to the length of the whole
total = len(candidate)
count = candidate.count(stockham)
if count > 0:
    percentage = round(((count/total) * 100), 3)
    print(f'{stockham}: {percentage}% ({count})')
# Separate if statement where count now = count of DeGette
count = candidate.count(degette)
if count > 0:
    percentage = round(((count/total) * 100), 3)
    print(f'{degette}: {percentage}% ({count})')
# "", but with Doane
count = candidate.count(doane)
if count > 0:
    percentage = round(((count/total) * 100), 3)
    print(f'{doane}: {percentage}% ({count})')

print("----------------------------")

# This sets variables to candidate count based off of the candidates name
winnerStockham = candidate.count(stockham)
winnerDeGette = candidate.count(degette)
winnerDoane = candidate.count(doane)
# If statement that compares the count of their names through winner varaible.
if winnerStockham > winnerDeGette and winnerStockham > winnerDoane:
    print("Winner: Charles Casper Stockham")
elif winnerDeGette > winnerStockham and winnerDeGette > winnerDoane:
    print("Winner: Diana DeGette")
elif  winnerDoane > winnerDeGette and winnerDoane > winnerStockham:
    print("Winner: Raymon Anthony Doane")
print("----------------------------")
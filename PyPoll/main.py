import os
import csv
import pandas as pd

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    ballotID = []
    county = []
    candidate = []

    stockham = 'Charles Casper Stockham'
    degette = "Diana DeGette"
    doane = "Raymon Anthony Doane"

    for row in csvreader:
        #create lists
        ballotID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
file = 'Analysis/analysis.txt'
with open(file, 'w', newline = '') as txt_file:  
    txt_file.write("This is an entry")

countRow = len(ballotID)
#Beginning format
print("Election Results")
print("----------------------------")
print(f"Total Votes:   ", countRow)
print("----------------------------")

#Candidates 
total = len(candidate)

count = candidate.count(stockham)
if count > 0:
    percentage = round(((count/total) * 100), 3)
    print(f'{stockham}: {percentage}% ({count})')

count = candidate.count(degette)
if count > 0:
    percentage = round(((count/total) * 100), 3)
    print(f'{degette}: {percentage}% ({count})')

count = candidate.count(doane)
if count > 0:
    percentage = round(((count/total) * 100), 3)
    print(f'{doane}: {percentage}% ({count})')

print("----------------------------")

winnerStockham = candidate.count(stockham)
winnerDeGette = candidate.count(degette)
winnerDoane = candidate.count(doane)

if winnerStockham > winnerDeGette and winnerStockham > winnerDoane:
    print("Winner: Charles Casper Stockham")
elif winnerDeGette > winnerStockham and winnerDeGette > winnerDoane:
    print("Winner: Diane DeGette")
elif  winnerDoane > winnerDeGette and winnerDoane > winnerStockham:
    print("Winner: Raymon Anthony Doane")

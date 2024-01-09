import os
import csv
import pandas as pd

# Set Path to csv and do calculations within the open file.
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
# Set file path for text
    analysis_file = ("Analysis/PyPoll_analysis.txt")
# Create open lists to store items
    ballotID = []
    county = []
    candidate = []
    # Declare variables to do if then checks
    stockham = 'Charles Casper Stockham'
    degette = "Diana DeGette"
    doane = "Raymon Anthony Doane"
## opens file path and determines that code must be run while open so it will print the output to txt_file
    with open(analysis_file, 'w', newline ='') as txt_file:  
# For loop for iterating through rows in CSV file
        for row in csvreader:
        # Append lists with csv data so you can work with it
            ballotID.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

# Create a variable to count the number of votes and print
        countRow = len(ballotID)
        print(f"\nElection Results\n")
        print(f"----------------------------\n")
        print(f"Total Votes:   {countRow}\n")
        print(f"----------------------------\n")
        txt_file.write(f"\nElection Results\n\n")
        txt_file.write(f"----------------------------\n\n")
        txt_file.write(f"Total Votes:   {countRow}\n\n")
        txt_file.write(f"----------------------------\n\n")

#Candidates if statements to check the length of their votes compared to the length of the whole
        total = len(candidate)
        count = candidate.count(stockham)
        if count > 0:
            percentage = round(((count/total) * 100), 3)
            print(f'{stockham}: {percentage}% ({count})\n')
            txt_file.write(f'{stockham}: {percentage}% ({count})\n\n')
# Separate if statement where count now = count of DeGette
        count = candidate.count(degette)
        if count > 0:
            percentage = round(((count/total) * 100), 3)
            print(f'{degette}: {percentage}% ({count})\n')
            txt_file.write(f'{degette}: {percentage}% ({count})\n\n')
# "", but with Doane
        count = candidate.count(doane)
        if count > 0:
            percentage = round(((count/total) * 100), 3)
            print(f'{doane}: {percentage}% ({count})\n')
            txt_file.write(f'{doane}: {percentage}% ({count})\n\n')

        print(f"----------------------------\n")
        txt_file.write(f"----------------------------\n\n")
# This sets variables to candidate count based off of the candidates name
        winnerStockham = candidate.count(stockham)
        winnerDeGette = candidate.count(degette)
        winnerDoane = candidate.count(doane)
# If statement that compares the count of their names through winner varaible.
        if winnerStockham > winnerDeGette and winnerStockham > winnerDoane:
            print(f"Winner: Charles Casper Stockham\n")
            txt_file.write(f"Winner: Charles Casper Stockham\n\n")
        elif winnerDeGette > winnerStockham and winnerDeGette > winnerDoane:
            print(f"Winner: Diana DeGette\n")
            txt_file.write(f"Winner: Diana DeGette\n\n")
        elif  winnerDoane > winnerDeGette and winnerDoane > winnerStockham:
            print(f"Winner: Raymon Anthony Doane\n")
            txt_file.write(f"Winner: Raymon Anthony Doane\n\n")
        print(f"----------------------------")
        txt_file.write(f"----------------------------")
# import os module
import os

# module for reading csv file
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#The total number of months included in the dataset
    data = list(csvreader)
    #print(data)
    row_count = len(data)
    print(row_count)

#The net total amount of "Profit/Losses" over the entire period
    total = 0
    for row in csvreader(csvfile):
        total += int(row[2])
    print(total)
# import os module
import os

# module for reading csv file
import csv

unique_candidates = []

candidate_votes = {}

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
   
#The total number of votes cast
    data = list(csv_reader)
    row_count = len(data)
    print("Total Votes: " + str(row_count))

#A complete list of candidates who received votes
    for row in csv_reader:
        candidate_name = row [2]
        if candidate_name not in unique_candidates:
            unique_candidates.append(candidate_name)
            #candidate_votes[candidate_name] = 1
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
    print(unique_candidates)

#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.
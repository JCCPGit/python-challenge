## PyPoll

# import required modules
import os
import csv
from collections import Counter

# set required variables
number_votes = 0
total = 0

# create required lists
candidates = []
votes = []

# path to collect data from Resources folder
csv_path = os.path.join("Resources", "election_data.csv")

# module for reading CSV files
with open(csv_path, 'r') as datafile:
    csv_reader = csv.reader(datafile, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        
# calculation of the total number of votes cast
        number_votes += 1
        
# list of the candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
        
# calculation of the total number of votes each candidate won       
        votes.append(row[2])

votes_by_candidate = Counter(votes)

# calculation of the percentage of votes each candidate won
values = votes_by_candidate.values()
values_list = list(values)
total = sum(values)
percentage_by_candidate = [round(value * 100 / total, 2) for value in values]

# winner of the election
max_percentage = max(percentage_by_candidate)
index = percentage_by_candidate.index(max_percentage)

# print of analysis
print("Election Results")
print("----------------------------")
print(f'Total Votes: {number_votes}')
print("----------------------------")
print(f"{candidates[0]}: {percentage_by_candidate[0]}00% ({values_list[0]}) ")
print(f"{candidates[1]}: {percentage_by_candidate[1]}00% ({values_list[1]}) ")
print(f"{candidates[2]}: {percentage_by_candidate[2]}00% ({values_list[2]}) ")
print(f"{candidates[3]}: {percentage_by_candidate[3]}00% ({values_list[3]}) ")
print("----------------------------")
print(f"Winner: {candidates[index]}")
print("----------------------------")







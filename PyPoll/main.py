## PyPoll

import os
import csv

number_votes = 0

candidates = []
votes_by_candidate = []

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path) as datafile:
    csv_reader = csv.reader(datafile, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        number_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])

        votes_by_candidate.append(row[2])

number_of_candidates = len(candidates)
print(number_of_candidates)

for x in range(number_of_candidates):

[[x, votes_by_candidate(x)] for x in set(votes_by_candidate)]


print(candidates)



print("Election Results")
print("----------------------------")
print(f'Total Votes: {number_votes}')
print("----------------------------")






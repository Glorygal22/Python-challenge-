# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Create variables for calculations
    total_votes = 0
    candidate = ""
    candidate_votes = {}
    candidate_percentages ={}
    winner_votes = 0
    winner = ""

     # tally votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# calculate vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.000%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dashbreak = "-------------------------"

# print out results
print("Election Results")
print(dashbreak)
print(f"Total Votes: {total_votes}")
print(dashbreak)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

# save summary to txt
#save_file = Main.py.strip(".csv") + "_results.txt"
#filepath = os.path.join(".", save_file)
with open('MyPoll.txt','w') as text:
    text.write(dashbreak + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write(dashbreak + "\n")
    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write(dashbreak + "\n")

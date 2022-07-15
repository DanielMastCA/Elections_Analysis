# Data we need to retrieve
# 1. A total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes candidate received
# 4. Percentage of total votes each candidate received
# 5. The winner of the election based on popular vote

import csv
import datetime
import os

from numpy import append

# set elections data path
file_to_load = os.path.join('Resources', 'election_results.csv')

# set elections analysis path
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# initlalize candidates
candidate_options = {}
candiate_name = ''

# initialize votes
total_votes = 0

# open and read the elections data 
with open(file_to_load) as election_data:
    # analyse data
    file_reader = csv.reader(election_data)

    header = next(file_reader)

    for row in file_reader:
        total_votes += 1

        # print(row)

        # checks if we have a record of the candidate
        if (candiate_name != row[2]):
            candiate_name = row[2]

            if (candiate_name not in candidate_options):
                # add candidate to the list and set their votes to 0
                candidate_options[candiate_name] = 0

        # count vote
        candidate_options[candiate_name] += 1
        
    #initialize winning candidate
    winning_candidate = {
        'Name' : '',
        "Percentage of Votes" : 0,
        "Number of Votes" : 0
    }
        
    for candidate_name, candidate_votes in candidate_options.items():
        
        # calculate vote percentage 
        vote_percentage = (candidate_votes / total_votes) * 100

        # set winning candidate
        if (candidate_votes > 0):
            if (candidate_votes > winning_candidate["Number of Votes"]):
                winning_candidate['Name'] = candidate_name
                winning_candidate['Percentage of Votes'] = vote_percentage
                winning_candidate['Number of Votes'] = candidate_votes

        # print results for each candidate
        print(f"{candidate_name}: {vote_percentage:.01f}% ({candidate_votes:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate['Name']}\n"
    f"Winning Vote Count: {winning_candidate['Number of Votes']:,}\n"
    f"Winning Percentage: {winning_candidate['Percentage of Votes']:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    # print winning candidate
    # print(f"Candidate {winning_candidate['Name']} won with {winning_candidate['Percentage of Votes']:.01f}% of votes with {str(winning_candidate['Number of Votes'])} registered votes!")

    print(f"The total votes of this election amounts to {total_votes}")

    


# Open the file
with open(file_to_save, 'w') as outfile:
    outfile.write('Hello World')
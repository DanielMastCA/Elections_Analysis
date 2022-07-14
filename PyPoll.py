# Data we need to retrieve
# 1. A total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes candidate received
# 4. Percentage of total votes each candidate received
# 5. The winner of the election based on popular vote

import csv
import datetime
import os

# set elections data path
election_data_dir = os.path.join('Resources', 'election_results.csv')

# set elections analysis path
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# open and read the elections data 
with open(election_data_dir) as election_data:
    # analyse data
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)
    

    


# Open the file
with open(file_to_save, 'w') as outfile:
    outfile.write('Hello World')
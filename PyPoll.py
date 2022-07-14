# Data we need to retrieve
# 1. A total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes candidate received
# 4. Percentage of total votes each candidate received
# 5. The winner of the election based on popular vote

import csv
import datetime
import os

# get elections data path
election_data_dir = os.path.join('Resources', 'election_results.csv')

# open and read the elections data 
with open(election_data_dir) as election_data:
    print(election_data)

    # analyse data

election_analysis_dir = os.path.join('Analysis', 'election_analysis.txt')

with open(election_analysis_dir, 'w') as election_analysis:
    print('here')
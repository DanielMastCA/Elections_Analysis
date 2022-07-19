# Elections_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. A total number of votes cast.
2. A complete list of candidates who received votes.
3. A total number of votes the candidates received.
4. Percentage of total votes each candidate received.
5. The winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.5, Visual Studio Code, 1.69.1

## Summary
[Election Results](https://github.com/DanielMastCA/Elections_Analysis/blob/6e25e560e4b46dd74a12460d091d6c5de4dfd89a/Analysis/election_analysis.txt#L2-L23)

The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
    - Diana DeGette received 73.8% of the votes and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
    
## Challenge Overview
The Election Commission has requested some additional county data to complete the audit.

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout rate

## Challenge Audit Results
The analysis of the election show that:
- The couties were:
    - Arapahoe
    - Denver
    - Jefferson
- The county results were:
    - **Arapahoe county** had **6.7%** of the votes with **24,801** votes
    - **Denver county** had **82.8%** of the votes with **306,055** votes
    - **Jefferson county** had **10.5%** of the votes with **38,855** votes
- The county with the highest turnout rate:
    - **Denver county**, with **82.8%** of the votes and **306,055** votes

## Challenge Summary
This script can easily be modified to be used nationwide or on a local level such as in a mayoral election. With a few additions to the script we can easily make it versatile and work at any level of governance:


#### 1. By removing any association to the current analysis
By renaming the words/variables we have used in the script, we can remove any associating factor about this election and increase the script's versatility.

##### Current Script
```Python
# Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Initalize county tracker
county_name = ""

# Extract the county name from each row.
county_name = row[1]
```

##### Suggested changes
```Python
# Create an area list and area votes dictionary.
areas = []
area_votes = {}

# Initalize area tracker
area_name = ""

# Extract the area name from each row.
area_name = row[1]
```


#### 2. By adding user choice to determine result outputs
We can add a choice to choose the type of election cast to determine result outputs. All we need to do is create a new table with a list of keywords, add a column for each type of election, then finally, refactor our script to load and use the set election variables.

#### New Elections Types Table
| Key Words | City | County | State | Nation |
| --- | --- | --- | --- | --- |
| area_type | City | County | State | Nation |


```Python
# Add election type variables
election_type_list = []
election_type = ""

# User choice based on election type
with open(strings_to_load) as election_types:
    reader = election_types

    header = list(next(reader))

    for x in range(1, len(header)):
        election_type_list.append(header[x].lower)

    # Wait for the user to choose election type
    while True:
        election_type = input(f"Please enter the election type you would like to analyse")
        if election_type.lower() in election_type_list:
            break
```

Now assuming we have loaded the elections types table above, we can edit the code that prints the results to incorporate which election type to choose from.

#### So instead of:
```Python
    # Get the county with the largest turnout result
    highest_turnout_area_string = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {highest_turnout_area['Name']}\n"
        f"-------------------------\n"
    )
```

#### We use somethink like:
```Python
    # Get the county with the largest turnout result
    highest_turnout_area_string = (
        f"\n"
        f"-------------------------\n"
        f"Largest {election_strings['area_type']} Turnout: {highest_turnout_area['Name']}\n"
        f"-------------------------\n"
    )
```

In short, code versatility is fairly easy and with a few steps, this code can be used anywhere and anyhow, at any election.

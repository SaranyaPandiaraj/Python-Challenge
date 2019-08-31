#PyPoll Challenge

import os
import csv

# Path to collect data from the Resources folder

election_csv = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')

#Creating lists to store the respecive contents

Votes = []
Candidates = {}
Percent = {}
Count = 0
Winner = ""
# Read in the CSV file and splitting the data on commas

with open(election_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
            
    csv_header = next(csvreader)
    
    # Loop through the data
    
    for row in csvreader:
        
		#Calculating the Total Number of Votes
        Votes.append(int(row[0]))
        Total_Votes = len(Votes)
        
        if row[2] in Candidates.keys():
            Candidates[row[2]] += 1
        else:
            Candidates[row[2]] = 1
        
        for Name, VoteCount in Candidates.items():
            Percent[Name] = round(((VoteCount/Total_Votes) * 100),1)

        for Name in Candidates.keys():
            if Candidates[Name] > Count:
                Winner = Name
                Count = Candidates[Name]
				
				
    
#Displaying the Final Output
output = (
f"\n-----------------------------------------------------"
f"\n                 Election Results                    "    
f"\n-----------------------------------------------------" 
f"\n"   
f"\n Total Votes : {Total_Votes} \n"
f"\n-----------------------------------------------------" 
f"\n"  
)
print(output)
for Name, VoteCount in Candidates.items():
    stat = print(Name + " : " + str(Percent[Name]) + "% (" + str(VoteCount) + ")")      
winner = (
f"\n-----------------------------------------------------" 
f"\n"   
f"\n Winner : {Winner} \n"
f"\n-----------------------------------------------------"  
)
print(winner)
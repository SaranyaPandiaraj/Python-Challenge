#PyPoll Challenge

import os
import csv

# Path to collect data from the Resources folder

election_csv = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')

#Creating lists to store the respecive contents

Votes = []

# Read in the CSV file and splitting the data on commas

with open(election_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
            
    csv_header = next(csvreader)
    
    # Loop through the data
    
    for row in csvreader:
        
        Votes.append(int(row[0]))
        Total_Votes = len(Votes)
        
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
#PyPoll Challenge

import os
import csv

# Path to collect data from the Resources folder

election_csv = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')

#Creating lists/dictionaries to store the respecive contents

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
        
        #Storing the Candidate Name And total number of votes each candidate won in a Candidates{} dictionary
        #Considering the Name as the Key and VoteCount as the Value 
        if row[2] in Candidates.keys():
            Candidates[row[2]] += 1
        else:
            Candidates[row[2]] = 1
        
        #Calculating the percentage of votes each candidate won
        for Name, VoteCount in Candidates.items():
            Percent[Name] = format((VoteCount/Total_Votes) * 100 , '.3f')
            
        #Identifying the winner of the election based on popular vote
        #Candidate[Name] will give you the Vote Count value of the Candidate and Name is the Candidate Name
        for Name in Candidates.keys():
            if Candidates[Name] > Count:
                Winner = Name
                Count = Candidates[Name]
				
#print(Candidates.keys()) --> dict_keys(['Khan', 'Correy', 'Li', "O'Tooley"])

#print(Candidates.values()) --> dict_values([2218231, 704200, 492940, 105630])

#print(Candidates.items()) --> dict_items([('Khan', 2218231), ('Correy', 704200), ('Li', 492940), ("O'Tooley", 105630)])   

                      
#Displaying the Final Output

TotalVotes = (
f"\n-----------------------------------------------------"
f"\n                 Election Results                    "    
f"\n-----------------------------------------------------" 
f"\n"   
f"\n Total Votes : {Total_Votes} \n"
f"\n-----------------------------------------------------" 
f"\n"  
)
print(TotalVotes)
for Name, VoteCount in Candidates.items():
    print(Name + " : " + str(Percent[Name]) + "% (" + str(VoteCount) + ")\n")      
Winner = (
f"\n-----------------------------------------------------" 
f"\n"   
f"\n Winner : {Winner} \n"
f"\n-----------------------------------------------------"  
)
print(Winner)

#Exporting the Final Output to a Text File

output_to_txt = os.path.join('..', 'PyPoll','Output', 'PyPoll_Election_Results.txt')
with open(output_to_txt, "w") as txt_file:
    txt_file.write(TotalVotes)
    for Name, VoteCount in Candidates.items():
        txt_file.write(Name + " : " + str(Percent[Name]) + "% (" + str(VoteCount) + ")\n\n")
    txt_file.write(Winner)

print("\n \n The Election Result has been Exported to PyPoll_Election_Results.txt file. \n \n ")
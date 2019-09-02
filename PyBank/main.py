#PyBank Challenge

import os
import csv

# Path to collect data from the Resources folder

budget_csv = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')

#Creating lists to store the respecive contents

Months = []
Amount = []
Change_Profit_Loss = []

# Function to return the average
def average(Change_Profit_Loss): 
    return round(sum(Change_Profit_Loss) / len(Change_Profit_Loss),2) 

# Read in the CSV file and splitting the data on commas

with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
            
    csv_header = next(csvreader)
    
    # Loop through the data
    
    for row in csvreader:
        
        #The total number of months included in the dataset
        Months = Months + [row[0]]
        Total_Months = len(Months)
        
        #The net total amount of "Profit/Losses" over the entire period
        Amount.append(int(row[1]))
        Total_Amount = sum(Amount)
        
    for change in range(len(Amount)-1):
        
        #The average of the changes in "Profit/Losses" over the entire period
        Change_Profit_Loss.append(Amount[change+1] - Amount[change])   
        Average_Change = average(Change_Profit_Loss)

#Finding the Greatest Increase & Decrease in Profits (date and amount) over the entire period

Greatest_Increase = max(Change_Profit_Loss)
Greatest_Decrease = min(Change_Profit_Loss) 

Greatest_Increase_Month = Months[Change_Profit_Loss.index(Greatest_Increase)+1]
Greatest_Decrease_Month = Months[Change_Profit_Loss.index(Greatest_Decrease)+1]
        
#Displaying the Final Output
output = (
f"\n-----------------------------------------------------"
f"\n                 Financial Analysis                  "    
f"\n-----------------------------------------------------" 
f"\n"   
f"\n Total Months : {Total_Months} \n"
f"\n Total Amount : ${Total_Amount} \n"
f"\n Average Change: ${Average_Change} \n"
f"\n Greatest Increase in Profits: {Greatest_Increase_Month} (${str(Greatest_Increase)}) \n"
f"\n Greatest Decrease in Profits: {Greatest_Decrease_Month} (${str(Greatest_Decrease)}) \n"
f"\n-----------------------------------------------------"

)
print(output)

#Exporting the Final Output to a Text File

output_to_txt = os.path.join('..', 'PyBank','Output', 'Pybank_Financial_Analysis.txt')
with open(output_to_txt, "w") as txt_file:
    txt_file.write(output)

print("\n \n The Financial Analysis Output has been Exported to Pybank_Financial_Analysis.txt file. \n \n ")
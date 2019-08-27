import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')
print(budget_csv)

Months_Count = []
Net_Total_Amount = []
Change_Profit_Loss = []

# Function to return the average
def average(Change_Profit_Loss): 
    return round(sum(Change_Profit_Loss) / len(Change_Profit_Loss),2) 



# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
            
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Using Comprehension Method :
    #Months_Count = [Month for Month in csvreader]
    #print(len(Months_Count))
    
    # Loop through the data
    for row in csvreader:
        
        Months_Count = Months_Count + [row[0]]
        Net_Total_Amount.append(int(row[1]))
        
    for i in range(len(Net_Total_Amount)-1):
        Change_Profit_Loss.append(Net_Total_Amount[i+1]-Net_Total_Amount[i])   

Greatest_Increase = max(Change_Profit_Loss)
Greatest_Decrease = min(Change_Profit_Loss)		
        
        
print(f"Total Months : {len(Months_Count)}")
print(f"Total : ${sum(Net_Total_Amount)}")
print(f"Average Change: ${average(Change_Profit_Loss)}")
print(f" $ {str(Greatest_Increase)}")
print(f" $ {str(Greatest_Decrease)}")
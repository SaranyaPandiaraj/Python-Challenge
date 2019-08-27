import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')
#print(budget_csv)

Total_Months = []
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
    #print(f"CSV Header: {csv_header}")
    
    # Using Comprehension Method :
    #Total_Months = [Month for Month in csvreader]
    #print(len(Total_Months))
    
    # Loop through the data
    for row in csvreader:
        
        Total_Months = Total_Months + [row[0]]
        Net_Total_Amount.append(int(row[1]))
        
    for i in range(len(Net_Total_Amount)-1):
	
        Change_Profit_Loss.append(Net_Total_Amount[i+1] - Net_Total_Amount[i])   

Greatest_Increase = max(Change_Profit_Loss)
Greatest_Decrease = min(Change_Profit_Loss)	

Greatest_Increase_Month = Total_Months[Change_Profit_Loss.index(Greatest_Increase)+1]
Greatest_Decrease_Month = Total_Months[Change_Profit_Loss.index(Greatest_Decrease)+1]
        
print("-----------------------------------------------------")
print("		Financial Analysis		")    
print("-----------------------------------------------------\n")    
print(f" Total Months : {len(Total_Months)}\n")
print(f" Total : ${sum(Net_Total_Amount)}\n")
print(f" Average Change: ${average(Change_Profit_Loss)}\n")
print(f" Greatest Increase in Profits: {Greatest_Increase_Month} (${str(Greatest_Increase)})\n")
print(f" Greatest Decrease in Profits: {Greatest_Decrease_Month} (${str(Greatest_Decrease)})\n")
print("-----------------------------------------------------")  
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
    
    # Using Comprehension Method :
    
    #Months = [Month for Month in csvreader]
    #print(len(Months))
    
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

print("\n-----------------------------------------------------")
print("                 Financial Analysis                    ")    
print("-----------------------------------------------------\n")    
print(f" Total Months : {Total_Months}\n")
print(f" Total Amount : ${Total_Amount}\n")
print(f" Average Change: ${Average_Change}\n")
print(f" Greatest Increase in Profits: {Greatest_Increase_Month} (${str(Greatest_Increase)})\n")
print(f" Greatest Decrease in Profits: {Greatest_Decrease_Month} (${str(Greatest_Decrease)})")
print("\n-----------------------------------------------------")  
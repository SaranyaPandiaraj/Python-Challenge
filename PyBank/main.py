import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')
print(budget_csv)

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
			
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
	
    # Loop through the data
    for row in csvreader:
		
        #if row[0] == 'Jan-2010':
		
            print(row[0]))

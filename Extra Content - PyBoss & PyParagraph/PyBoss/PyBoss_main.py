import os
import csv
import datetime

csvpath = os.path.join("../PyBoss/Resources", "employee_data.csv")

#Dictionary to store the states with abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Creating a List to Store Emp ID, First Name, Last Name, DOB, SSN & State

Emp_Detail = [['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    
    csv_header = next(csvreader)
    
    for row in csvreader:
    
        Emp_Detail.append([
		
		row[0], #Emp ID
        row[1].split(" ")[0], #First Name
        row[1].split(" ")[1], #Last Name
        datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'), #DOB
         '***-**-' + row[3][-4:], #SSN
        us_state_abbrev[row[4]] #State
		
		])
        
#print(Emp_Detail) 

# Write all of the election data to csv
outputfile = os.path.join("../PyBoss/Output", "Reformat_employee_data.csv")
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(Emp_Detail)
        
print("\nThe Reformatted Employee Data has been exported to Reformat_employee_data.csv file in the Output Folder")	
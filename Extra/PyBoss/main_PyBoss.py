## PyBoss

import os
import csv
from datetime import datetime
import ast

employee_id = []
first_name = []
last_name = []
date_new = []
ssn_new = []
states_new = []

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

csv_file = os.path.join("Resources", "employee_data.csv")

with open(csv_file, "r") as datafile:
    csv_reader = csv.reader(datafile, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        id = row[0]
        employee_id.append(id)
        
        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
            
        date = row[2]
        date_format = datetime.strptime(date, "%Y-%m-%d").strftime("%m/%d/%Y")
        date_new.append(date_format)

        ssn = row[3].split("-")
        ssn_format = "***-**-" + ssn[2]
        ssn_new.append(ssn_format)

        for k, v in us_state_abbrev.items():
            if row[4] == k:
                states_new.append(v)

cleaned_csv = zip(employee_id, first_name, last_name, date_new, ssn_new, states_new)

output_file = os.path.join("Analysis", "employee_data_final.csv")

with open(output_file, "w", newline="") as datafile_b:
    writer = csv.writer(datafile_b)

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(cleaned_csv)

final_file = os.path.join("Analysis", "employee_data_final.csv")

with open(final_file, "r") as datafile_c:
    final_reader = csv.reader(datafile_c, delimiter=',')
    for row in final_reader:
        print(row[0], row[1], row[2], row[3], row[4], row[5])
        
        






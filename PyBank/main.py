## PyBank

# import required modules
import os
import csv

# set required variables
month_counter = 0
total_amount = 0
total_change = 0
a = 0

# create required lists
monthly_changes = []
months_monthly_changes = []

# path to collect data from Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# module for reading CSV files
with open(csvpath, 'r') as csvfile_a:
    csv_reader_a = csv.reader(csvfile_a, delimiter=",")
    csv_header_a = next(csv_reader_a)

# identify the value of the initial row
    interestingrow = [row for idx, row in enumerate(csv_reader_a) if idx == 0]

    for row in interestingrow:
        initial_value = int(row[1])
        
# module for reading CSV files
with open(csvpath, 'r') as csvfile_b:
    csv_reader_b = csv.reader(csvfile_b, delimiter=",")
    csv_header_b = next(csv_reader_b)

    for row in csv_reader_b:

# calculation of total months included in the dataset
        month_counter += 1
        
# calculation of the net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])
        
# calculation of the changes in "Profit/Losses" over the entire period and the average of those changes
        monthly_change = int(row[1]) - a
        total_change = total_change + (int(row[1]) - a)

        if row[1] != initial_value:
            monthly_changes.append(monthly_change)
            months_monthly_changes.append(row[0])
        
        a = int(row[1])

average_change = round((total_change - initial_value) / (month_counter - 1),2)

# calculation of the greatest increase and decrease in profit and losses (date and amount), respectively
greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)
index_increase = monthly_changes.index(greatest_increase_profits)
index_decrease = monthly_changes.index(greatest_decrease_profits)
month_increase = months_monthly_changes[index_increase]
month_decrease = months_monthly_changes[index_decrease]

# print of analysis

print("Financial Analysis")
print("------------------")

print(f'Total Months: {month_counter}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_increase} $({greatest_increase_profits})')
print(f'Greatest Decrease in Profits: {month_decrease} $({greatest_decrease_profits})')


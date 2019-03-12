# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')


# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #create variables for calculations
    month_count = 0
    total_profit = 0
    this_month_profit = 0
    last_month_profit = 0
    proft_change = 0
    profit_changes = []
    months = []
    #gather monthly changes in profit
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_profit = int(row[1])
        total_profit = total_profit + this_month_profit
        if month_count > 1:
            profit_change = this_month_profit - last_month_profit
            profit_changes.append(profit_change)
        last_month_profit = this_month_profit
    # analyze the month by month results
    sum_profit_changes = sum(profit_changes)
    average_change = sum_profit_changes / (month_count - 1)
    max_change = max(profit_changes)
    min_change = min(profit_changes)
    max_month_index = profit_changes.index(max_change)
    min_month_index = profit_changes.index(min_change)
    max_month = months[max_month_index]
    min_month = months[min_month_index]
    # print summary to user
    print("Financial Analysis")
    print("----------------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

    # save summary to txt
    save_file = bankreader.strip(".csv") + "_results.txt"
    filepath = os.path.join(".", save_file)
    with open(filepath,'w') as text:
        text.write("Financial Analysis" + "\n")
        text.write("----------------------------------------" + "\n")
        text.write(f"Total Months: {month_count}" + "\n")
        text.write(f"Total: ${total_profit}" + "\n")
        text.write(f"Average Profit Change: ${average_change}" + "\n")
        text.write(f"Greatest Increase in Profit: {max_month} (${max_change})" + "\n")
        text.write(f"Greatest Decrease in Profit: {min_month} (${min_change})" + "\n")
# Dependencies
import os
import csv

#file path
pybank_path = os.path.join('..', 'Resources', 'budget_data.csv')

#Reading using CSV module

with open(pybank_path, newline='', encoding='utf-8') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:

        date.append(row[0])
        profit/loss.append(row[1])

# Total Months

# Total

# Average Change

# Greatest Increase
        percent = round(int(row[]) / int(row[], 2)
        gain_percent.append(percent)

# Greatest Decrease   
        percent = round(int(row[]) / int(row[], 2)
        loss_percent.append(percent)

# Zip lists together
cleaned_csv = zip(total months, total, average change, greatest increase, greatest decrease)


# Specify the file to write to
pybank_output_path = os.path.join("Analysis", "outputbank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(pybank_output_path, 'w', newline='') as datafile:

    # Initialize csv.writer
    writer = csv.writer(datafile)

    # Write the first row (column headers)
    writer.writerow(['First Name', 'Last Name', 'SSN'])

# Print final products

def print_Financial_Analysis():
    print(f"Financial Analysis")

print_Financial_Analysis()


Total Months: 
Total: 
Average  Change: 
Greatest Increase 
Greatest Decrease 
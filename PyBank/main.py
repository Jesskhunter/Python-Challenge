# Dependencies
import os
import csv

#file path
pybank_path = os.path.join('C:/Users/jessk/OneDrive/Desktop/HW/Python-Challenge/PyBank/Resources/budget_data.csv')

#Reading using CSV module
with open(pybank_path,newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')

# Read header row
    header = next(csvreader)

# Set totals to zero for computing
    total_months = 0
    total_sum = 0

# Lists for computing                                 
    month_sum = []
    profit_or_loss = []
    previous = 0
    change = 0

# Computations
    for row in csvreader:
        total_months +=1
        total_sum +=(int(row[1]))
        change = int(row[1])-previous
        profit_or_loss.append(change)
        previous = int(row[1])

    Average_change = sum(profit_or_loss[1:])/len(profit_or_loss[1:])
    max_index = profit_or_loss.index(max(profit_or_loss))
    min_index = profit_or_loss.index(min(profit_or_loss))
    final_output=(
    f"Financial Analysis \n"
    f"---------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_sum)}\n"
    f"Average Change: ${str(round(Average_change,2))}\n"
    f"Greatest Increase in Profits: (${profit_or_loss[max_index]})\n"
    f"Greatest Decrease in Profits: (${profit_or_loss[min_index]})\n"
    )
# Specify the file to write to
output_path = os.path.join("C:/Users/jessk/OneDrive/Desktop/HW/Python-Challenge/PyBank/Analysis/outputbank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as datafile:
    datafile.write(final_output)

print(final_output)

 

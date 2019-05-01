# Import modules

import os
import csv

# Path to our csv file

csvPyBank = os.path.join("..", "PyBank", "budget_data.csv")

# Create empty lists to iterate through specific rows

total_months = []
total_amount = []
average_of_change = []


#open file to read and get information out of it    

with open(csvPyBank, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skipping first line in our file

    header = next(csvreader)
   

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period

    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))

   
# The average of the changes in "Profit/Losses" over the entire period

    for i in range(len(total_amount) - 1):
        average_of_change.append(total_amount[i + 1] - total_amount[i])


# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

    max_increase_value = max(average_of_change)
    max_decrease_value = min(average_of_change)

    max_increase_month = average_of_change.index(max(average_of_change)) + 1
    max_decrease_month = average_of_change.index(min(average_of_change)) + 1 

# Print all statements

print(f"""Financial Analysis
----------------------------
Total Month: {len(total_months)}
Total: ${sum(total_amount)}
Average Change: ${round(sum(average_of_change)/len(average_of_change),2)}
Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})
Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})
""")

# Output

output_path = os.path.join("..", "PyBank", "Financial_Analysis.txt")

# Printing results in new file we made

with open(output_path, "w") as file:
    
    file.write("\n")
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average_of_change)/len(average_of_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
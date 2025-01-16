# Dependencies
import csv


# Files to load and output (update with correct file paths)
budget_file = r'C:\Users\eek_e\Documents\Data A\Starter_Code\PyBank\Resources\budget_data.csv'  # Input file path #
file_output =  r'C:\Users\eek_e\Documents\Data A\Starter_Code\PyBank\analysis\Budget_analysis.txt' # Output file path


# Define variables to track the financial data
greatest_decrease=0
greatest_increase=0
accumulate_change=0
# Add more variables to track other necessary financial data
total_month=0
total_Profit_losses=0.0
PL_changes=[]
prev_value=0




# Open and read the csv
with open(budget_file,encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)
    # Process each row of data
    
    for r in reader:
        # Track the total Months and Profit/Losses
        total_month +=1
        total_Profit_losses += int(r[1]) 
        # Track the net change
        current = int(r[1])
        ch=current-prev_value # ch represent the variable change which is current Profit/Losses -  Previous Profit/Losses - 
        accumulate_change += ch
        PL_changes.append(ch)
        prev_value = current
        # Calculate the greatest increase in profits (month and amount)
        if ch > greatest_increase:
            greatest_increase=ch
            greatest_increase_month=r[0]

        # Calculate the greatest decrease in losses (month and amount)
        if ch< greatest_decrease:
            greatest_decrease=ch
            greatest_decrease_month=r[0]

        

# Calculate the average net change across the months
First_value=int(PL_changes[0])#Query the first value in changes list to be remove from the accumulate changes       
average_changes = (accumulate_change-First_value)/(len(PL_changes)-1)

#Print the output

print("Financial Analysis")
print("")
print("-------------------------------------------------------------")
print("")
print("Total months:",total_month)
print("")
print(f"Total: ${int(total_Profit_losses)}")
print("")
print(f"Average Change: ${round(average_changes,2 )}")
print("")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print("")
print(f"Greatest Decrease in Profit: {greatest_decrease_month} (${greatest_decrease})")


# Write the results to a text file
with open(file_output, "w") as txt_file:
    txt_file.write(str("Financial Analysis"))
    txt_file.write((f"\n"))
    txt_file.write(str("--------------------------------------"))
    txt_file.write((f"\n"))
    txt_file.write(f"Total months: {total_month}\n")
    txt_file.write((f"\n"))
    txt_file.write(f"Total: ${int(total_Profit_losses)}\n")
    txt_file.write((f"\n"))
    txt_file.write(f"Average Change: ${round(average_changes,2 )}\n")
    txt_file.write((f"\n"))
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write((f"\n"))
    txt_file.write(f"Greatest Decrease in Profit: {greatest_decrease_month} (${greatest_decrease})\n")

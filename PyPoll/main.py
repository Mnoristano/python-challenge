import os
import csv

poll_csv = os.path.join("budget_data.txt")

# Lists to store data
date = []
profit= []

with open(pull_csv, newline="") as csvfile:
	
	
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)
	for row in csvreader:
        # Add title
		date.append(row[0])
		profit.append(float(row[1]))
		i+=1
	for x in range(i):
		change = profit[x]-profit[x-1]
		totalChange += change
		if change > maxChange:
			maxChange = change
			maxDate = date[x]
		if change < minChange:
			minChange = change
			minDate = date[x]
		
		
	total = sum(profit)
	avgChange = totalChange/i
	
	
	
	
	
	
	print("Financial Analysis")
	print("----------------------------------")
	print("Total Months: ",i)
	print("Total: $"+str(total))
	print(f"Average Change: ${avgChange}")
	print(f"Greatest Increase In Profits: {maxDate} (${maxChange})")
	print(f"Greatest Decrease In Profits: {minDate} (${minChange})")
	#print("Average Change: $"+str(avgChange))
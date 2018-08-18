import os
import csv

budget_csv = os.path.join("budget_data.txt")

# Lists to store data
date = []
profit= []
totalChange = []
with open(budget_csv, newline="") as csvfile:
	change = 0
	i = 0
	maxChange = 0
	minChange = 0
	maxDate = ""
	minDate= ""
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)
	for row in csvreader:
        # Add title
		date.append(row[0])
		profit.append(float(row[1]))
		i+=1
	for x in range(i):
		if x!= 0:
			change = profit[x]-profit[x-1]
			totalChange.append(change)
		if change > maxChange:
			maxChange = change
			maxDate = date[x]
		if change < minChange:
			minChange = change
			minDate = date[x]
		
		
	total = sum(profit)
	avgChange = round(sum(totalChange)/(i-1),2)
	
	
	
	
	
	
	print("Financial Analysis")
	print("----------------------------------")
	print("Total Months: ",i)
	print("Total: $"+str(total))
	print(f"Average Change: ${avgChange}")
	print(f"Greatest Increase In Profits: {maxDate} (${maxChange})")
	print(f"Greatest Decrease In Profits: {minDate} (${minChange})")
	
import os
import csv

poll_csv = os.path.join("election_data.txt")

# Voter ID,County,Candidate
canidate= []
county= []
voterID = []
i = 0
khanVotes=0
correyVotes=0	
liVotes=0
tooleyVotes=0
with open(poll_csv, newline="") as csvfile:
	
	
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)
	for row in csvreader:
		voterID.append(row[0])
		county.append(row[1])
		canidate.append(row[2])
		i+=1
	for x in range(i):
		if canidate[x] == "Khan":
			khanVotes += 1
		elif canidate[x] == "Correy":
			correyVotes += 1
		elif canidate[x] == "Li":
			liVotes += 1
		elif canidate[x] == "O'Tooley":
			tooleyVotes += 1

totalVotes = khanVotes + correyVotes + liVotes + tooleyVotes	

khanP = round(khanVotes/totalVotes*100,4)
correyP = round(correyVotes/totalVotes*100,4)
liP = round(liVotes/totalVotes*100,4)
tooleyP = round(tooleyVotes/totalVotes*100,4)

pList = [khanP,correyP,liP,tooleyP]
winner = ""
if max(pList) == khanP:
	winner ="Khan"
if max(pList) == correyP:
	winner = "Correy"
if max(pList) == liP:
	winner = "Li"
if max(pList) == tooleyP:
	winner ="O'Tooley"
	
print("Election Results")
print("------------------------------")
print(f"Total Votes: {totalVotes}")
print("------------------------------")		
print(f"Khan: {khanP}% ({khanVotes})")
print(f"Correy: {correyP}% ({correyVotes})")
print(f"Li: {liP}% ({liVotes})")
print(f"O'Tooley: {tooleyP}% ({tooleyVotes})")
print("------------------------------")	
print(f"Winner: {winner}")
print("------------------------------")		

with open('sumElection.txt', 'w') as tf:
	tf.write("Election Results\n")
	tf.write("------------------------------\n")
	tf.write(f"Total Votes: {totalVotes}\n")
	tf.write("------------------------------\n")
	tf.write(f"Khan: {khanP}% ({khanVotes})\n")
	tf.write(f"Correy: {correyP}% ({correyVotes})\n")
	tf.write(f"Li: {liP}% ({liVotes})\n")
	tf.write(f"O'Tooley: {tooleyP}% ({tooleyVotes})\n")
	tf.write("------------------------------\n")
	tf.write(f"Winner: {winner}\n")
	tf.write("------------------------------\n")
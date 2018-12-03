import csv
with open("election_data.csv", "r") as file:
    csvreader = csv.reader(file)
    csvheader = next(csvreader)
# Creating empty dictionary 
    candidate_votes = {}
#    print(candidate_votes.keys())

    for row in csvreader:
        candidate = row[2]

# print(f"Checking if {candidate} is in the candidate  votes dictionary keys")

#populating dictionary with individule candidate and total votes
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#total votes
totalvotes=sum(candidate_votes.values())
#calculating vote percent for individule candidate
percent=[]
for i in candidate_votes:
    percent = round((float(candidate_votes[i])/totalvotes)*100,0)

#finding candidate with maximum votes

for key in candidate_votes.keys():

    if candidate_votes[key] == max(candidate_votes.values()):
        the_key_were_interested_in = key
#printing final output
print("  Election Results")
print("------------------------------------------")
print(f" Total Votes : {totalvotes}")
print("------------------------------------------")
for i in candidate_votes:
    percent = round((float(candidate_votes[i])/totalvotes)*100,0)
    print(f" {i} : %{percent} ({candidate_votes[i]})")
print("------------------------------------------")
print(f" The winner is : {the_key_were_interested_in}")
print("------------------------------------------")

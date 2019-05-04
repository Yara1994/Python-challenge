# Importing Modules

import os
import csv

# Path to ur CSV file

csvPyPoll = os.path.join("..", "PyPoll", "election_data.csv")

# Open file to read and get information out of it 

with open(csvPyPoll, "r", newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Skipping first line in our file

    header = next(csvreader)

    # Create empty lists to iterate through specific rows

    voter_id = []
    county = []
    candidate = []

    # Looping though every single row (without header) to append each element in DATA to lists we made before

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # The total number of votes cast   
     
    total_votes = len(voter_id)
    
    # A complete list of candidates who received votes and the total number of votes each candidate won

    candidate_list = []     # creating empty list to store all candidate names
    candidate_votes = {}    # creating empty dictionary to store all votes for each candidate

    for name in candidate:
        if name not in candidate_list:
            candidate_list.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] = candidate_votes[name] + 1

    # The percentage of votes each candidate won
    
    candidate_vote_percentage = {}    # creating empty dictionary to store all percentage for every candidate

    for element in candidate_list:
        candidate_vote_percentage[element] = (candidate_votes[element]/total_votes)*100

    # The winner of the election based on popular vote

    winner_votes =  0
    
    for candidate in candidate_votes:
    
        if candidate_votes[candidate] > winner_votes:
            winner_votes = candidate_votes[candidate]
            winner = candidate

    
# Print all statements:

print(f"""Election Results
---------------------------
Total Votes: {total_votes}
---------------------------
Khan: {candidate_vote_percentage["Khan"]:.3f}% ({candidate_votes["Khan"]})
Correy: {candidate_vote_percentage["Correy"]:.3f}% ({candidate_votes["Correy"]})
Li: {candidate_vote_percentage["Li"]:.3f}% ({candidate_votes["Li"]})
O'Tooley: {candidate_vote_percentage["O'Tooley"]:.3f}% ({candidate_votes["O'Tooley"]})
---------------------------
Winner: {winner}
---------------------------
""")   

# Output

output_path = os.path.join("..", "PyPoll", "Election_Results.txt")

# Printing results in new file we made

file = open("Election_Results.txt", "w")
    
file.write("Election Results")
file.write("\n")
file.write("---------------------------")
file.write("\n")
file.write(f"Total Votes: {total_votes}")
file.write("\n")
file.write(f"---------------------------")
file.write("\n") 
x = candidate_vote_percentage["Khan"]
print(x)
y = f"{x:.3f}"
print(y)
file.write(f"Khan: {y}%")
#file.write("\n")
#file.write(f"Correy: {candidate_vote_percentage["Correy"]:.3f}% ({candidate_votes["Correy"]})")
#file.write("\n")
#file.write(f"Li: {candidate_vote_percentage["Li"]:.3f}% ({candidate_votes["Li"]})")
#file.write("\n")
#file.write(f"O'Tooley: {candidate_vote_percentage["O'Tooley"]:.3f}% ({candidate_votes["O'Tooley"]})")
file.write("\n")
file.write("---------------------------")
file.write("\n")
file.write(f"Winner: {winner}")


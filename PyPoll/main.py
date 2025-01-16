# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv


# Files to load and output (update with correct file paths)
file_to_load = r'C:\Users\eek_e\Documents\Data A\Starter_Code\PyPoll\Resources\election_data.csv'  # Input file path
file_to_output = r'C:\Users\eek_e\Documents\Data A\Starter_Code\PyPoll\analysis\Poll_analysis.txt'  # Output file path

# Initialize variables to track the election data
t_votes = 0  # Track the total number of votes cast
candidates_total_votes = {} # dictionary for total of votes on each candidate
Candidate_name=[]# Creating list for storing the candidate names
Percentage_per_candidate=[]#Creating list for storing the candidate percentage
Total_vote_per_candidate=[]#Creating list for storing the candidate total votes
Winner="" # Winning Candidate


# Open the CSV file and process it
with open(file_to_load,encoding='UTF-8') as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        t_votes +=1 
        c = row[2] # counter for candidates - 3er column - this logic was base on https://www.w3schools.com/python/python_dictionaries_access.asp
        if c in candidates_total_votes: # If candidate is in the dictionary then add 1 vote the this candidate
            candidates_total_votes[c] += 1
        else:
            candidates_total_votes[c] = 1 # if Candidate is no in the dictionary so add the candidate to it and a 1 vote.

for candidates, votes in candidates_total_votes.items(): # For loop for going through the dictionary and storing data in a list
    percentage_vote=  (votes/t_votes)*100
    Candidate_name.append(candidates)
    Percentage_per_candidate.append(percentage_vote)
    Total_vote_per_candidate.append(votes)


    ############Checking who was the winner
if Total_vote_per_candidate[0] > Total_vote_per_candidate[1] and Total_vote_per_candidate[0] > Total_vote_per_candidate[2]:
    winner=Candidate_name[0]
elif Total_vote_per_candidate[1] > Total_vote_per_candidate[0] and Total_vote_per_candidate[1] > Total_vote_per_candidate[2]:
    winner=Candidate_name[1]
else:
    winner=Candidate_name[2]

# Print the results to the terminal

print(f"Election Results")
print("")
print("-------------------------------------------------------------")
print("")
print(f"Total Votes: {t_votes}")
print("")
print("-------------------------------------------------------------")
print("")
print( f"{Candidate_name[0]}: {round(Percentage_per_candidate[0],3)}% ({Total_vote_per_candidate[0]})")
print( f"{Candidate_name[1]}: {round(Percentage_per_candidate[1],3)}% ({Total_vote_per_candidate[1]})")
print( f"{Candidate_name[2]}: {round(Percentage_per_candidate[2],3)}% ({Total_vote_per_candidate[2]})")
print("")
print("-------------------------------------------------------------")
print("")
print(f"Winner: {winner}")
print("")
print("-------------------------------------------------------------")


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(str("Election Results"))
    txt_file.write((f"\n"))
    txt_file.write("--------------------------------------------------------")
    txt_file.write((f"Total Votes: {t_votes}\n"))
    txt_file.write("--------------------------------------------------------")
    txt_file.write((f"\n"))
    txt_file.write(f"{Candidate_name[0]}: {round(Percentage_per_candidate[0],3)}% ({Total_vote_per_candidate[0]})\n")
    txt_file.write(f"{Candidate_name[1]}: {round(Percentage_per_candidate[1],3)}% ({Total_vote_per_candidate[1]})\n")
    txt_file.write(f"{Candidate_name[2]}: {round(Percentage_per_candidate[2],3)}% ({Total_vote_per_candidate[2]})\n")
    txt_file.write((f"\n"))
    txt_file.write("--------------------------------------------------------")
    txt_file.write((f"\n"))
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write((f"\n"))
    txt_file.write("--------------------------------------------------------")

   

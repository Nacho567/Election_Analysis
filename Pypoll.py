# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


#Add dependencies

import csv
import os

# Assign a variable for the file to load and the path to it.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Set total votes to zero
total_votes = 0

#Candidate Options & votes (empty dictionary)
candidate_options = []
candidate_votes = {}

#Winning Candidate & count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read headers
    headers = next(file_reader)

    #Print each row, add 1 to total votes, & print total votes
    for row in file_reader:
      total_votes += 1

    #Print the candidate name from each row
      candidate_name = row[2]

      if candidate_name not in candidate_options:
    #Add candidate name to the list and set them to zero
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0

     #Add one vote each time   
      candidate_votes[candidate_name] += 1

#Add total votes, make percentage, and decide winner
for candidate_name in candidate_votes:
  votes = candidate_votes[candidate_name]
  votes_percentage = float(votes)/float(total_votes)*100

  print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")


  if (votes > winning_count) and (votes_percentage > winning_percentage):
    winning_count = votes
    winning_percentage = votes_percentage
    winning_candidate = candidate_name

winning_candidate_summary = (
  f"-------------------------\n"
  f"Winner: {winning_candidate}\n"
  f"Winning Vote Count: {winning_count:,}\n"
  f"Winning Percentage: {winning_percentage:.1f}%\n"
  f"-------------------------\n")
print(winning_candidate_summary)





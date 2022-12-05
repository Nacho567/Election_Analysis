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

with open(file_to_save, "w") as txt_file:

  #Print final vote count to terminal
  election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

  print(election_results, end="")

  txt_file.write(election_results)

  #Add total votes, make percentage, and decide winner
  for candidate_name in candidate_votes:
    #Retrieve vote count and percent
    votes = candidate_votes[candidate_name]
    votes_percentage = float(votes)/float(total_votes)*100
    candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
    #Print voter counts & percent to terminal
    print(candidate_results)
    #Save results to text file
    txt_file.write(candidate_results)

    #Determine winning vote count, percent, and candidate
    if (votes > winning_count) and (votes_percentage > winning_percentage):
      winning_count = votes
      winning_percentage = votes_percentage
      winning_candidate = candidate_name

  #Print winner to terminal
  winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

  print(winning_candidate_summary)
  #Save winner to text file
  txt_file.write(winning_candidate_summary)
  

  











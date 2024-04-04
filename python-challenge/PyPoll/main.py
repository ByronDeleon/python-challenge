#import modules
import os
import csv

#Set csv paths
csvpath=os.path.join('PyPoll', 'Resources','election_data.csv')
outputpath=os.path.join('PyPoll','Analysis','vote_results.txt')


# Total Vote Counter
tot_votes = 0

# Candidate Options and Vote Counting
candidates_running = []
candidate_votes = {}

# Winner the election and winner count of votes
win_cand = ""
win_count = 0

# Make Dictionary,read the csv, count the votes
with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

    # Count Rows for Candidates
    for row in reader:
        
        # Add to  vote count
        tot_votes = tot_votes + 1

        # Get candidates name from row
        cand_name = row["Candidate"]

        # If the candidate does not match any existing candidate...
       
        if cand_name not in candidates_running:

            # Append the list of candidates running
            candidates_running.append(cand_name)

            #Tracking candidate's voter count
            candidate_votes[cand_name] = 0

        # Add a vote to candidate's vote count
        candidate_votes[cand_name] = candidate_votes[cand_name] + 1


# Print the results and write to text file
with open(outputpath, "w") as txt_file:

    # Print the final vote count to terminal screen
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {tot_votes}\n"
        f"-------------------------\n\n"
        f"Total Votes For Each Candidate \n\n"
        )
    
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)


    # Loop thru votes to find the winner
    for candidate in candidate_votes:

        # Get votes count and percentage
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(tot_votes) * 100

        # Finf winning vote count and candidate
        if (votes > win_count):
            win_count = votes
            win_cand = candidate

        # Print each candidate vote count and % of votes  (to terminal)
        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's vote count and % to .txt file
        txt_file.write(voter_output)


    # Print the winner to terminal
    win_cand_summary = (
        "\n"
        f"-------------------------\n"
        f"Winner: {win_cand}\n"
        f"-------------------------\n")
    print(win_cand_summary)



    # Write winner to  text file
    txt_file.write(win_cand_summary)
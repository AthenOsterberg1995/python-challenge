import os
import csv

def main():
    #find csv file path
    #code for finding file path from class 3.2 activity Stu_ReadComicBooksCSV
    csvpath = os.path.join("..","PyPoll" ,"Resources", "election_data.csv")
    print(csvpath)

    #create list for candidates and number of votes cast
    candidate_list = []
    vote_count_list = []

    #read csv
    #code for reading csv from class 3.2 activity Stu_ReadComicBooksCSV
    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        #Get header so it's not added to list elements
        csv_header = next(csvreader) 
        
        #read rows and add values to lists
        for row in csvreader:
            #code to check if value is in list and finding index of element
            #https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
            #if the candidate in the current is not in the candidate list, add them to the list and
            #add a vote for them in the vote count
            #This ensures candidate name and vote count share the same index in their respective lists
            if str(row[2]) not in candidate_list:
                candidate_list.append(str(row[2]))
                vote_count_list.append(1)
            #if the candidate is already in our list, increase the vote count in the vote count
            #list at the same index as the candidate in the candidate list
            else:
                vote_count_list[candidate_list.index(str(row[2]))] += 1
    
    #find total votes
    total_votes = GetTotalVotes(vote_count_list)
    #create a list to hold percentage of votes for later
    percent_vote_list = GetPercentVotes(vote_count_list,total_votes)
    #find the winner
    election_winner = str(candidate_list[GetWinner(vote_count_list)])
    WriteAndPrintAnalysis(total_votes,candidate_list,percent_vote_list,vote_count_list,election_winner)
    

def GetTotalVotes(candidate_vote_count):
    #loop through vote count list and add all the values for total votes
    total = 0
    for vote_count in candidate_vote_count:
        total += int(vote_count)
    return total

def GetPercentVotes(candidate_vote_count, total_vote_count):
    #find the percentage of the vote each candidate had and return a list of those percentages 
    #with same index as the candidate and count
    percent_list = []
    #loop through each value in the vote count list and divide by total votes for percentage and return
    #a list with the percents at the same index as candidate name and vote count
    for vote_count in candidate_vote_count:
        percent_list.append(round(int(vote_count)/total_vote_count*100,3))
    return percent_list

def GetWinner(candidate_vote_count):
    #find the list index of the winner
    winner_index = 0
    winner_value = 0
    #loop through vote count list, if the current value is greater than what's stored in winner_value,
    #set a new winner value and the new index equal to whatever index the loop is at
    for vote_count in range(0,len(candidate_vote_count)):
        if int(candidate_vote_count[vote_count]) > winner_value:
            winner_index = vote_count
            winner_value = int(candidate_vote_count[vote_count])
    return winner_index

def WriteAndPrintAnalysis(total_vote_count,candidates,candidate_percent_votes,candidate_votes,winner):
    #create a list of values to output to terminal and text file
    output_list = ["Election Results", 
                   "-------------------------",
                   f"Total Votes: {total_vote_count}",
                   "-------------------------"]
    for index in range(0,len(candidates)):
        output_list.append(f"{candidates[index]}: {candidate_percent_votes[index]}% ({candidate_votes[index]})")
    output_list.append("-------------------------")
    output_list.append(f"Winner: {winner}")
    output_list.append("-------------------------")
    #Copied write and print from PyBank code
    #print statements to match output in example
    for line in output_list:
        print(str(line))

    #write results to text file
    #code from https://www.pythontutorial.net/python-basics/python-write-text-file/
    with open('Analysis.txt','w') as f:
        for line in output_list:
            f.write(line)
            #\n to output to next line
            f.write("\n")               
main()
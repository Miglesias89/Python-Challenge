#Import os module
import os

#Import module to read CSV files
import csv



csvpath=os.path.join('..','PyRoll','election_data.csv')

#Read CSV module
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    #Read the header row first
    headerrow=next(csvreader,None)

    #Set variable 
    candidate_vote={}
    candidate_name= []
    
    for row in csvreader:
        candidate=row[2]

        if candidate not in candidate_name:
            candidate_name.append(candidate)
            candidate_vote[candidate]=1

        candidate_vote[candidate]=candidate_vote[candidate]+1
    
    total_votes=sum(candidate_vote.values())
    
    percentage=[]
    print ("Election Results")
    print ("--------------------")
    output=(
        f'\nElection Results\n'
        f'---------------------------\n')

    print(f'Total Votes: {total_votes}')
    print('----------------------')

    #Percent of vote per candidate
    for candidate in candidate_vote:
        percentage=((candidate_vote[candidate]/total_votes)*100)

        print(f'{candidate}:{percentage:.2f}% ({candidate_vote[candidate]})')
        output += f'{candidate}:{percentage:.2f}% ({candidate_vote[candidate]}))\n'

    for winner in candidate_vote.keys():
        if candidate_vote[winner]==max(candidate_vote.values()):
            candidate_win=winner

    print('----------------------')
    print (f'Winner: {candidate_win} ')
    output += (f'Winner: {candidate_win}')

    text_path=os.path.join("election_data.txt")
    with open(text_path,"w") as txtfile:
        txtfile.write(output)




  
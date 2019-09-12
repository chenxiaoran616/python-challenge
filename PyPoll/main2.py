import os
import csv
import collections

#store file path to PyPoll
PyPoll=os.path.join('Resources','election_data.csv')
print(PyPoll)

#open up file
with open(PyPoll, newline='') as csvfile:

    PyPollreader = csv.reader(csvfile, delimiter=',')
    #store the headerline
    PyBank_header = next(PyPollreader)
    #convert data to a list
    data =list(PyPollreader)
    #count and print the row number
    row_count=len(data)
    vote_cast=row_count
print("Total Votes:" + str(vote_cast))


with open(PyPoll, newline='') as csvfile:

    PyPollreader = csv.reader(csvfile, delimiter=',')
    PyBank_header=next(PyPollreader)

    #create an empty list for candidates' names
    cleaned_candidates=[]
    #using loop to add names to the empty list
    for row in PyPollreader:
        if row[2] not in cleaned_candidates:
            cleaned_candidates.append(row[2])
            #print out candidates' name in terminal
            print(row[2])

candidates=collections.Counter()
with open(PyPoll, newline='') as csvfile:

    PyPollreader = csv.reader(csvfile, delimiter=',')
    PyBank_header=next(PyPollreader)

    #using for loop to count how many times each candidate is voted
    for names in PyPollreader:
        candidates[names[2]]+=1
    print(candidates['Khan'])
    print(candidates['Correy'])
    print(candidates['Li'])
    print(candidates["O'Tooley"])

    #calculate and print vote percentage for each candidate
    Khan_rate=candidates['Khan']/vote_cast
    print(Khan_rate)
    Correy_rate=candidates['Correy']/vote_cast
    print(Correy_rate)
    Li_rate=candidates['Li']/vote_cast
    print(Li_rate)
    OTooley_rate=candidates["O'Tooley"]/vote_cast
    print(OTooley_rate)













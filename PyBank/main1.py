import os
import csv

PyBankpath=os.path.join('Resources','budget_data.csv')
print(PyBankpath)

with open(PyBankpath, newline='') as csvfile:

    PyBankreader = csv.reader(csvfile, delimiter=',')
    #recoganize the header line
    PyBank_header = next(PyBankreader)
    #convert data in CSV into a list
    data =list(PyBankreader)
    #count the length of the list
    row_count=len(data)
    months=row_count-1
print("Total Months:" + str(months))


with open(PyBankpath, newline='') as csvfile:

    PyBankreader = csv.reader(csvfile, delimiter=',')
   
    headerline=next(csvfile)
    #calculate total profit using for loop
    total=0
    for row in PyBankreader:
        total+=int(row[1])
    print("Total :$"+str(total))

# set up a function to calculate average
def Average(list):
    return sum(list)/len(list)
with open(PyBankpath, newline='') as csvfile:

    PyBankreader = csv.reader(csvfile, delimiter=',')
    
    headerline=next(csvfile)
    #create a list for "Profit" column in the CSV file
    profit=[]
    for col in PyBankreader:
        profit.append(col[1])
    #calculate difference of each period and form a list for all differences
    differences=[]
    for index in range(1,len(profit)):
        differences.append(int(profit[index])-int(profit[index-1]))
    #print out the average, maximun and minimum value from the list
    print("Average Change: "+str(Average(differences)))
    print("Greatest Increase in profit: "+str(max(differences)))
    print("Greatest Decrease in profit: "+str(min(differences)))










    









    

    







    
        


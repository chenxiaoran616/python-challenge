import os
import csv

PyBankpath=os.path.join('Resources','budget_data.csv')
print(PyBankpath)

with open(PyBankpath, newline='') as csvfile:

    PyBankreader = csv.reader(csvfile, delimiter=',')

    #print(PyBankreader)

    PyBank_header = next(PyBankreader)
    #print(f"CSV Header: {PyBank_header}")

    #for row in PyBankreader:
        #print(row)
    data =list(PyBankreader)
    row_count=len(data)
    months=row_count-1
print("Total Months:" + str(months))


with open(PyBankpath, newline='') as csvfile:

    PyBankreader = csv.reader(csvfile, delimiter=',')
   
    headerline=next(csvfile)
    total=0
    for row in PyBankreader:
        total+=int(row[1])
    print("Total :$"+str(total))


def Average(list):
    return sum(list)/len(list)
with open(PyBankpath, newline='') as csvfile:

    PyBankreader = csv.reader(csvfile, delimiter=',')
    
    headerline=next(csvfile)
    profit=[]
    for col in PyBankreader:
        profit.append(col[1])

    differences=[]
    for index in range(1,len(profit)):
        differences.append(int(profit[index])-int(profit[index-1]))
    #print(differences)
    print("Average Change: "+str(Average(differences)))
    print("Greatest Increase in profit: "+str(max(differences)))
    print("Greatest Decrease in profit: "+str(min(differences)))
    









    









    

    







    
        


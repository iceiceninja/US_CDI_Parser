# importing csv module
import csv
# csv file name
filename = "U.S._Chronic_Disease_Indicators__CDI_.csv"

# initializing the titles and rows list
fields = []
rows = []
dataDic  =   {}

count = 0
numOfInputs = 0

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    # extracting field names through first row
    fields = next(csvreader)
    # row_count = sum(1 for row in csvreader)
    # numOfInputs = row_count

    # extracting each data row one by one
    numOfInputs = int(input("How many rows do you wish to use? type -1 for all:   "))
    for row in csvreader:
        if(numOfInputs != -1):
            if(count < numOfInputs):    #number in if statement is how many rows you read in. Remove this if statement if you want all lines
                rows.append(row)
                count+=1
            else:
                break
        else:
            rows.append(row)
print("rows: ",len(rows))

for row in rows[:numOfInputs]:   
    # parsing each column of a row
    if(row[3] in dataDic):
        if(row[5] in dataDic[row[3]]):
            dataDic[row[3]][row[5]] += 1
        else:
            dataDic[row[3]].update({row[5] : 1}) 
    else:
        dataDic[row[3]] = {row[5] : 1}


def searchDisease(disease):
    sumDisease = 0
    for state in dataDic:
        # print(state, dataDic[state].keys())
        if(disease in dataDic[state].keys()):
            print(state,dataDic[state][disease])
            sumDisease+=dataDic[state][disease]
    print(sumDisease)

def stateStats(state):
    print(state,dataDic[state])

query = int(input("Do you want to sort by state (0) or disease (1)   "))
if(query == 0):
    stateStats(input("Which state?      "))
elif(query == 1):
    searchDisease(input("Which disease?     "))

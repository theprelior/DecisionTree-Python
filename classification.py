'''
The price of the car with 4 categories: 1 to 4
Maintenance prices with 4 categories: 1 to 4
Number of doors with 4 categories: 2 to 5
Capacity of the car (number of persons that fit) with 3 categories: 2,4,6
Luggage size with 3 categories: 1 to 3 
Safety with 3 categories: 1 to 3
'''
from decimal import *

from IPython.display import display
import pandas as pd
import numpy as np
import cmath 
df = pd.read_excel('trainDATA.xlsx')
dfprice=df['Price'].values
dfmaint=df['MaintPrice'].values
dfdoors=df['NoofDoors'].values
dfpersons=df['Persons'].values
dflugsize=df['Lug_size'].values
dfsafety=df['Safety'].values
dfresults=df['Car Acceptibility'].values

countOfYes=0
countOfNo=0
lenOfdata=len(dfresults)


dictOfPrice=dict([(1, [0,0,0]), (2, [0,0,0]),(3, [0,0,0]),(4, [0,0,0])])
dictOfMaint=dict([(1, [0,0,0]), (2, [0,0,0]),(3, [0,0,0]),(4, [0,0,0])])
dictOfDoors=dict([(2, [0,0,0]), (3, [0,0,0]),(4, [0,0,0]),(5, [0,0,0])])
dictOfPersons=dict([(2, [0,0,0]), (4, [0,0,0]),(6, [0,0,0])])
dictOfLugsize=dict([(1, [0,0,0]), (2, [0,0,0]),(3, [0,0,0])])
dictOfSafety=dict([(1, [0,0,0]), (2, [0,0,0]),(3, [0,0,0])])

print(Decimal('10').logb())


def specificGain(dictOfAny,lenOfData):
    gain=0
    print(dictOfAny)
    for i in dictOfAny:
        gain=gain+(dictOfAny[i][0]/lenOfData)*computeInfoD(dictOfAny[i][1],dictOfAny[i][2],lenOfData)
    return gain





def eachEntity(dfResult,dfOfAny,dictOfAny,lenOfdata):
    for i in range(lenOfdata):
        if dfOfAny[i]==1:
            internalDict={1:[dictOfAny.get(1)[0]+1,dictOfAny.get(1)[1],dictOfAny.get(1)[2]]}
            dictOfAny.update(internalDict)
            if dfResult[i]==1:
                internalDict={1:[dictOfAny.get(1)[0],dictOfAny.get(1)[1]+1,dictOfAny.get(1)[2]]}
                dictOfAny.update(internalDict)
            elif dfResult[i]==2:
                internalDict={1:[dictOfAny.get(1)[0],dictOfAny.get(1)[1],dictOfAny.get(1)[2]+1]}
                dictOfAny.update(internalDict)
        elif dfOfAny[i]==2:
            internalDict={2:[dictOfAny.get(2)[0]+1,dictOfAny.get(2)[1],dictOfAny.get(2)[2]]}
            dictOfAny.update(internalDict)
            if dfResult[i]==1:
                internalDict={2:[dictOfAny.get(2)[0],dictOfAny.get(2)[1]+1,dictOfAny.get(2)[2]]}
                dictOfAny.update(internalDict)
            elif dfResult[i]==2:
                internalDict={2:[dictOfAny.get(2)[0],dictOfAny.get(2)[1],dictOfAny.get(2)[2]+1]}
                dictOfAny.update(internalDict)
        elif dfOfAny[i]==3:
            internalDict={3:[dictOfAny.get(3)[0]+1,dictOfAny.get(3)[1],dictOfAny.get(3)[2]]}
            dictOfAny.update(internalDict)
            if dfResult[i]==1:
                internalDict={3:[dictOfAny.get(3)[0],dictOfAny.get(3)[1]+1,dictOfAny.get(3)[2]]}
                dictOfAny.update(internalDict)
            elif dfResult[i]==2:
                internalDict={3:[dictOfAny.get(3)[0],dictOfAny.get(3)[1],dictOfAny.get(3)[2]+1]}
                dictOfAny.update(internalDict)
        elif dfOfAny[i]==4:
            internalDict={4:[dictOfAny.get(4)[0]+1,dictOfAny.get(4)[1],dictOfAny.get(4)[2]]}
            dictOfAny.update(internalDict)
            if dfResult[i]==1:
                internalDict={4:[dictOfAny.get(4)[0],dictOfAny.get(4)[1]+1,dictOfAny.get(4)[2]]}
                dictOfAny.update(internalDict)
            elif dfResult[i]==2:
                internalDict={4:[dictOfAny.get(4)[0],dictOfAny.get(4)[1],dictOfAny.get(4)[2]+1]}
                dictOfAny.update(internalDict)
        elif dfOfAny[i]==5:
            internalDict={5:[dictOfAny.get(5)[0]+1,dictOfAny.get(5)[1],dictOfAny.get(5)[2]]}
            dictOfAny.update(internalDict)
            if dfResult[i]==1:
                internalDict={5:[dictOfAny.get(5)[0],dictOfAny.get(5)[1]+1,dictOfAny.get(5)[2]]}
                dictOfAny.update(internalDict)
            elif dfResult[i]==2:
                internalDict={5:[dictOfAny.get(5)[0],dictOfAny.get(5)[1],dictOfAny.get(5)[2]+1]}
                dictOfAny.update(internalDict)
        elif dfOfAny[i]==6:
            internalDict={6:[dictOfAny.get(6)[0]+1,dictOfAny.get(6)[1],dictOfAny.get(6)[2]]}
            dictOfAny.update(internalDict)
            if dfResult[i]==1:
                internalDict={6:[dictOfAny.get(6)[0],dictOfAny.get(6)[1]+1,dictOfAny.get(6)[2]]}
                dictOfAny.update(internalDict)
            elif dfResult[i]==2:
                internalDict={6:[dictOfAny.get(6)[0],dictOfAny.get(6)[1],dictOfAny.get(6)[2]+1]}
                dictOfAny.update(internalDict)
    return dictOfAny
          

def findout(countOfYes,countOfNo):
    for i in dfresults:
        if i==1:
            countOfYes=countOfYes+1
        elif i==2:
            countOfNo=countOfNo+1
    return [countOfYes,countOfNo]

def computeInfoD(countOfYes,countOfNo,length):
    yesC=countOfYes/length
    noC=countOfNo/length
    result=-yesC*cmath.log(yesC,2)-noC*cmath.log(noC,2)
    return result

#print(-9/14*math.log(9/14,2)-5/14*math.log(5/14,2))

countOfYes=findout(countOfYes,countOfNo)[0]
countOfNo=findout(countOfYes,countOfNo)[1]

infoD=computeInfoD(countOfYes,countOfNo,lenOfdata)
dictOfPrice=eachEntity(dfresults,dfprice,dictOfPrice,lenOfdata)
dictOfMaint=eachEntity(dfresults,dfmaint,dictOfMaint,lenOfdata)
dictOfDoors=eachEntity(dfresults,dfdoors,dictOfDoors,lenOfdata)
dictOfPersons=eachEntity(dfresults,dfpersons,dictOfPersons,lenOfdata)
dictOfLugsize=eachEntity(dfresults,dflugsize,dictOfLugsize,lenOfdata)
dictOfSafety=eachEntity(dfresults,dfsafety,dictOfSafety,lenOfdata)


'''
print(dictOfPrice)
print(dictOfMaint)
print(dictOfDoors)
print(dictOfPersons)
print(dictOfLugsize)
print(dictOfSafety)'''

print(specificGain(dictOfPrice,lenOfdata))
print(specificGain(dictOfMaint,lenOfdata))
print(specificGain(dictOfDoors,lenOfdata))
print(specificGain(dictOfPersons,lenOfdata))
print(specificGain(dictOfLugsize,lenOfdata))
print(specificGain(dictOfSafety,lenOfdata))



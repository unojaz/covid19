# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:03:53 2020

@author: Sajinu
"""


def getUpdatedLists(usedlist,leftlist,num):
    usedNumbers2=usedlist.copy()
    usedNumbers2.append(num)
    leftNumbers2=leftlist.copy()
    leftNumbers2.remove(num)
    return [usedNumbers2,leftNumbers2]
            


def getNextNumber(usedNumbers,leftNumbers,sumNumber):
    leftNumbers.sort()
    found=False
    if len(usedNumbers) in [0,1,2,3,5,6,7,9,10]:
        for num in leftNumbers:
            [usedNumbers2,leftNumbers2]=getUpdatedLists(usedNumbers,leftNumbers,num)
            if(getNextNumber(usedNumbers2,leftNumbers2,sumNumber)):
                usedNumbers=usedNumbers2
                leftNumbers=leftNumbers2
                break
    elif len(usedNumbers) in [4,8]:
        found=False
        if(len(usedNumbers)==4):
            sumUntil=sum(usedNumbers[0:4])
        elif(len(usedNumbers)==8):
            sumUntil=sum(usedNumbers[5:8])
        for num in leftNumbers:
            if(num+sumUntil==sumNumber):
                [usedNumbers2,leftNumbers2]=getUpdatedLists(usedNumbers,leftNumbers,num)
                if(len(usedNumbers)!=8):
                    if(getNextNumber(usedNumbers2,leftNumbers2,sumNumber)):
                        usedNumbers=usedNumbers2
                        leftNumbers=leftNumbers2
                        break
    elif len(usedNumbers) in [11]:
        sumUntil=sum(usedNumbers[9:11])
        for num in leftNumbers:
            if(num+sumUntil==sumNumber):
                [usedNumbers2,leftNumbers2]=getUpdatedLists(usedNumbers,leftNumbers,num)
                usedNumbers=usedNumbers2
                leftNumbers=leftNumbers2
                found=True
                break 
        if(found==True):
            print(usedNumbers)
    return found

sumNumber=40
leftNumbers=list(range(1,30))
usedNumbers=[]
getNextNumber(usedNumbers,leftNumbers,sumNumber)
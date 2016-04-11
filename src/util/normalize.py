#!/usr/bin/python


##########################################################################
# Normalization functions
# -normalize: Subtract min from each element of vector, then divide by max. [0,1]
# -normalizeMinMax: Subtract min from each element of vector, then divide by max-min. [0,1]
# -normalizeStandardize: Subtract mean from each element of vector, then divide by variance. [-2, 2]
# -normalizeDecimal: ?? [0,1]
##########################################################################


import math

'''
Normalizing by subtracting the min value and dividing by the max value.
This will put all the coordinates in the [0,1] range
'''
def normalize(someDict):
	newDict = {}
	for value in someDict:
		lst = someDict[str(value)]
		minNum = float(min(lst))
		maxNum = float(max(lst))
		temp = []
		#print lst
		for val in lst:
			temp.append((val - minNum) / maxNum)
		newDict[str(value)]	= temp
	return newDict

'''
Normalizing by subtracting the min value and dividing by the max value - min value.
This will put all the coordinates in the [0,1] range
'''
def normalizeMinMax(someDict):
	newDict = {}
	for value in someDict:
		lst = someDict[str(value)]
		minNum = float(min(lst))
		maxNum = float(max(lst))
		temp = []		
		for val in lst:
			temp.append((val - minNum) / (maxNum - minNum))
		newDict[str(value)]	= temp			
	return newDict

'''
# Normalizing by subtracting the mu value and dividing by the variance.
# This will put all the coordinates in the [-2,2] range
'''
def normalizeStandardize(someDict):
	newDict = {}	
	for value in someDict:
		lst = someDict[str(value)]
		minNum = float(min(lst))
		maxNum = float(max(lst))
		var = variance(lst)
		mu = mean(lst)
		temp = []
		for val in lst:
			temp.append((val - mu) / math.sqrt(var))
		newDict[str(value)] = temp	
	return newDict

'''
Normalizing  by moving the decimal point of values of feature X
This will put all the coordinates in the [0,1] range
'''
def normalizeDecimal(someDict):
	newDict = {}	
	for index , value in enumerate(someDict):
		lst = someDict[str(value)]
		k = max(math.ceil(math.log(max(lst),10)),math.ceil(math.log(min(lst),10)))
		temp = []
		for i, val in enumerate(lst):
			if k > 0:
				temp.append(val/math.pow(10,k))
			else:
				temp.append(val * math.pow(10,k))	
		newDict[str(value)] = temp
	return newDict



########### HELPERS ##############

'''
 These are helper functions for the normalization
'''
def mean(myList):
    meanVal = 0
    if(len(myList) == 0):
       return 0
    else:
       meanVal = sumList(myList,sumFunc)/len(myList)
       return meanVal
'''
Finds Variance
'''
def variance(myList):
    myMean = mean(myList)
    myLen = len(myList)
    temp = 0
    for i in range(myLen):
        temp += (myList[i] - myMean)**2 
    return temp / (myLen-1);
 
'''
returns the value
'''
def sumFunc(num):
     return num 

'''
Gets the sum of list
''' 
def sumList(myList, sumFunc):
    sum = 0
    for i in myList:
        sum = sum + i
    return sum


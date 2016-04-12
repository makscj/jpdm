#!/usr/bin/python

import random 

##########################################################################
# This is the dataset object which is used to encapsulate a given data file.
# Each dataset corresponds to one data file.
# Data is represented in dictionary:	Label --> Data vector (row)
##########################################################################

class Dataset:
	
	title = ""
	subtitle = ""
	excelColumnRange = ""
	dataMaxDimensionality = 0
	dataDictionary = {}
	reducedDataDictionary = {}
	reducedDimensionality = 0

	def __init__(self, title, subtitle, columnRange, dataDictionary):
		self.title = title;
		self.subtitle = subtitle;
		self.excelColumnRange = columnRange;
		self.dataMaxDimensionality = len(dataDictionary.values()[0])
		self.dataDictionary = dataDictionary;

	def getMaximumDimensionality(self):
		return self.dataMaxDimensionality

	# Return dictionary -- labels (strings) mapping to vectors (double arrays)
	def getVectors(self):
		return self.dataDictionary

	# Returns the title and subtitle for this dataset
	def getTitles(self):
		return [self.title, self.subtitle]

	##################################################################
	# FOR STORING/SETTING CURRENT "REDUCED" VERSION OF THIS DATASET
	def setReducedDictionary(self, newDictionary, kDimensionality):
		self.reducedDataDictionary = newDictionary
		self.reducedDimensionality = kDimensionality

	def getReducedDimensionality(self):
		return self.reducedDimensionality

	def getReducedVectors(self):
		return self.reducedDataDictionary
	##################################################################

	# Argument: Integer, x, that will be used to randomly choose
	# x columns to be activated.
	def getRandomVectorsByDimensionality(self, dimensionality):
		activeVectorsArray = []
		for i in range(0, dimensionality):
			r = random.randint(0, dataMaxDimensionality-1)
			while r in activeVectorsArray:
				r = random.randint(0, dataMaxDimensionality-1)
			activeVectorsArray.append(r)
		return self.getVectorsByArray(activeVectorsArray)


	# Argument: List of indices for activated columns
	# Returns vectors with only the specified columns activated
	def getVectorsByArray(self, activeVectorsArray):

		modifiedDataDictionary = {}

		for label in self.dataDictionary:
			newVector = []
			for i in range(0, self.dataMaxDimensionality): # For each column...
				if i in activeVectorsArray: # If active, add it to new vector
					try:
						newVector.append(self.dataDictionary[label][i])
					except:
						print "ERROR: Index out of range!"
			modifiedDataDictionary[label] = newVector

		# print modifiedDataDictionary
		return modifiedDataDictionary



	def toString(self, currentDictionary):
		s = "{"
		for label in currentDictionary:
			s+= "("+label+": "+str(currentDictionary[label])+")\n"
		s+="}"
		return s


	def toString(self):
		s = "{"
		for label in self.dataDictionary:
			s+= "("+label+": "+str(self.dataDictionary[label])+")\n"
		s+="}"
		return s

	# Returns the number of rows
	def getNumPoints(self):
		return len(self.dataDictionary)

	








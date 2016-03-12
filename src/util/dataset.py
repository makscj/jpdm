
import random 

class Dataset:
	
	title = ""
	subtitle = ""
	excelColumnRange = ""
	dataMaxDimensionality = 0
	dataDictionary = {}

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
		return self.dataDictionary;

	# Returns the title and subtitle for this dataset
	def getTitles(self):
		return [self.title, self.subtitle];

	# Argument: Integer, x, that will be used to randomly choose
	# x columns to be activated.
	def getRandomVectorsByDimensionality(self, dimensionality):
		activeVectorsArray = []
		for i in range(0, dimensionality):
			r = random.randint(0, dataMaxDimensionality-1)
			while r in activeVectorsArray:
				r = random.randint(0, dataMaxDimensionality-1)
			activeVectorsArray.append(r)
		return getVectorsByArray(activeVectorsArray)


	# Argument: List of indices for activated columns
	# Returns vectors with only the specified columns activated
	def getVectorsByArray(self, activeVectorsArray):

		modifiedDataDictionary = {}

		for label in dataDictionary:
			newVector = []
			for i in range(0, dataMaxDimensionality): # For each column...
				if i in activeVectorsArray: # If active, add it to new vector
					newVector.append(modifiedDataDictionary[label][i])
			modifiedDataDictionary[label] = newVector

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
	








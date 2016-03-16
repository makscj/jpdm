import sys
import random
sys.path.insert(0, '../util')
import cluster
import read
import dataset
import normalize
import distance



# Iterates through datasets, gets the largest possible dimensionality for 
# each dataset, then returns the minimum "maximum dimensionality." Use this 
# function to know the possible range of dimensionalities that are valad for a
# given group of datasets.
def getMinDimensionalityAcrossDatasets(datasets):
	minDimensionality = float('inf') 
	for d in datasets:
		tempMax = d.getMaximumDimensionality()
		if  tempMax < minDimensionality:
			minDimensionality = tempMax
	return minDimensionality

# Gets a list of <dimensionality> different random numbers, in the range
# 0-<dataMaxDimensionality>.
# Use this function to randomly generate an array of active columns
def getListOfRandomIndices(dimensionality, dataMaxDimensionality):
	activeVectorsArray = []
	for i in range(0, dimensionality):
		r = random.randint(0, dataMaxDimensionality-1)
		while r in activeVectorsArray:
			r = random.randint(0, dataMaxDimensionality-1)
		activeVectorsArray.append(r)
	return activeVectorsArray


# Arguments:
#	-datasets: List of dataset objects, for each of which a dictionary of labelled vectors will be returned
# 	-dimensionality: The number of columns/components to be used to form each vector
# 	-sameColumnsForAllDatasets: If true, the same set of random indices is used for each dataset. If false, a different set of random indices is used to create vectors for each dataset.
# Returns:
#	-A list of dictionaries (labell---> vector)
def randomlyConfigureActiveColumns(datasets, dimensionality, sameColumnsForAllDatasets):
	
	dataDictionaries = []

	minDimensionality = getMinDimensionalityAcrossDatasets(datasets)
	if dimensionality > minDimensionality: # Ensure dimensionality is suitable for all datasets.
		print "ERROR 1:", dimensionality, "-dimensional vectors cannot be generated for the datasets you are currently using because one or more of the datasets does not have enough data/columns."

	activeColumns = False
	if sameColumnsForAllDatasets:
		activeColumns = getListOfRandomIndices(dimensionality, minDimensionality)

	for d in datasets:
		if sameColumnsForAllDatasets:
			dataDictionaries.append(d.getVectorsByArray(activeColumns))
		else:
			dataDictionaries.append(d.getRandomVectorsByDimensionality(dimensionality))

	return dataDictionaries

# Arguments:
#	-list of datasets
# 	-list of indice arrays--an array for each dataset.
#	-If sameArrayForAll is true, use the same list of indices for all datasets. In this case, the second argument is a single list of indices.
def explicitlyConfigureActiveColumns(datasets, listOfActiveIndices, sameArrayForAll):
	
	dataDictionaries = []

	if sameArrayForAll:
		activeColumns = listOfActiveIndices
		for d in datasets:
			dataDictionaries.append(d.getVectorsByArray(activeColumns))
	else:
		for i in range(0, len(listOfActiveIndices)):
			dataDictionaries.append(datasets[i].getVectorsByArray(listOfActiveIndices[i]))

	return dataDictionaries


# Takes a list of dictionaries and returns a single dictionary

def crunchDictionaryList(dictionaries):
	bigDictionary = {}
	for d in dictionaries:
		items = d.items()
		for i in items:
			bigDictionary[i[0]] = i[1]
	return bigDictionary


def experiment1(datasets):

	##############---VECTOR CONFIGURATION---###############

	# Configure data, resulting in a list of dictionaries (labels-->vectors)
	# There is a dictionary for each dataset, stored in the same order as in the datasets list
	# dataDictionaries = randomlyConfigureActiveColumns(datasets, 5, True)
	dataDictionaries = explicitlyConfigureActiveColumns(datasets, [0,1,2,3], True) # OR

	##############---VECTOR NORMALIZATION---###############

	# At this point, have list of dictionaries. Each dictionary contains labels mapping to vectors.
	# All of the vectors are the same dimensionality, build in the way that we specified for configuration.
	normalizedDictionaries = []
	for d in dataDictionaries:
		# print d, "\n"
		normalizedDictionaries.append(normalize.normalize(d)) # THERE ARE ALSO OTHER WAYS TO NORMALIZE


	##############---CLUSTERING---###############
	numClusters = 3
	clusters = cluster.gonzalez(crunchDictionaryList(normalizedDictionaries), numClusters, distance.euclidean);


	for i in range(0, numClusters):
		for c in clusters:
			if c[1]==i:
				print c[0]




if __name__ == "__main__":
	# Read data files.
	reader = read.Read(False)
	# Get data as list of dataset objects.
	datasets = reader.getDataSets()
	experiment1(datasets)



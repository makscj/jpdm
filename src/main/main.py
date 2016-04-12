#!/usr/bin/python

import sys
import random
import itertools
import datetime
sys.path.insert(0, '../util')
import cluster
import read
import dataset
import normalize
import distance
import regression


##############################################################
# Experiment Template
##############################################################

# ------------------------------------------------------------
# RUN EXPERIMENT FOR EVERY POSSIBLE N
# ------------------------------------------------------------

# def experiment1(datasets):

# ------------------------------------------------------------
# PART 1: CHOOSING DATA
# ------------------------------------------------------------
	###############---VECTOR CONFIGURATION---################

	# < Put work here -- this is where we choose columns>

	###############---REDUCTION WITH REGRESSION---################

	# < Put work here -- if desired, use regression to reduce dimensionality/columns to uniform k>

# ------------------------------------------------------------
# PART 2: NORMALIZATION AND CHOOSING DISTANCE MEASURE 
# ------------------------------------------------------------

	###############---VECTOR NORMALIZATION---################

	# < Put work here >

# ------------------------------------------------------------
# PART 3: RUN
# ------------------------------------------------------------

	###################---CLUSTERING---#####################

	# < Put work here >

# ------------------------------------------------------------
# PART 4: WRITE RESULTS 
# ------------------------------------------------------------
	##################---STORE RESULTS---####################

	# Prepare to write experiment file -- fill in the below values for this experiment.

	# clusteringAlgorithmInfo = "gonzalez"
	# distanceMeasurementInfo = "euclidean"
	# vectorConfigurationInfo = "explicitly configured, same columns used across datasets, Indices used: [0,1,2,3]"

	# writeFile(1, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo, clusters)


##############################################################
##############################################################


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


def writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo, vectorConfigurationInfo, otherNotes, clusters):

	now = datetime.datetime.now()
	month = now.month
	day = now.day
	hour = now.hour
	minute = now.minute

	filename = '../../results/exp'+str(expIndex)+"/"+str(expIndex)+'_'+str(month)+'.'+str(day)+'_'+str(hour)+'.'+str(minute)+'_K.'+str(numClusters)
	f = open(filename,'w')

	f.write("CONFIGURATION DETAILS:\n\n")
	f.write("Experiment index: "+str(expIndex)+"\n")
	f.write("Number of clusters: "+str(numClusters)+"\n\n")
	f.write("Clustering algorithm: "+clusteringAlgorithmInfo+"\n")
	f.write("Distance measurement: "+distanceMeasurementInfo+"\n")
	print vectorConfigurationInfo
	f.write("Vector configuration: "+vectorConfigurationInfo+"\n")
	f.write("Notes: "+otherNotes+"\n")

	for i in range(0, numClusters):
		# print "Cluster: ", i
		f.write("\nCLUSTER "+str(i)+":\n\n")
		for key, val in clusters.iteritems():
			if val==i:
				f.write("\t"+key)

	f.close()




def experiment1(datasets, numClusters):

	###############---VECTOR CONFIGURATION---################

	# Configure data, resulting in a list of dictionaries (labels-->vectors)
	# There is a dictionary for each dataset, stored in the same order as in the datasets list
	# dataDictionaries = randomlyConfigureActiveColumns(datasets, 5, True)
	# OR:
	dataDictionaries = explicitlyConfigureActiveColumns(datasets, [0,1,2,3], True) 

	###############---VECTOR NORMALIZATION---################

	# At this point, have list of dictionaries. Each dictionary contains labels mapping to vectors.
	# All of the vectors are the same dimensionality, build in the way that we specified for configuration.
	normalizedDictionaries = []
	for d in dataDictionaries:
		# print d, "\n"
		normalizedDictionaries.append(normalize.normalize(d)) # THERE ARE ALSO OTHER WAYS TO NORMALIZE

	###################---CLUSTERING---#####################
	clusterResults = cluster.gonzalez(crunchDictionaryList(normalizedDictionaries), numClusters, distance.euclidean);

	##################---STORE RESULTS---####################

	# Prepare to write experiment file
	clusteringAlgorithmInfo = "gonzalez"
	distanceMeasurementInfo = "euclidean"
	vectorConfigurationInfo = "explicitly configured, same columns used across datasets, Indices used: [0,1,2,3]"

	writeFile(1, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo,"", clusterResults[1])




def experiment2(datasets, numClusters, dimensionality):

	# ------------------------------------------------------------
	# PART 1: CHOOSING DATA
	# ------------------------------------------------------------
	###############---VECTOR CONFIGURATION---################
	###############---REDUCTION WITH REGRESSION---################=
	for d in datasets:
		reducedDictionary = regression.getLowerSpace(d.getVectors(), dimensionality)
		d.setReducedDictionary(reducedDictionary, dimensionality)
	
	# ------------------------------------------------------------
	# PART 2: NORMALIZATION AND CHOOSING DISTANCE MEASURE 
	# ------------------------------------------------------------

	###############---VECTOR NORMALIZATION---################

	# At this point, have list of dictionaries of uniform dimensionality. 
	# Each dictionary contains labels mapping to vectors.
	normalizedDictionaries = []
	for d in datasets:
		# print d, "\n"
		# print d
		normalizedDictionaries.append(normalize.normalize(d.getReducedVectors())) # THERE ARE ALSO OTHER WAYS TO NORMALIZE

	# ------------------------------------------------------------
	# PART 3: RUN
	# ------------------------------------------------------------

	###################---CLUSTERING---#####################
	clusterResults  = cluster.gonzalez(crunchDictionaryList(normalizedDictionaries), numClusters, distance.euclidean);

	# ------------------------------------------------------------
	# PART 4: WRITE RESULTS 
	# ------------------------------------------------------------
	##################---STORE RESULTS---####################
	# def writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo, vectorConfigurationInfo, clusters):
	# Prepare to write experiment file -- fill in the below values for this experiment.

	clusteringAlgorithmInfo = "gonzalez"
	distanceMeasurementInfo = "euclidean"
	vectorConfigurationInfo = "{}, {}".format("configured using regression, reduced to dimensionality:", dimensionality)
	writeFile(2, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo, "Trying to get this thing to work!",clusterResults[1])



# datasets: Sets to be clustered 
# dimensionality: If >0, then set to this value, if <=0 set to maximum valid dimensionality for  this data.
def experiment3(datasets, dimensionality):

	# ------------------------------------------------------------
	# PART 1: CHOOSING DATA
	# ------------------------------------------------------------
	###############---VECTOR CONFIGURATION---################
	###############---REDUCTION WITH REGRESSION---################=
	for d in datasets:
		reducedDictionary = regression.getLowerSpace(d.getVectors(), dimensionality)
		d.setReducedDictionary(reducedDictionary, dimensionality)
	
	# ------------------------------------------------------------
	# PART 2: NORMALIZATION AND CHOOSING DISTANCE MEASURE 
	# ------------------------------------------------------------

	###############---VECTOR NORMALIZATION---################

	# At this point, have list of dictionaries of uniform dimensionality. 
	# Each dictionary contains labels mapping to vectors.
	normalizedDictionaries = []
	for d in datasets:
		# print d, "\n"
		# print d
		normalizedDictionaries.append(normalize.normalize(d.getReducedVectors())) # THERE ARE ALSO OTHER WAYS TO NORMALIZE

	# ------------------------------------------------------------
	# PART 3: RUN
	# ------------------------------------------------------------

	###################---CLUSTERING---#####################
	clusterResults  = cluster.gonzalez(crunchDictionaryList(normalizedDictionaries), numClusters, distance.euclidean);

	# ------------------------------------------------------------
	# PART 4: WRITE RESULTS 
	# ------------------------------------------------------------
	##################---STORE RESULTS---####################
	# def writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo, vectorConfigurationInfo, clusters):
	# Prepare to write experiment file -- fill in the below values for this experiment.

	clusteringAlgorithmInfo = "gonzalez"
	distanceMeasurementInfo = "euclidean"
	vectorConfigurationInfo = "{}, {}".format("configured using regression, reduced to dimensionality:", dimensionality)
	writeFile(2, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo, "Trying to get this thing to work!",clusterResults[1])



if __name__ == "__main__":
	# Read data files.
	reader = read.Read(False) # READS EVERYTHING
	# Get data as list of dataset objects.
	datasets = reader.getDataSets() # EVERY DATASET IS NOW AT YOUR DISPOSAL


	copy1 = list(datasets)
	# copy1.pop(0)
	experiment1(copy1, 3)

	copy2 = list(datasets)
	# copy2.pop(0)
	experiment2(copy2, 3, 2)



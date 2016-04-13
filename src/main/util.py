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

# All parameters are lists.
def writeCostFile(expIndex, maxClusters, centerCosts, meanCosts, clusterFileNames):

	if not (len(centerCosts)==len(meanCosts) and len(centerCosts)==len(clusterFileNames)):
		print "PROBLEM--NUMBER OF COSTS DOESNT MATCH NUMBER OF CLUSTER EXPERIMENTS."

	f = open('../../results/exp'+str(expIndex)+"/"+clusterFileNames[0]+"_CDF_POINTS",'w')
	f.write("CDF POINTS\n\n")

	f.write("CENTER COST POINTS (N, cost):\n")
	for c in range(1, maxClusters+1):
		f.write(str(c)+"\t"+str(centerCosts[c-1])+"\n")
	f.write("\nMEAN COST POINTS (N, cost):\n")
	for c in range(1, maxClusters+1):
		f.write(str(c)+"\t"+str(meanCosts[c-1])+"\n")


	f.write("\nCENTER COST POINTS (N, cost):\n[")
	for c in range(1, maxClusters+1):
		f.write("["+str(c)+","+str(centerCosts[c-1])+"];")
	f.write("]\n")
	f.write("\nMEAN COST POINTS (N, cost):\n[")
	for c in range(1, maxClusters+1):
		f.write("["+str(c)+","+str(meanCosts[c-1])+"];")
	f.write("]\n")
	f.write("\nCORRESPONDING CLUSTER FILES:\n")
	for name in clusterFileNames:
		f.write(name+"\n")
	f.close()


def writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo, vectorConfigurationInfo, otherNotes, clusters):

	now = datetime.datetime.now()
	month = now.month
	day = now.day
	hour = now.hour
	minute = now.minute
	second = now.second

	filename = str(expIndex)+'_'+str(day)+'_'+str(hour)+'.'+str(minute)+'.'+str(second)+'_K.'+str(numClusters)
	f = open('../../results/exp'+str(expIndex)+"/"+filename,'w')

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

	return filename



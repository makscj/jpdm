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
import util


##############################################################
# Experiment Template
##############################################################

# ------------------------------------------------------------
# RUN EXPERIMENT FOR EVERY POSSIBLE N
# ------------------------------------------------------------

# Automatically generates results for every N
# datasets: Sets to be clustered 
# dimensionality: If >0, then set to this value, if <=0 set to maximum valid dimensionality for  this data.
# def experiment1(datasets, dimensionality):

# ------------------------------------------------------------
# PART 1: ECTOR CONFIGURATION (CHOOSING COLUMNS) 
# ------------------------------------------------------------
	# "Manually" configure, or configure with regression:
	# < Put work here -- if desired, use regression to reduce 
	# dimensionality/columns to uniform k>

# ------------------------------------------------------------
# PART 2: CHOOSE NORMALIZATION AND DISTANCE FUNCTIONS
# ------------------------------------------------------------
	# < Put work here >

# ------------------------------------------------------------
# PART 3: RUN -- CHOOSE CLUSTERING ALGORITHM
# ------------------------------------------------------------
	# < Put work here >

# ------------------------------------------------------------
# PART 4: Get costs (if gonzalez or lloyds)
# ------------------------------------------------------------

# ------------------------------------------------------------
# PART 5: WRITE RESULTS 
# ------------------------------------------------------------
	# Use WriteFile function--- BE THOROUGH FOR GOODNESS SAKE!

##############################################################
##############################################################


def experiment1(datasets, numClusters):

	###############---VECTOR CONFIGURATION---################

	# Configure data, resulting in a list of dictionaries (labels-->vectors)
	# There is a dictionary for each dataset, stored in the same order as in the datasets list
	# dataDictionaries = randomlyConfigureActiveColumns(datasets, 5, True)
	# OR:
	dataDictionaries = util.explicitlyConfigureActiveColumns(datasets, [0,1,2,3], True) 

	###############---VECTOR NORMALIZATION---################

	# At this point, have list of dictionaries. Each dictionary contains labels mapping to vectors.
	# All of the vectors are the same dimensionality, build in the way that we specified for configuration.
	normalizedDictionaries = []
	for d in dataDictionaries:
		# print d, "\n"
		normalizedDictionaries.append(normalize.normalize(d)) # THERE ARE ALSO OTHER WAYS TO NORMALIZE

	###################---CLUSTERING---#####################
	clusterResults = cluster.gonzalez(util.crunchDictionaryList(normalizedDictionaries), numClusters, distance.euclidean);

	##################---STORE RESULTS---####################

	# Prepare to write experiment file
	clusteringAlgorithmInfo = "gonzalez"
	distanceMeasurementInfo = "euclidean"
	vectorConfigurationInfo = "explicitly configured, same columns used across datasets, Indices used: [0,1,2,3]"

	util.writeFile(1, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo,"", clusterResults[1])




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
	clusterResults  = cluster.gonzalez(util.crunchDictionaryList(normalizedDictionaries), numClusters, distance.euclidean);

	# ------------------------------------------------------------
	# PART 4: WRITE RESULTS 
	# ------------------------------------------------------------
	##################---STORE RESULTS---####################
	# def writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo, vectorConfigurationInfo, clusters):
	# Prepare to write experiment file -- fill in the below values for this experiment.

	clusteringAlgorithmInfo = "gonzalez"
	distanceMeasurementInfo = "euclidean"
	vectorConfigurationInfo = "{}, {}".format("configured using regression, reduced to dimensionality:", dimensionality)
	util.writeFile(2, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo, "Trying to get this thing to work!",clusterResults[1])


# Automatically generates results for every N
# datasets: Sets to be clustered 
# dimensionality: If >0, then set to this value, if <=0 set to maximum valid dimensionality for  this data.
def experiment3(datasets, dimensionality):

	expIndex = 3

	clusterFileNames=[]
	centerCosts = []
	meanCosts = []

	# First, find the number of examples between all datasets. 
	# This is the maximum number of clusters that can be made.
	maxClusters = 0
	for d in datasets:
		maxClusters+=d.getNumPoints()

	if(dimensionality<1):
		dimensionality = util.getMinDimensionalityAcrossDatasets(datasets)


	# --------------------------------------------------------------------------------------
	# --------------------------------------------------------------------------------------


	# Now, run experiment for every possible number of clusters
	for numClusters in range(1, maxClusters+1):

		# ------------------------------------------------------------
		# PART 1: CHOOSING DATA (columns)
		# ------------------------------------------------------------
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
			normalizedDictionaries.append(normalize.normalizeMinMax(d.getReducedVectors())) # THERE ARE ALSO OTHER WAYS TO NORMALIZE

		# ------------------------------------------------------------
		# PART 3: RUN
		# ------------------------------------------------------------
		###################---CLUSTERING---#####################
		crunchedData = util.crunchDictionaryList(normalizedDictionaries)
		clusterResults  = cluster.gonzalez(crunchedData, numClusters, distance.euclidean);

		# ------------------------------------------------------------
		# PART 4: Get costs (if gonzalez or lloyds)
		# ------------------------------------------------------------
		centerCosts.append(cluster.centerCost(crunchedData, clusterResults[0], clusterResults[1], distance.euclidean))
		meanCosts.append(cluster.meanCost(crunchedData, clusterResults[0], clusterResults[1], distance.euclidean))
		
		# ------------------------------------------------------------
		# PART 5: WRITE RESULTS 
		# ------------------------------------------------------------
		##################---STORE RESULTS---####################
		# def writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo, vectorConfigurationInfo, clusters):
		# Prepare to write experiment file -- fill in the below values for this experiment.

		clusteringAlgorithmInfo = "gonzalez"
		distanceMeasurementInfo = "euclidean"
		vectorConfigurationInfo = "{}, {}".format("configured using regression, reduced to dimensionality:", dimensionality)
		clusterFileNames.append(util.writeFile(expIndex, numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo, "Trying to get this thing to work!",clusterResults[1]))

	# --------------------------------------------------------------------------------------
	# --------------------------------------------------------------------------------------
	# WRITE COST INFO TO FILE
	util.writeCostFile(expIndex, maxClusters, centerCosts, meanCosts, clusterFileNames)



if __name__ == "__main__":

	#-----------------------------------
	# Read ALL data files.
	reader = read.Read(False) # READS EVERYTHING, and makes dataset objects from each T#.txt file
	# Get data as list of dataset objects.
	datasets = reader.getDataSets() # EVERY DATASET IS NOW AT YOUR DISPOSAL, and indices match dataset titles.
	#-----------------------------------

	# copy1 = list(datasets) # This is where you choose which tables you're using
	# copy1.pop(0)
	# experiment1(copy1, 3) # This is where you choose which tables you're using

	copy2 = list(datasets) # This is where you choose which tables you're using
	experiment3([copy2[0]], -1) # This is where you choose which tables you're using



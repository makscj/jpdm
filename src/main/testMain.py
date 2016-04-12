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

# def experiment1(datasets):

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
# PART 4: WRITE RESULTS 
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


# Automatically generates results for every N
# datasets: Sets to be clustered 
# dimensionality: If >0, then set to this value, if <=0 set to maximum valid dimensionality for  this data.
def experiment3(datasets, numClusters):

	# ------------------------------------------------------------
	# PART 1: CHOOSING DATA (columns)
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

	#-----------------------------------
	# Read ALL data files.
	reader = read.Read(False) # READS EVERYTHING, and makes dataset objects from each T#.txt file
	# Get data as list of dataset objects.
	datasets = reader.getDataSets() # EVERY DATASET IS NOW AT YOUR DISPOSAL, and indices match dataset titles.
	#-----------------------------------

	copy1 = list(datasets) # This is where you choose which tables you're using
	# copy1.pop(0)
	experiment1(copy1, 3) # This is where you choose which tables you're using

	copy2 = list(datasets) # This is where you choose which tables you're using
	# copy2.pop(0)
	experiment2([copy2[2]], 3, 2) # This is where you choose which tables you're using



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

def experiment2(datasets, numClusters, dimensionality):

	# ------------------------------------------------------------
	# PART 1: CHOOSING DATA
	# ------------------------------------------------------------
	###############---VECTOR CONFIGURATION---################
	###############---REDUCTION WITH REGRESSION---################=

	
	for d in datasets:
		
		reducedDictionary = regression.getReducedSpace(d.getVectors(), dimensionality)
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
		normalizedDictionaries.append(d.getReducedVectors()) # THERE ARE ALSO OTHER WAYS TO NORMALIZE

	# ------------------------------------------------------------
	# PART 3: RUN
	# ------------------------------------------------------------
#	print normalizedDictionaries
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
	util.writeFile("maks", numClusters, clusteringAlgorithmInfo, distanceMeasurementInfo,vectorConfigurationInfo, "Trying to get this thing to work!",clusterResults[1])



if __name__ == "__main__":

	#-----------------------------------
	# Read ALL data files.
	reader = read.Read(False) # READS EVERYTHING, and makes dataset objects from each T#.txt file
	# Get data as list of dataset objects.
	datasets = reader.getDataSets() # EVERY DATASET IS NOW AT YOUR DISPOSAL, and indices match dataset titles.
	#-----------------------------------
	experiment2([datasets[0]], 3, 1);
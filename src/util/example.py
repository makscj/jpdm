#!/usr/bin/python

import distance
import cluster
import regression
import numpy as np


def kprint(keys, phi):
	for key in keys:
		cluster = phi[key];
		print "{}: {}".format(key,cluster);
	print "----------"

raw = [[11.5377, 12.6501], [12.8339, 17.0349], [8.7412, 14.7254], [11.8622, 13.9369], [11.3188, 14.7147], [9.6923, 13.7950], [10.5664, 13.8759], [11.3426, 15.4897], [14.5784, 15.4090], [13.7694, 15.4172], [-10.3285, 8.3884], [-12.2075, 6.3529], [-10.2828, 6.4311], [-9.3698, 6.6905], [-10.5111, 4.5557], [-9.9653, 8.9384], [-10.2731, 7.8252], [-11.3034, 6.7451], [-10.7061, 8.8703], [-11.7873, 5.7885], [11.8978, -7.4637], [11.7586, -6.5226], [12.3192, -7.8141], [12.3129, -7.7135], [11.1351, -6.6068], [11.9699, -5.0674], [11.8351, -7.3697], [12.6277, -6.2286], [13.0933, -6.8256], [13.1093, -5.4826]]

data = {};

count = 1;
char = 'a';
keys = [];
for ls in raw:
	if count == 11:
		if(char == 'a'):
			char = 'b';
		else:
			char = 'c';
		count = 1;
	key = "{}{}".format(char,count);
	keys.append(key);
	data[key] = ls;
	count += 1;



#print "---------"
(n_gonz_c, n_gonz_p) = cluster.gonzalez(data, 3, distance.euclidean);
#print n_gonz_p;
(n_ll_c, n_ll_p) = cluster.lloyds(data, 3, distance.euclidean);
#print n_ll_p;
#print "--------"
(hi_c,hi_p) = cluster.hierarchical(data, 3, cluster.completelink);

kprint(keys, n_gonz_p);
kprint(keys, n_ll_p);
kprint(keys, hi_p);



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
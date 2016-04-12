#!/usr/bin/python

##########################################################################
# This file contains ALL of our clustering algorithmsa and cost functions
#
# Clustering algorithms:
#	-Gonazalez (K-center)
#	-Lloyds (K-means) 
#	-Hierarchical (single link, complete link and mean link)
# Cost functions:
#	-Center cost
#	-Mean cost
#
# How to use these (high level):
# Clustering: Call them, and provide distance measure argument (where 
#	applicable)
# Cost functions: Take data, centers, phi, and distance and return cost. 
# 	(so, call AFTER you've done all clustering)
#
# Note: For experimentation, may not use hierarchical often--we don't have 
# a cost function for it.
##########################################################################

import itertools
import distance
import random


'''
data - the data to be clustered, represented as a {string=>list} dictionary
k - The number of desired clusters
link - the link distance to use for computing 'closest' clusters.

returns a dictionary of {string=>integer}, where each key corresponds to a key in the data
dictionary, and every integer is the cluster it belongs to. 
'''
def hierarchical(data, k, link):

	#
	#	This comprehension creates a dictionary where the keys are all the keys from the data file, and all the
	#	values are unique integers from [|data.keys()|]. In other words, assigning each key to a unique integer
	#	which corresponds to assigning each key a different cluster. 

	#	Note, this may now be irrelevant --- phi is never set until the end, so we could just initialize phi to be
	#	an empty dictionary.
	#
	#phi = {v[0]:v[1] for v in zip(data.keys(), [v for v in range(len(data.keys()))])};

	phi = {};

	# Assign each label to a cluster
	clusters = [[ke] for ke in data.keys()];

	# Keep track of the number of clusters we have
	number_of_clusters = len(data.keys());


	# While we have not found k clusters
	while(number_of_clusters > k):

		# Find the closest two clusters
		mini = float('inf');
		minj = float('inf');
		mind = float('inf');
		for i in range(len(clusters)):
			for j in range(i+1, len(clusters)):
				dist = link(clusters[i], clusters[j], data);
				if(dist < mind):
					mini = i;
					minj = j;
					mind = dist;

		# Merge the closest clusters
		clusters[mini] = clusters[mini] + clusters[minj];
		del clusters[minj];
		number_of_clusters -= 1;

	# Compute the final phi values
	cval = 0;
	for cluster in clusters:
		for val in cluster:
			phi[val] = cval;
		cval += 1;

	return (clusters,phi);

'''
Method that runs the Gonzalez greedy algorithm for k-Center Clustering.

data - dictionary of {string=>list}
k - integer, the number of desired clusters
distance - function, the distance metric we want to use

returns a dictionary of {string=>integer}, where each key corresponds to a key in the data
dictionary, and every integer is the cluster it belongs to. 
'''
def gonzalez(data, k, distance):
	# Initialize every point to the first cluster
	phi = {v:0 for v in data.keys()};

	# Create the list of cluster centers
	c = [0 for v in range(k)];
	# Arbitrarily choose the first cluster center
	initial = random.randrange(0,len(data.keys()));
	c[0] = data[data.keys()[initial]];
	# Loop through the number of clusters we want
	for i in range(1,k):
		# Find the point farthest away from it's current assigned cluster center
		Max = 0;
		c[i] = 0;
		for (key,val) in data.iteritems():
			dist = distance(val,c[phi[key]])
			if(dist > Max):
				Max = dist;
				c[i] = val;
		#print c[i]
		# Find the closest cluster center to each point
		for key,val in data.iteritems():
			if distance(val,c[phi[key]]) > distance(val, c[i]):
				phi[key] = i;
	return (c, phi); # List of centers, dictionary of phis ==> Labels mapped to center index


def lloyds(data, k, distance):
	keys = data.keys();
	phi = {v:0 for v in keys};
	c = [[] for i in range(k)];
	rando = random.sample(range(len(keys)), k);
	hasNotChanged = lambda x,y: collections.Counter(x) == collections.Counter(y);
	for i in range(k):
		c[i] = data[keys[rando[i]]];

	for loop in range(50):

		for (key,val) in data.iteritems():
			mind = float('inf');
			mini = 0;
			for i in range(k):
				dist = distance(val, c[i])
				if(dist < mind):
					mind = dist;
					mini = i;
			phi[key] = mini;

		for i in range(k):
			avg = [0]*len(c[i]);
			count = 0;
			for key,val in data.iteritems():
				if(phi[key] == i):
					for dim in range(len(avg)):
						avg[dim] += val[dim];
					count += 1;
			for dim in range(len(avg)):
				avg[dim] /= count;
			c[i] = avg;
	return (c,phi)

def singlelink(set1, set2, data):
	# Create a list of lists for each list in data corresponding to set 1
	lists1 = [data[val] for val in set1];
	# Create a list of lists for each list in data corresponding to set 2
	lists2 = [data[val] for val in set2];
	# Compute the Cartesian product of the vectors in set1 and set2
	cartesian = [element for element in itertools.product(lists1, lists2)];
	
	# Find the minimum distance in the Cartesian product.
	Min = float("inf");
	for pair in cartesian:
		dist = distance.euclidean(pair[0], pair[1]);
		if(dist < Min):
			Min = dist;
	return Min;
	
def completelink(set1, set2, data):
	# Create a list of lists for each list in data corresponding to set 1
	lists1 = [data[val] for val in set1];
	# Create a list of lists for each list in data corresponding to set 2
	lists2 = [data[val] for val in set2];
	# Compute the Cartesian product of the vectors in set1 and set2
	cartesian = [element for element in itertools.product(lists1, lists2)];
	
	# Find the maximum distance in the Cartesian product.
	Max = -1;
	for pair in cartesian:
		dist = distance.euclidean(pair[0], pair[1]);
		if(dist > Max):
			Max = dist;
	return Max;

def meanlink(set1, set2, data):
	# Create a list of lists for each list in data corresponding to set 1
	lists1 = [data[val] for val in set1];
	# Create a list of lists for each list in data corresponding to set 2
	lists2 = [data[val] for val in set2];

	# Compute the means of set1 and set2
	s1 = [0 for r in range(len(lists1[0]))];
	s2 = [0 for r in range(len(lists2[0]))];
	for lis in lists1:
		for i in range(len(lis)):
			s1[i] += lis[i]/len(lists1);

	for lis in lists2:
		for i in range(len(lis)):
			s2[i] += lis[i]/len(lists2);

	# Return the norm of the means
	return distance.euclidean(s1,s2);


#---------------------------------------------------------------------------
# Can calculate center and mean cost when using gonzalez and lloyds
#--------------------------------------------------------------------------

# Takes data dictionary
# Takes centers of clusters and phi
# Distance measure
def centerCost(data, centers, phi, distance):
	Max = 0;
	for key,point in data.iteritems():
		dis = distance(centers[phi[key]], point);
		if dis > Max:
			Max = dis;
	return Max;


# Takes data dictionary
# Takes centers of clusters and phi
# Distance measure
def meanCost(data, centers, phi, distance):
	cost = 0.0;
	count = 0;
	for key,point in data.iteritems():
		dis = distance(centers[phi[key]], point);
		cost += distance**2;
		count += 1;

	return sqrt(cost/count);





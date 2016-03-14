import itertools
import distance

'''
data - the data to be clustered, represented as a string=>list dictionary
k - The number of desired clusters
link - the link distance to use for computing 'closest' clusters.

returns - a vector of len(data) which maps each key in data to a cluster value, from 0 to k-1. 
'''
def hierarchical(data, k, link):

	#
	#	This comprehension creates a dictionary where the keys are all the keys from the data file, and all the
	#	values are unique integers from [|data.keys()|]. In other words, assigning each key to a unique integer
	#	which corresponds to assigning each key a different cluster. 
	#
	phi = {v[0]:v[1] for v in zip(data.keys(), [v for v in range(len(data.keys()))])};

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
		number_of_clusters -=1;

	# Compute the final phi values
	cval = 0;
	for cluster in clusters:
		for val in cluster:
			phi[val] = cval;
		cval += 1;

	return phi;


def gonzalez(set1, set2, k):
	phi = {v[0]:v[1] for v in zip(data.keys(), [v for v in range(len(data.keys()))])};


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









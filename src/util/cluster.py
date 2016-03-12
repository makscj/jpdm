

'''
k - The number of desired clusters
data - the data to be clustered
'''
def hierarchical(data, k, link, distance):

	#
	#	This comprehension creates a dictionary where the keys are all the keys from the data file, and all the
	#	values are unique integers from [|data.keys()|]. In other words, assigning each key to a unique integer
	#	which corresponds to assigning each key a different cluster. 
	#
	phi = {v[0]:v[1] for v in zip(data.keys(), [v for v in range(len(data.keys()))])};

	clusters = [[k] for k in data.keys()];

	number_of_clusters = len(data.keys());

	while(number_of_clusters > k):
		for i in range(len(clusters)):
			for j in range(i, len(clusters)):
				x = 3;

	print

	print clusters;
	#while two clusters are close enough

	#find the closest two clusters 

	#merge the clusters into one

def singlelink(set1, set2, data):
	lists1 = [data[val] for val in set1]
	return lists1;
	


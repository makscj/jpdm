import sys
import random
import timeit
import math
from sets import Set


#-------------------------------------------------------
# General Tools
#-------------------------------------------------------
# NOTES:
# Format of a point, [index, x, y]
# format of clusters is array of arrays. Each array is a point belonging to a single cluster.
#-------------------------------------------------------

# Prints (x,y) points for cdf plot.
def plotdcdf(numbers,interval):

	numbers.sort()
	maxN = numbers[len(numbers)-1]+1
	minN = numbers[0] # min

	i = minN
 	while i<maxN:
 		less = 0.0 # Number of items in n which are less than or equal to i
 		for n in numbers:
 			if n<=i:
 				less+=1
 		print "("+str(i)+","+str(less/len(numbers))+")"
 		i+=interval




# Returns the center point to which x is the closest
def phi_C(x, centers):
	dis = float("inf")
	closest = centers[0]
	for c in centers:
		ed = eucDistance(x, c)
		if ed<dis:
			dis = ed
			closest = c
	return closest

def getMedianCost(points, C):
	cost = 0.0
	for x in points:
		cost+= eucDistance(x, phi_C(x, C))
	return cost/len(points)


def get3MeansCost(points, C):
	result = 0.0
	for x in points:
		phi_c = phi_C(x, C)
		result+=pow(eucDistance(x, phi_c), 2)
	result = result/len(points)
	return math.sqrt(result)


# Given a set of points and a set of centers, splits points into clusters.
# If 3 center cost is included, an array is returned with the 3-center cost for each cluster.
def getClustersFromCenters(points, centers, include3CenterCost):

	clusters = []
	maxDistanceOfPointInCluster = [] # Store value for each cluster
	i= len(centers)-1
	while i>-1:
		clusters.append([]) # Initialize clusters array
		maxDistanceOfPointInCluster.append(0.0)
		i=i-1

	for p in points:
		closestDis = float("inf")
		closestClusterIndex = -1		
		for i in range(0, len(centers)):
			# print "TESTING 1", p, centers[i]
			ed = eucDistance(p, centers[i])
			if ed < closestDis:
				closestDis = ed
				closestClusterIndex = i
		clusters[closestClusterIndex].append(p) # Add point to its cluster
		# If distance of p from a center is more than the current maximum distance of a 
		# point (in that cluster) from that center, set this distance to the current
		# maximum distance that a point is from that center.
		if closestDis>maxDistanceOfPointInCluster[closestClusterIndex]:
			maxDistanceOfPointInCluster[closestClusterIndex] = closestDis

	# print "CENTERS:", centers
	# print "CLUSTERS:", clusters

	if  include3CenterCost:
		return [clusters, maxDistanceOfPointInCluster]
	else:
		return clusters


def centersGiveSameSubsets(points,c1, c2):
	if not len(c1)==len(c2): # Need same number of centers
		return False

	# Arrays of arrays
	clus1 = getClustersFromCenters(points, c1, False)
	clus2 = getClustersFromCenters(points, c2, False)

	for cl1 in clus1: # One cluster
		foundMatch = False
		for cl2 in clus2: # One cluster
			if foundMatch:
				break

			# Do cl1 and cl2 match?
			if len(cl1)==len(cl2): # Clusters should be the same length
				set1 = set()
				set2 = set()

				for p in cl1:
					set1.add(p[0]) # Point indices only
				for p in cl2:
					set2.add(p[0])


				setIntersect = set1 ^ set2
				if len(setIntersect)==0:
					foundMatch = True

		if not foundMatch: # If for one of the clusters in clus1 you don't find a match, then this has failed.
			return False

	return True





#!/usr/bin/python

##########################################################################
# Distance measure functions (each takes two vectors, to measure 
# the distance between them).
# -Euclidean
# -Manhattan
# -Jaccard
# -Cosine
# -kl divergence (Note: not a metric)
# -Infinity norm
# -Plus any other kind of n-Norm
##########################################################################

import math

'''
Computes the Euclidean distance (L2 norm) between two vectors.
'''
def euclidean(vector1, vector2):
	return Ln_norm(vector1, vector2, 2);

'''
Computes the Manhattan distance (L1 norm) between two vectors. 
'''
def manhattan(vector1, vector2):
	return Ln_norm(vector1, vector2, 1);


def infNorm(vector1, vector2):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");

	distance = 0.0;
	# Max
	M = 0;
	for i in range(len(vector1)):
		distance = math.fabs(vector1[i] - vector2[i]);
		if distance > M:
			M = distance;

	return M;	

'''
Computes the Ln norm for two vector, V1 and V2, for any given n. 

Note, that for n < 1, the Ln norm is not a metric. 
'''
def Ln_norm(vector1, vector2, n):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");

	distance = 0;

	for i in range(len(vector1)):
		distance += math.fabs(vector1[i] - vector2[i])**n;

	return distance**(1.0/n);	


'''
Computes the Jaccard distance between two vectors.
'''
def jaccard(vector1, vector2):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");
	numerator = 0.0;

	denominator = 0.0;

	for i in range(len(vector1)):
		numerator += min(vector1[i], vector2[i]);
		denominator += max(vector1[i],vector2[i]);

	return 1 - numerator/denominator;

"""
Computes the cosine difference between two vectors. This is the angle between vectors.
"""
def cosine(vector1, vector2):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");
	numerator = 0.0;

	denominator_x = 0.0;
	denominator_y = 0.0;

	for i in range(len(vector1)):
		numerator += vector1[i]*vector2[i];
		denominator_x += vector1[i]**2;
		denominator_y += vector2[i]**2;

	return 1 - numerator/(math.sqrt(denominator_x)*math.sqrt(denominator_y));


'''
Computes the KL Divergence of two vectors. It is reminiscent of entropy.

Note that the KL divergence is NOT a metric. It is not symmetric and it violates the triangle inequality. 

That is, klDiv(V1, V2) != klDiv(V2, V1)
'''
def klDiv(vector1, vector2):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");
	
	div = 0.0;

	for i in range(len(vector1)):
		div += vector1[i]*math.log(vector1[i]/(vector2[i]*1.0));

	return div;

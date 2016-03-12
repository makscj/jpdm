import math

def euclidean(vector1, vector2):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");

	distance = 0;
	for i in range(len(vector1)):
		distance += (vector1[i] - vector2[i])**2;

	return math.sqrt(distance);


def Ln_norm(vector1, vector2, n):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");

	distance = 0;

	for i in range(len(vector1)):
		distance += math.fabs(vector1[i] - vector2[i])**n;

	return distance**(1.0/n);	


def jaccard(vector1, vector2):
	if(len(vector1) != len(vector2)):
		print("Vectors are not the same length");
	numerator = 0.0;

	denominator = 0.0;

	for i in range(len(vector1)):
		numerator += min(vector1[i], vector2[i]);
		denominator += max(vector1[i],vector2[i]);

	return 1 - numerator/denominator;


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

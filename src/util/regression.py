import numpy as np

def svd(matrix):
	
	U,s,V = np.linalg.svd(matrix, full_matrices=True);

	rows = matrix.shape[0];
	cols = matrix.shape[1];

	S = np.zeros((rows, cols));
	S[:cols, :cols] = np.diag(s);

	return (U, S, V);

def pca(matrix):
	rows = matrix.shape[0];

	eye = np.identity(rows);
	one = np.ones((rows,rows));
	C = eye - (1.0/rows)*one;

	nu_matrix = C*matrix;
	return svd(nu_matrix);

def subsvd(U, S, V, k):

	Uk = U[:,0:k];
	Sk = S[0:k,0:k];
	Vk = V[:,0:k];
	return (Uk, Sk, Vk);


'''
Takes in a data set (names => vectors) dictionary.

Returns a tuple (keys, matrix), where the keys is a list of the keys that are associated to each row of the matrix. 
'''
def createMatrix(data):
	keys = [];
	values = [];
	for key,val in data.iteritems():
		keys.append(key);
		values.append(val);
	# temp = values[1];
	# values[1] = values[2];
	# values[2] = temp;
	return (keys, np.matrix(values));

def mapToLowerSpace(matrix, Vk):
	return matrix*Vk;

def mapToPlane(Uk, Sk, Vk):
	return Uk*Sk*np.transpose(Vk);


def getLowerSpace(data, k):
	(keys, matrix) = createMatrix(data);
	(U, S, V) = svd(matrix);
	(Uk, Sk, Vk) = subsvd(U, S, V, k);
	lower = mapToLowerSpace(matrix, Vk);
	return dict(zip(keys, [lower[k,:].tolist()[0] for k in range(lower.shape[0])]));


def getReducedSpace(data, k):
	(keys, matrix) = createMatrix(data);
	(U, S, V) = svd(matrix);
	(Uk, Sk, Vk) = subsvd(U, S, V, k);
	lower = mapToPlane(Uk, Sk, Vk);
	return dict(zip(keys, [lower[k,:].tolist()[0] for k in range(lower.shape[0])]));


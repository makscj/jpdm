#!/usr/bin/python

import distance
import cluster
import regression;
import numpy as np;

'''
x = [1,2,3];
y = [1,3,5];


print distance.euclidean(x,y);

print distance.Ln_norm(x,y,2);

print distance.manhattan(x,y);

print distance.Ln_norm(x,y,1);

print distance.infNorm(x,y);

print distance.Ln_norm(x,y,50);

print distance.jaccard(x,y);

print distance.cosine(x,y);

print distance.klDiv(x,y);

print distance.klDiv(y,x);
'''

# x and y should be in the same cluster. 
# data = {'x':[1,2,3], 'y':[.5,1.5,2.5], 'z' : [4,8,6]};



# (c,p) = cluster.hierarchical(data, 2, cluster.singlelink);

# print c
# print p

# (c,p) = cluster.gonzalez(data, 2, distance.euclidean);

# print "-----"

# print c
# print p
# print cluster.centerCost(data, c, p, distance.euclidean);

# print "-----"

# (c,p) = cluster.lloyds(data, 2, distance.euclidean);

# print c
# print p
# print cluster.centerCost(data, c, p, distance.euclidean);

# a = np.matrix("4 3; 2 2; -1 -3; -5 -2");

#l1 = [4,3]; l2=[2,2]; l3=[-1,-3]; l4=[-5,-2];

data = {'a':[4,3], 'b':[2,2], 'c':[-1,-3], 'd':[-5,-2]};

print data

print "-------"

data1d = regression.getLowerSpace(data, 1);
print data1d;

print "------"

data2d = regression.getReducedSpace(data, 1);
print data2d;

(c,p) = cluster.lloyds(data, 2, distance.euclidean);

print p

(c,p) = cluster.lloyds(data1d, 2, distance.euclidean);

print p

(c,p) = cluster.lloyds(data2d, 2, distance.euclidean);

print p

print "-----------"
print "-----------"

(k,A) = regression.createMatrix(data);

print regression.svd(A);
print "!!!!!!!!!!!!!!!"
print regression.pca(A);



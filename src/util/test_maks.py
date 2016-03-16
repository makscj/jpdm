#!/usr/bin/python

import distance
import cluster


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
data = {'x':[1,2,3], 'y':[.5,1.5,2.5], 'z' : [4,8,6]};

print cluster.hierarchical(data, 2, cluster.singlelink);

print cluster.gonzalez(data, 2, distance.euclidean);

print cluster.lloyds(data, 2, distance.euclidean);


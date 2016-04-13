#!/usr/bin/python


import normalize


print   "Maksnormalize", normalize.normalize({"A": [1,1,1,1], "B": [0,2,0,2]})
print   "normalize", normalize.normalize({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalizeMinMax", normalize.normalizeMinMax({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalizeStandardize", normalize.normalizeStandardize({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalizeDecimal", normalize.normalizeDecimal({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalizeMinMax", normalize.normalizeMinMax({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalizeStandardize", normalize.normalizeStandardize({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalizeDecimal", normalize.normalizeDecimal({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})
print "normalize", normalize.normalize({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,1,1,1,1]})



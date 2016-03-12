#!/usr/bin/python


import normalize

print "normalize", normalize.normalize({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,11,1]})
print "normalizeMinMax", normalize.normalizeMinMax({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,11,1]})
print "normalizeStandardize", normalize.normalizeStandardize({"something": [.001,123.123,54,3,4,100,1,13], "somethingElse": [1,1,1,1,11,1,1000]})
print "normalizeDecimal", normalize.normalizeDecimal({"something": [.0021,.123,.123,.54,.3,.4,.100,.1,13], "somethingElse": [1,1,1,1,11,1,1000]})
print "normalizeMinMax", normalize.normalizeMinMax({"something": [.001,.002,.02,.2], "somethingElse": [1,2,3,4,5,6]})
print "normalizeStandardize", normalize.normalizeStandardize({"something": [.001,.002,.02,.2], "somethingElse": [1,2,3,4,5,6]})
print "normalizeDecimal", normalize.normalizeDecimal({"something": [.001,.002,.02,.2], "somethingElse": [1,2,3,4,5,6]})
print "normalize", normalize.normalize({"something": [.001,.002,.02,.2], "somethingElse": [1,2,3,4,5,6]})



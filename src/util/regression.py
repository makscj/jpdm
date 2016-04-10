import numpy as np



a = np.matrix("4 3; 2 2; -1 -3; -5 -2");

U, s, V = np.linalg.svd(a, full_matrices=True);


Acol = a.shape[1];
Arow = a.shape[0];

k = 1;


S = np.zeros((Arow, Acol));

S[:Acol, :Acol] = np.diag(s);

#print U*S*V

Uk = U[:,0:k];
Sk = S[0:k:,0:k];
Vk = V[:,0:k];

# print Uk
# print Sk
# print Vk

print U*S*V;

print "======================"

print Uk*Sk*np.transpose(Vk)

print "========================"

print Vk

print "==================="

print a*Vk
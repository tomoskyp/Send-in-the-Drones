import math
from math import *

# Drones
# volume / MPL / speed / flight time / range no cargo/ range with cargo
A = [50625.0, 3.5, 40.0, 35.0, 23.333,0]
B = [19800.0, 8.0, 79.0, 40.0, 52.667,0]
C = [90000.0, 14.0, 64.0, 35.0, 37.333,0]
D = [12500.0, 11.0, 60.0, 18.0, 18,0]
E = [13500.0, 15.0, 60.0, 15.0, 15,0]
F = [40000.0, 22.0, 79.0, 24.0, 31.6,0]
G = [17408.0, 20.0, 64.0, 16.0, 17.066,0]
# H = [199875, 0, 0, na, 0]

#this function does not work
#A_range = A[3]*math.e**(-.15*A[1])
#B_range = B[3]*math.e**(-.15*B[1])
#C_range = C[3]*math.e**(-.15*C[1])
#D_range = D[3]*math.e**(-.15*D[1])
#E_range = E[3]*math.e**(-.15*E[1])
#F_range = F[3]*math.e**(-.15*F[1])
#G_range = G[3]*math.e**(-.15*G[1])

# use minus .5 minute per pound of cargo

A[5] = A[2]*((A[3]-A[1]*0.5)/60.0)

B[5] = B[2]*((B[3]-B[1]*0.5)/60.0)
C[5] = C[2]*((C[3]-C[1]*0.5)/60.0)
D[5] = D[2]*((D[3]-D[1]*0.5)/60.0)
E[5] = E[2]*((E[3]-E[1]*0.5)/60.0)
F[5] = F[2]*((F[3]-F[1]*0.5)/60.0)
G[5] = G[2]*((G[3]-G[1]*0.5)/60.0)


#print A_range
#print B_range
#print C_range
#print D_range
#print E_range
#print F_range
#print G_range
print A[5]
print B[5]
print C[5]
print D[5]
print E[5]
print F[5]
print G[5]
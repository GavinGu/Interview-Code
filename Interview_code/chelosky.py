import numpy as np
import pprint

A=np.array([[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]);

print(A)


pprint.pprint(A)


L= np.linalg.cholesky(A);
np.dot(L.T,L)

## decomposed into A
L_m=np.zeros(shape(A));
[row,col]=shape(A);
for i in range(row):
    for k in range(col):
        if i==k:
            sum_=0;
            #for j in range(k):
            #   sum_+=L_m[k,j]*L_m[k,j];
            
            sum_=sum(L_m[k,j]*L_m[k,j] for j in range(k));
            
            L_m[i,k]=np.sqrt(A[i,k]-sum_);
        else:
            sum_=0;
            #for j in range(k):
            #    sum_+=L_m[i,j]*L_m[k,j];
            sum_=sum(L_m[i,j]*L_m[k,j] for j in range(k));
            
            L_m[i,k]=1/L_m[k,k]*(A[i,k]-sum_);
        print (L_m)

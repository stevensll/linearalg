import numpy as np
from numpy import linalg as la
import csv

def mk_mtx(file):
    with open(file) as f:
        reader = csv.reader(f)
        m = list(reader)
    matrix = np.asarray(m, float)
    return matrix 

m1 = mk_mtx("dummy.txt")

def colley_solve(colleyMatrix, colleyVector):
    r = np.matmul(np.linalg.inv(colleyMatrix), colleyVector)
    return np.round(r,2);
def mk_colley(m, v):
    cm = np.copy(m)
    cv  = np.copy(v)
    for i in range(len(m)):
        for j in range(len(m)):
            if i==j:
                cm[i][j]+=2
            else:
                cm[i][j]*=-1
        cv[i]=1+(v[i]-(m[0][0]-v[i]))/2
    return cm,cv

m2 = mk_mtx("b.txt")
print(m2)
print(np.matmul(m2,la.inv(m1)))

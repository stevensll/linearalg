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
eig = la.eig(np.matmul(np.transpose(m1),m1))
print(eig[1])
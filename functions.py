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

avgm = np.asarray


eig = la.eig(np.matmul(m1,np.transpose(m1)))
print(eig[1])
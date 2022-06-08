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

m2 = mk_mtx("b.txt")

print(np.matmul(m2,np.transpose(m1)))

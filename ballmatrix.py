import numpy as np

import csv


with open("CelticsStartingFive.txt") as file:
    reader = csv.reader(file)
    matrix = list(reader)

with open("CelticsPPG.txt") as file:
    reader = csv.reader(file)
    vector = list(reader)

m = np.asarray(matrix,float)
m = np.hstack((m, np.ones((5,1))))

v = np.asarray(vector,float)

m_t = np.transpose(m)

def reg_proj(m, v):
    square = np.matmul(m_t,m)
    invert = np.linalg.inv(square)
    return np.matmul(np.matmul(invert, m_t), v)

# print(reg_proj(m,v))

print(m_t, "\n")
print(v)

print(np.linalg.solve(m,v))

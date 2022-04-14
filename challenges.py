"""
Matrix challenges with python
Challenges covered:
1) Transpose 2D
2) Modulo by n
3) Finding max entry of matrix
4) Trace of a matrix
5) Frobenius inner product


"""
import numpy as np
import csv

with open("CelticsStartingFive.txt") as file:
    reader = csv.reader(file)
    matrix = list(reader)

m = np.asarray(matrix, float) * 1000

def transpose2D(matrix):
    t_shape = np.flip(np.shape(matrix))
    m_t = np.empty(t_shape, float)
    for v in range(t_shape[0]):
        for h in range (t_shape[1]):
            m_t[v][h] = matrix[h][v]
    return (m_t)

def modulo(matrix, divisor):
    return matrix % divisor    

def max(matrix):
    shape = np.shape(matrix)
    max = matrix[0][0]
    entries = [0,0]
    for i in range (shape[0]):
        for j in range (shape[1]):
            if matrix[i][j] > max:
                max = matrix[i][j]
                print(max)
                entries = i,j
    return entries
def trace(matrix):
    shape = np.shape(matrix)
    if(shape[0]!=shape[1]):
        print("Trace does not exist for non square matrix.")
        return 0
    trace = 0
    for i in range (shape[0]):
            trace += matrix[i][i]
    return trace

def frobenius(m1, m2):
    return trace(np.matmul(transpose2D(m1),m2))


print("Matrix m:\n", m , "\n")

print("Transpose of m \n", transpose2D(m), "\n")
d = 3

print("Modulo of m by ", d, "\n", modulo(m,d), "\n")

print("Maximum value of m is located at \n", max(matrix), "which is ", matrix[max(matrix)[0]][max(matrix)[1]], "\n")

print("Trace of matrix m is ", trace(m), "\n")

with open("SquareMatrix.txt") as file:
    reader = csv.reader(file)
    square = list(reader)

s = np.asarray(square, int)
print("Matrix s \n", s)

print("Trace of matrix s is ", trace(s), "\n")

print("Frobenius product of s with itself is\n", frobenius(s,s), "\n")

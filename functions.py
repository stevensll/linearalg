import numpy as np
from numpy import linalg as la
import csv
from operator import itemgetter

def mk_mtx(file):
    with open(file) as f:
        reader = csv.reader(f)
        m = list(reader)
    matrix = np.asarray(m, float)
    return matrix 

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
        cv[i]=1+(v[i]-(m[i][i]-v[i]))/2
    return cm,cv

def massey_solve(masseyMat,masseyV):
    r = np.matmul(np.linalg.inv(masseyMat),masseyV)
    return np.round(r,2);


def mk_standings(team_list,ranking_list):
    dic = {team_list[i]:ranking_list[i] for i in range(len(team_list))}
    return dict(sorted(dic.items(), key=itemgetter(1), reverse=True))  

def mk_standings_csv(dic, file):
    with open(file, 'w') as file:
        w = csv.writer(file)
        w.writerows(dic.items())
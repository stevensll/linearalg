import csv
from collections import OrderedDict
from operator import itemgetter
import numpy as np
import functions

ecf = open("ecf.txt").read().splitlines()
wcf = open("wcf.txt").read().splitlines()
nba = ecf + wcf
nbaDict = OrderedDict({key: 0 for key in nba})
# print(nba)

matchups = np.zeros((len(nba), len(nba)), int)
wins = np.zeros(len(nba), int)

with open("NBA2022edited.csv") as file:
    reader = csv.reader(file)
    for r in reader:
        teamA = r[2]
        teamB = r[4]
        if int(r[3]) > int(r[5]):
            wins[nba.index(teamA)]+=1
        elif int(r[5]) > int(r[3]):
            wins[nba.index(teamB)]+=1

        matchups[nba.index(teamA)][nba.index(teamA)]+=1
        matchups[nba.index(teamB)][nba.index(teamB)]+=1

        matchups[nba.index(teamB)][nba.index(teamA)]+=1
        matchups[nba.index(teamA)][nba.index(teamB)]+=1

i = 0
print(wins)
for v in nbaDict:
    nbaDict[v] = int(wins[i])
    i+=1

print(nbaDict)
# print(matchups)
# print(wins)
# print("\n")
np.savetxt("matchups.csv",matchups.astype(int), fmt='%i',delimiter=",")

colleyMatrix,colleyVector = functions.mk_colley(matchups, wins)

print(colleyVector)

colleyResult=functions.colley_solve(colleyMatrix, colleyVector)

print(colleyResult)

print("\n")
oldRankings = dict(sorted(nbaDict.items(), key=itemgetter(1), reverse=True))
with open('old-standings.csv', 'w') as file:
    w = csv.writer(file)
    w.writerows(oldRankings.items())
    
colleyStandings = {nba[i]:colleyResult[i] for i in range(len(nba))}
newStandings = dict(sorted(colleyStandings.items(),key=itemgetter(1),reverse=True))
with open('new-standings.csv', 'w') as file:
    w = csv.writer(file)
    w.writerows(newStandings.items())

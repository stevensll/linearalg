import csv
from collections import OrderedDict
from operator import itemgetter
import numpy as np
import functions

ecf = open("ecf.txt").read().splitlines()
wcf = open("wcf.txt").read().splitlines()
nba = ecf + wcf
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

# print(matchups)
# print("\n")
np.savetxt("matchups.csv",matchups.astype(int), fmt='%i',delimiter=",")

colleyMatrix,colleyVector = functions.mk_colley(matchups, wins)

print(colleyVector)

colleyResult=functions.colley_solve(colleyMatrix, colleyVector)

print(colleyResult)

print("\n")


def mk_standings(team_list,ranking_list):
    dic = {team_list[i]:ranking_list[i] for i in range(len(team_list))}
    return dict(sorted(dic.items(), key=itemgetter(1), reverse=True))  

def mk_standings_csv(dic, file):
    with open(file, 'w') as file:
        w = csv.writer(file)
        w.writerows(dic.items())

oldRankings = mk_standings(nba,wins)

newStandings = mk_standings(nba, colleyResult) 


mk_standings_csv(oldRankings, 'old-standings.csv')
mk_standings_csv(newStandings, 'new-standings.csv')

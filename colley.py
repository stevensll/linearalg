import csv
from collections import OrderedDict
from operator import itemgetter
import numpy as np
import functions

# DATA PARSING
ecf = open("ecf.txt").read().splitlines()
wcf = open("wcf.txt").read().splitlines()
nba = ecf + wcf

matchups = np.zeros((len(nba), len(nba)), int)
wins = np.zeros(len(nba), int)

with open("NBA2022.csv") as file:
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

#Save the Matchup Matrix
np.savetxt("matchups.csv",matchups.astype(int), fmt='%i',delimiter=",")

#form the colley matrix
colleyMatrix,colleyVector = functions.mk_colley(matchups, wins)

#Solve for the colley ranking vector
colleyResult=functions.colley_solve(colleyMatrix, colleyVector)

#Save old and new standings as CSV
oldRankings = functions.mk_standings(nba,wins)
newStandings = functions.mk_standings(nba, colleyResult) 
functions.mk_standings_csv(oldRankings, 'old-standings.csv')
functions.mk_standings_csv(newStandings, 'new-standings.csv')

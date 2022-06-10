import csv
import numpy as np
import functions

ecf = open("ecf.txt").read().splitlines()
wcf = open("wcf.txt").read().splitlines()
nba = ecf + wcf

#Data Parsing
matchups = np.zeros((len(nba), len(nba)), int)
dfs = np.zeros(len(nba), int)

with open("NBA2022.csv") as file:
    reader = csv.reader(file)
    for r in reader:
        teamA = r[2]
        teamB = r[4]
        dfs[nba.index(teamA)]+=(int(r[3])-int(r[5]))
        dfs[nba.index(teamB)]+=(int(r[5])-int(r[3]))

        matchups[nba.index(teamA)][nba.index(teamA)]+=1
        matchups[nba.index(teamB)][nba.index(teamB)]+=1

        matchups[nba.index(teamB)][nba.index(teamA)]+=1
        matchups[nba.index(teamA)][nba.index(teamB)]+=1


#Form the Massey Matrix and Vector
matchups[len(matchups)-1] = np.ones(len(matchups))
dfs[len(nba)-1] = 0

#Save the Massey Matrix
np.savetxt("matchups.csv",matchups.astype(int), fmt='%i',delimiter=",")

#Solve for the Massey rating vector
masseyResult=functions.massey_solve(matchups,dfs)

#Save new and old standings as CSV
oldRankings = functions.mk_standings(nba,dfs)
newStandings = functions.mk_standings(nba, masseyResult) 
functions.mk_standings_csv(oldRankings, 'old-standings.csv')
functions.mk_standings_csv(newStandings, 'new-standings.csv')

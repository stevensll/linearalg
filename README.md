# Ranking NBA Standings with Colley and Massey Matrices
Linear Algebra Final project with Mr. Honner

## How does it work?

Traditional sports standings usually rank teams simply by their Win-Loss ratio. However, this doesn't always encapsulate the full picture. A team that beats a bad team many times  may have an inflated rank compared to a team who loses to a good team. The [Colley Method](https://www3.nd.edu/~apilking/Math10170/Information/Lectures%202015/Topic8Colley.pdf) aims to account for this disparity in schedule based on the win loss system. 

Additionally, we can also account for how "hard" a team beats another team. If team A always beats their opponents by 15 points, and team B always beats their opponents by 10 points, shouldn't team A rank higher than team B even if they have the same amount of wins? The [Massey Method](https://www3.nd.edu/~apilking/Math10170/Information/Lectures%202015/Topic%209%20Massey%27s%20Method.pdf) aims to account for point differential.

Further readings:
https://www.colleyrankings.com/
https://masseyratings.com/
http://seaver-faculty.pepperdine.edu/dstrong/LinearAlgebra/2014/2014SteveHilbert.pdf
https://www.dcs.bbk.ac.uk/~ale/dsta+dsat/dsta+dsat-3/lm-ch3-colley.pdf


## What does this program do?

This program contains 3 python files that utilize numpy and basic python file reading. 

`functions.py` contains the linear algebra functions to create and solve Colley and Massey systems.

`colley.py` parses input csv data and writes it to two csv files, `new-standings.csv` and `old-standings.csv` using the colley method. 

`massey.py` does the same thing as `colley.py` but using the massey method.

## How you can play around with it

You can check out the different outputs by changing the input file in the `with open("NBA2022.csv") as file` line. All CSV data has been exported from [basketballref](https://www.basketball-reference.com/leagues/NBA_2022_games.html

Alternatively, you can use your own data and call the functions yourself. **The most important thing is to make sure you generate a proper matchup matrix**, which is a n by n matrix where each row, column represents the amount of games team row played against team column. 

To see an example, check out the data [here](https://docs.google.com/spreadsheets/d/1XW7BVppVHFHgkYIFt8ZXMZyTFxi_Zi-haj1cCEbxGEE/edit#gid=1556726268).

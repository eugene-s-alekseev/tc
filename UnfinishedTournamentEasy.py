
"""
Problem Statement
    	A tournament is being played. There are n participants, numbered 0 through n-1. The tournament is a single round-robin tournament. In other words, each player is supposed to play each other player exactly once. There are no ties, each match will be won by one of the two players. 



Some games may have already been played. You are given the information about the current state of the tournament in the String[] G. For each x and y, if x won the game against y, we have G[x][y] = 'W' and G[y][x] = 'L'. For the games that haven't been played yet we have G[x][y] = G[y][x] = '?'. 



The winning rate of a player is the percentage of games they won. In particular, at the end of the tournament the winning rate of a player can be computed as the number of games they won divided by n-1. 



The variance of a sequence is the average square distance of an element of the sequence from the mean of the sequence. Formally, suppose you have a sequence s[0], ..., s[n-1]. Then:
The mean of this sequence is mu(s) = ( s[0] + ... + s[n-1] ) / n.
The variance of this sequence is var(s) = ( (s[0]-mu(s))^2 + ... + (s[n-1]-mu(s))^2 ) / n.


Let r[0], ..., r[n-1] be the sequence of the winning rates of our n players at the end of the tournament. Fill in the results of the remaining matches in a way that maximizes the variance of r. Return the maximal possible value of var(r).
 
Definition
    	
Class:	UnfinishedTournamentEasy
Method:	maximal
Parameters:	String[]
Returns:	double
Method signature:	double maximal(String[] G)
(be sure your method is public)
    
 
Notes
-	Your answer will be considered correct if its absolute or relative error does not exceed 10^(-9).
 
Constraints
-	n will be between 2 and 20, inclusive.
-	G will contain exactly n elements.
-	Each element in G will contain exactly n characters.
-	Each character in G will be one of {'W', 'L', '?', '-'}.
-	For each i, G[i][i] = '-'.
-	For each i != j: {G[i][j], G[j][i]} = {'W', 'L'} or G[i][j] = G[j][i] = '?'.
 
Examples
0)	
    	
{"-??",
 "?-?",
 "??-"}
Returns: 0.16666666666666669
One of the optimal solutions is the following tournament:
-WW
L-W
LL-
For this tournament the winning rates of the three players are {1, 0.5, 0}. Thus, the mean is 0.5 and the variance is ((1-0.5)^2 + (0.5-0.5)^2 + (0-0.5)^2) / 3 = 0.5 / 3 = 0.16667.
1)	
    	
{"-WL",
 "L-W",
 "WL-"}
Returns: 0.0
This time all matches are finished. The winning rates are {0.5, 0.5, 0.5} thus the variance is 0.
2)	
    	
{"-WWL",
 "L-??",
 "L?-?",
 "W??-"}
Returns: 0.1388888888888889
3)	
    	
{"-WWL",
 "L-WW",
 "LL-?",
 "WL?-"}
Returns: 0.08333333333333331
4)	
    	
{"-?",
 "?-"}
Returns: 0.25
5)	
    	
{"-WWL?",
"L-L??",
"LW-?W",
"W??-L",
"??LW-"}
Returns: 0.07500000000000001
"""
import numpy as np

def cast_to_np(track, rows, cols):
    arr = np.full((rows, cols), "?")
    for (player1, player2, result) in track:
        arr[player1, player2] = result
    return arr

def get_win_rate(track):
    return (track == "W").sum() / (track.shape[0]-1)

def get_variance(tournament):
    return np.std(np.apply_along_axis(get_win_rate, 1, tournament))

def maximize_variance(track):
    pass

def main():
    pass


if __name__ == "__main__":
    main()

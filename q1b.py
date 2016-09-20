import numpy as np
import math
n = int(input("Enter no of rounds: "))
m = 2
M = np.random.randint(0,2, size=(m, m))
AS = 0
LA = 0
LB = 0
W = [float(1)] * m
print(M)
for r in range(n):
	print('Round',r)
	row = int(input("Enter Row of Choice: "))
	V = []
	for w in W:
		V.append(float(w)/float(sum(W)))	
	column = np.random.choice(range(m), 1, p=V)
	print('You picked row',row)
	print('AI picked column',column)
	print('Value',M[row][column])
	AS += M[row][column]
	LA += M[row][0]
	LB += M[row][1]
	for i, val in enumerate(W):
		W[i] = W[i] * math.exp(-1 * 0.2 * M[row][i])
	print('Action A Score',LA)
	print('Action B Score',LB)
	print('AI Score',AS)
	print('Adjusted Weight',W)
	print('Regret',AS-min(LA,LB))

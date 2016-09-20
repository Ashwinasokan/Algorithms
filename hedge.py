import numpy as np
import math
n = int(input("Enter no of rounds: "))
m = int(input("Enter payoff matrix size: "))
M = np.random.randint(-100,100, size=(m, m))
HS = 0
AS = 0
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
	HS += M[row][column]
	AS -= M[row][column]
	for i, val in enumerate(W):
		W[i] = W[i] * math.exp(0.2 * M[row][i])
	print('Your Score',HS)
	print('AI Score',AS)
	print('Adjusted Weight',W)

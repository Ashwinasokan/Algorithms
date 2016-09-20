import networkx as nx
import random as rand
import math
import matplotlib.pyplot as plt
minimum_cut_map = dict()
def generate_connected_random_graph(i):
	G =nx.fast_gnp_random_graph(i, 0.5)
	while not nx.is_connected(G):
		G = nx.fast_gnp_random_graph(i, 0.5)
	return G
def printMe(G):
	for (u,v) in G.edges():
		print(u,v)
def main():
	global minimum_cut_map
	for i in range(5,25):
		G = generate_connected_random_graph(i)
		M = minimum_cut(G)
		printMe(G)
		print("Karger's_minimum_cut:")
		print(extract_cut(M))
		M = fast_minimum_cut(G)
		print("Karger_stein_minimum_cut:")
		print(extract_cut(M))
	x = []
	y = []
	for key,val in minimum_cut_map.items():
		x.append(key)
		y.append(val)
	plt.scatter(x, y)
	plt.show()
   
def minimum_cut(G):
	global minimum_cut_map
	max_runs = int(10 * math.pow(G.order(), 2))
	min_cut = random_cut(G,2)
	minimum_cut_map[G.order()] = 1
	for run in range(1,max_runs):
		cut = random_cut(G,2)
		C1 = extract_cut(cut)
        	C2 = extract_cut(min_cut)
		if len(C1)<len(C2):
			minimum_cut_map[G.order()] = 1
			min_cut = cut
		elif len(C1)==len(C2):
			minimum_cut_map[G.order()] = minimum_cut_map[G.order()] + 1
	minimum_cut_map[G.order()] = float(minimum_cut_map[G.order()])/float(max_runs)
	return min_cut

def extract_cut(G):
	cut = []
	for e in G.edges(data = True):  
		cut.append(e[2]['weight'])
 	return cut
   
def random_cut(G,t):
	C = nx.MultiGraph()
	for a,b in G.edges_iter():
		C.add_edge(a,b,weight=(a,b))
	while C.order()>t:
  		(a,b,d)=rand.choice(C.edges(data=True))
		for e in C.edges():  
			if e == (a,b) : C.remove_edge(a,b)
  		for n in C.neighbors(b):
			l = len(C[b][n])
			while l > 0:
    				C.add_edge(a,n,weight=C[b][n][l-1]['weight'])
				l-=1  
   			C.remove_edge(b,n)  
  		C.remove_node(b)
	return C

def fast_minimum_cut(G):
	if(G.order() <= 6):
		return minimum_cut(G)
	t = int(math.ceil(1+(G.order()/math.sqrt(2))))
	G1 = random_cut(G,t)
	G2 = random_cut(G,t)
	return minimum_graph(fast_minimum_cut(G1),fast_minimum_cut(G2))
	
def minimum_graph(G1,G2):
	return G1 if G1.order()<G2.order() else G2

def minimum_cut_graph(G1,G2):
	C1 = extract_cut(G1)
	C2 = extract_cut(G2)
	return G1 if len(C1)<len(C2) else G2
   
if __name__ == '__main__':  
    main()

import random as rand
import matplotlib.pyplot as plt
t_first_pod_gets_first_minion = dict()
t_all_pods_gets_one_minion = dict()
def distribute(k,n):
	pods =  [0] * k
	t = 0
	m = n
	while m > 0:
		t += 1
		r = rand.choice(range(0,k))
		while pods[r] > int((n-m)/k):
			r = rand.choice(range(0,k))
		pods[r] += 1
		m -= 1
		r = rand.choice(range(0,k))
		pods[r] += 1
                m -= 1
		inspect(pods,t,k)
	return pods	

def inspect(pods,t,k):
	global t_first_pod_gets_first_minion
	global t_all_pods_gets_one_minion
	if t_first_pod_gets_first_minion[k] == -1:
		if pods[0] >= 1:
			t_first_pod_gets_first_minion[k] = t
	if t_all_pods_gets_one_minion[k] == -1:
		hasZero = 0
		for i in pods:
			if i == 0:
				hasZero = 1
		if hasZero == 0:
			t_all_pods_gets_one_minion[k] = t
	print("No of minions in first Pod",pods[0],t)
	print("Time when first pod gets a minion",t_first_pod_gets_first_minion[k])
	print("Time when all pods get atleast a minion",t_all_pods_gets_one_minion[k])
		
def main():
	global t_first_pod_gets_first_minion
        global t_all_pods_gets_one_minion
	for k in range(10,100,10):
		t_first_pod_gets_first_minion[k] = -1
		t_all_pods_gets_one_minion[k] = -1
		print (distribute(k,10*k))
	x = []
        y = []
	z = []
        for key,val in t_all_pods_gets_one_minion.items():
                x.append(key)
                y.append(val)
		z.append(t_first_pod_gets_first_minion[key])
	print(x)
	print(y)
	print(z)
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	ax1.scatter(x, y, s=10, c='b', marker="s", label='All pods gets atleast one minion')
	ax1.scatter(x, z, s=10, c='r', marker="o", label='First pod gets first minion')
	plt.legend(loc='upper left')
	plt.show()

if __name__ == '__main__':  
    main()

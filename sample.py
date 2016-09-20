import numpy as np
for i in range(5):
	sample = np.random.uniform(0,1,i)
	print(sample)
for i in range(5):
        sample = np.random.dirichlet(np.ones(i),size=1)
        print(sample)

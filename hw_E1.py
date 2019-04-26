import numpy as np 
import seaborn
import matplotlib.pyplot as plt 
lam_for_poisson = float(input("Lam for poisson: "))
size_for_distribution = int(input("Size_for_distribution: "))
poisson_distribution = np.random.poisson(lam = lam_for_poisson, size = size_for_distribution) 
seaborn.distplot (poisson_distribution,label = "poisson" ) 
plt.legend () 
plt.show ()

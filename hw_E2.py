import numpy as np 
import seaborn
import matplotlib.pyplot as plt 
lam_for_pareto = float(input("Lam for pareto: "))
size_for_distribution = int(input("Size for distribution: "))
pareto_distribution = np.random.poisson(lam = lam_for_pareto, size = size_for_distribution) 
seaborn.distplot (pareto_distribution,label = "pareto" ) 
plt.legend () 
plt.show ()

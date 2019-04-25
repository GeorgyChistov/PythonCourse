import numpy as np 
import seaborn as sea
import matplotlib.pyplot as plt 

poisson = np.random.poisson(lam=0.5, size=1000) 
sea.distplot (poisson,label = "poisson" ) 
plt.legend () 
plt.show ()

import seaborn as sea 
import numpy as np 
import matplotlib.pyplot as mathplt 

pareto = np.random.pareto(100, 1000) 

sea.distplot (pareto,label = "pareto") 
mathplt.legend () 
mathplt.show ()

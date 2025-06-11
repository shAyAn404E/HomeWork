import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import append
import scipy.stats as stats


X = np.array([2,3,4,6,2,3,1,3,2,4,1])
mean = np.full_like(X, X.mean())
difference = []


plt.scatter(np.arange(len(X)), X,label="Data")
plt.plot(mean,"g--", label="Mean")

for i in range(len(X)):
    plt.plot([i,i],[mean[i],X[i]],linestyle="dashed", color="pink")
    difference.append(X[i]-mean[i])

mod = (stats.mode(X))
med = (np.median(X))
mea = (np.mean(X))
su = np.sum(X)
pr = X.prod()


with open('difference.txt','w') as f:
    f.write(f'the difference for each data to mean is : {difference} \n ')
    f.write(f'\n the most coming data and number its comes is : {mod} \n' )
    f.write(f'\n the center of the data is : {med} \n ')
    f.write(f'\n the mean of the data is : {mea:.4f} \n ')
    f.write(f'\n tne sum of the data is {su} \n')
    f.write(f'\n the prod of the data is : {pr} \n ')




plt.legend()
plt.show()
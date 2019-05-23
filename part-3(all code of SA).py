# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:39:46 2019

@author: Murat Batuhan Günaydın
"""

import random, numpy as np, math
import matplotlib.pyplot as plt
import copy as cp

call = np.genfromtxt('Coordinates.csv', dtype='str',delimiter=',', encoding='utf-8').T
names=call[0]
x = call[1].astype(float)
y = call[2].astype(float)

def get_path_length(apath):
    # this function returns the total distance of a path
    call = np.genfromtxt('distancematrix.csv', dtype='str',delimiter=',', encoding='utf-8')
    call[call==''] = 0
    def distance(i,j):
        return float(call[i+1, j+1])
    
    total = 0
    for i,j in zip(apath[:-1],apath[1:]):
        d=distance(i,j)
        total = total + d
    return total

city = np.vstack((x, y)).T
cn=len(city)

xmin = min(pair[0] for pair in city)
aa= [pair[0] for pair in city]
xmax = max(pair[0] for pair in city)
ymin = min(pair[1] for pair in city)
ymax = max(pair[1] for pair in city)

def transform(pair):
    x = pair[0]
    y = pair[1]
    return [(x-xmin)*100/(xmax - xmin), (y-ymin)*100/(ymax - ymin)]


fc=np.where(names=='Ankara')

city = [ transform(b) for b in city]
path = random.sample(range(cn),cn);
path=np.delete(path,fc)
path=np.insert(np.asarray(path),0,fc)
path=path.tolist()

for temperature in np.logspace(0,5,num=100000)[::-1]:
    [i,j] = sorted(random.sample(range(cn),2));
        
    newpath =  path[:i] + path[j:j+1] +  path[i+1:j] + path[i:i+1] + path[j+1:];
 
    if math.exp( ( sum([ math.sqrt(sum([(city[path[(k+1) % cn]][d] - city[path[k % cn]]
    [d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([math.sqrt(sum([(city[newpath[(k+1) % cn]][d]
    - city[newpath[k % cn]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
        path = cp.copy(newpath);
    plt.plot(temperature)

path=np.delete(path,fc)
path=np.insert(np.asarray(path),0,fc)
path=path.tolist()
distance=get_path_length(path)

plt.plot([city[path[i % cn]][0] for i in range(cn+1)], [city[path[i % cn]][1] for i in range(cn+1)], 'o-');
plt.show()
print('best path is= ',distance)


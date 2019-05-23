# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:32:31 2019

@author: S2B
"""

import numpy as np
import matplotlib.pyplot as plt

def get_coordinates():
    
    call = np.genfromtxt('Coordinates.csv', dtype='str',delimiter=',', encoding='utf-8').T    
    cities = call[0]
    x = call[1].astype(float)
    y = call[2].astype(float)
    points=np.vstack((x,y))
    return points, x, y,cities

def get_path():
   
  f_c = np.where(cities=='Ankara') # first city
  n = points.shape[1]  
  l = list(range(n))
  l=np.delete(l,f_c)
  np.random.shuffle(l)
  l=np.insert(l,0,f_c)  

  return l


def get_path_length(path):
    
    path=np.append(path,path[0])
        
    call = np.genfromtxt('distancematrix.csv', dtype='str',delimiter=',', encoding='utf-8')  
    def distance(i,j):
        return float(call[i+1, j+1])    
    
    total_length = 0
    for i,j in zip(path[:-1],path[1:]):
        d=distance(i,j)
        total_length = total_length + d
    return total_length

def draw_path(path):
  path = np.append(path,path[0])
  plt.plot(y[path],x[path],'-o')

def cross_over(gene1,gene2, mutation=0.5):
   
  r = np.random.randint(len(gene1)) # cross over location
  newgene = np.append(gene1[:r],gene2[r:]) # may be a defunct gene    
  missing = set(gene1)-set(newgene)
  elements, count = np.unique(newgene, return_counts=True)
  duplicates = elements[count==2]
  duplicate_indices=(newgene[:, None] == duplicates).argmax(axis=0)
  newgene[duplicate_indices]=list(missing) # now proper.

  if np.random.rand()<mutation:
    i1,i2 = np.random.randint(0,len(newgene),2)
    newgene[[i1,i2]] = newgene[[i2,i1]] 

  return newgene

def create_initial_population(m):
  population = []
  fitness = []
  for i in range(m):
    gene = get_path()
    path_length = get_path_length(gene)   
    population.append(gene)
    fitness.append(path_length)
  
  population = np.array(population)
  fitness = np.array(fitness)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]

def next_generation(population):
  pop = []
  fit = []
  i=0
  f=int(np.sqrt(len(population)))
  for gene1 in population[:f]:
    for gene2 in population[:f]:
      i=i+1      
      x =  cross_over(gene1,gene2)
      l = get_path_length(x)
      pop.append(x)
      fit.append(l)
  
  population = np.array(pop)
  fitness = np.array(fit)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]



n_population=300
points,x,y,cities=get_coordinates()
population, fitness  = create_initial_population(n_population)

for i in range(10000):
  population, fitness=next_generation(population)
  #print(fitness.min(),fitness.mean())
  print('iteration', i+1, 'distance is: ', fitness.min())
  best_path = population[0]
  draw_path(best_path)
  plt.show()
  plt.plot(fitness)
  plt.show()
  


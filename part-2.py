# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:27:08 2019

@author: S2B
"""

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
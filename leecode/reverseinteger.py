# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:55:58 2020

@author: user
"""



#%% easier version 
def reverse1(x):
    y = list(str(abs(x)))
    y.reverse()
    z= ''.join(x for x in y)
    if x > 0 and int(z) <= (2**31-1):
        return (int(z))
    if x == 0: 
        return 0
    if x < 0 and int(z) <= (2**31-1):
        return (- int(z))
    else: 
        return 0
#%%
reverse1(-123)











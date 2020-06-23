# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:29:43 2020

@author: user
"""


#%%
def twoSum(nums, target):
        a ={}
        for i, num in enumerate(nums):
            if target-num in a:
                return [a[target - num], i]
            else:
                a[num] = i

#%%
b = [2, 7, 11, 15]
t = 9
print(twoSum(b,t))
#%%                
## a = {2:0} 
## a[2] = 0 
#%%









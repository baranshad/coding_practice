# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:00:16 2020

@author: user
"""

import numpy as np
#%%
def ifexistSubstringcontainallunique(s):
    list_st = list(s)
    uniq_s=np.unique(list_st) 
    anyin=[]
    for i in range(0, len(list_st)-len(uniq_s)+1):
        if set(list_st[i:i+len(uniq_s)]) == set(uniq_s):
            anyin.append(1)
        else: 
            anyin.append(0)
    if sum(anyin)>0: 
       return(len(uniq_s))
    else: 
#%%
# Python program to find the length of the longest substring 
# without repeating characters 
NO_OF_CHARS = 256
  
def longestUniqueSubsttr(string): 
  
    # Initialize the last index array as -1, -1 is used to store 
    # last index of every character 
    lastIndex = [-1] * NO_OF_CHARS 
  
    n = len(string) 
    res = 0   # Result 
    i = 0
  
    for j in range(0, n): 
        # Find the last index of str[j] 
        # Update i (starting index of current window) 
        # as maximum of current value of i and last 
        # index plus 1 
        i = max(i, lastIndex[ord(string[j])] + 1); 
  
        # Update result if we get a larger window 
        res =  max(res, j - i + 1) 
  
        # Update last index of j. 
        lastIndex[ord(string[j])] = j; 
  
    return res 
#%%
string1 = "abcbbcbc"
lengthOfLongestSubstring(string1)
#%%












 

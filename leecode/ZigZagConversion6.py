# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### ZigZag Conversion 6 
## The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
## number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

##P   A   H   N
##A P L S I I G
##Y   I   R
##And then read line by line: "PAHNAPLSIIGYIR"

##Write the code that will take a string and make this conversion given a number of rows:

##string convert(string s, int numRows);
##Example 1:

##Input: s = "PAYPALISHIRING", numRows = 3
##Output: "PAHNAPLSIIGYIR"
##Example 2:

##Input: s = "PAYPALISHIRING", numRows = 4
##Output: "PINALSIGYAHRPI"
##Explanation:

##P     I    N
##A   L S  I G
##Y A   H R
##P     I
#%%
def convert(s, numRows):
    if numRows == 1: 
        return s 
    n = len(s) 
    cycle= numRows*2 - 2 
    strlist = []
    for i in range(numRows):
        for j in range(i, n, cycle):
            strlist.append(s[j])
            if i != 0 and i != numRows - 1 and j+cycle-2*i < n : 
                strlist.append(s[j+cycle-2*i])
    newstring = ''.join(strlist)
    return newstring 
#%% 
    
    
    
    
    
    
    
    
    
    
    
    


















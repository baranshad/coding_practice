# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:51:35 2020

@author: baran
"""


## String to Integer (atoi)
## Implement atoi which converts a string to an integer.

##The function first discards as many whitespace characters as necessary until the first 
## non-whitespace character is found. Then, starting from this character, takes an optional 
##initial plus or minus sign followed by as many numerical digits as possible, and interprets 
## them as a numerical value.

##The string can contain additional characters after those that form the integral number,
##  which are ignored and have no effect on the behavior of this function.

##If the first sequence of non-whitespace characters in str is not a valid integral number,
## or if no such sequence exists because either str is empty or it contains only whitespace characters,
## no conversion is performed.

##If no valid conversion could be performed, a zero value is returned.

##Note:

##Only the space character ' ' is considered as whitespace character.
##Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
##Example 1:

##Input: "42"
##Output: 42
##Example 2:

##Input: "   -42"
##Output: -42
##Explanation: The first non-whitespace character is '-', which is the minus sign.
##             Then take as many numerical digits as possible, which gets 42.
##Example 3:

##Input: "4193 with words"
##Output: 4193
##Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
##Example 4:

##Input: "words and 987"
##Output: 0
##Explanation: The first non-whitespace character is 'w', which is not a numerical 
##             digit or a +/- sign. Therefore no valid conversion could be performed.
##Example 5:

##Input: "-91283472332"
##Output: -2147483648
##Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
##             Thefore INT_MIN (−231) is returned.
#%%  
def myAtoi(s: str):
    newstr=[]
    for i in range(len(s)):
        if s[i] != ' ':
            newstr.append(s[i])
        newstring = ''.join(newstr)   
    finalinterger=[]
    for j in range(len(newstring)):
        if not newstring[j].isdigit(): 
            break
        else:  
            finalinterger.append(newstring[j])
    newinter = ''.join(finalinterger)
    if int(str(newinter)) >= 2**31-1: 
            return 2**31-1 
    if int(str(newinter)) <= -2**31: 
            return -2**31
    else:
            return newinter
#%%
s= "4223.321 the umber is not"
len(s)
print(len(s))
print(s[12])

#%%
myAtoi(s)
print(myAtoi(s))

#%% other Solution:
def myAtoi2(S: str):
        v_first=True
        l_check=[str(i) for i in range(10)]
        l_out=""
        S=S.lstrip()
        for i,s in enumerate(S):
            if v_first:
                if s in l_check or s=="-" or s=="+":
                    l_out+=s
                    v_first=False
                else:
                    return 0
            else:
                if s in l_check:
                    l_out+=s
                else:
                    break
        if len(l_out)==0:
            return 0
        elif len(l_out)==1:
            if l_out=="-" or l_out=="+":
                return 0
        else:
            if int(l_out)<0 and -1*int(l_out)>=2**31:
                l_out=-1*2**31
            elif int(l_out)>=0 and int(l_out)>=2**31-1:
                l_out=2**31-1
            else:
                l_out=int(l_out)        
        return l_out
#%%
myAtoi2(s)
print(myAtoi2(s))

#%%
#%%
newstr=[]
for i in range(len(s)):
    print(s[i])
    if s[i] != ' ':
        newstr.append(s[i])
    newstring = ''.join(newstr)
#%%
finalinterger=[]
for j in range(len(newstring)):
    if not newstring[0].isdigit(): 
        return 0 
    if newstring[j] == '-' or  newstring[j].isdigit(): 
        finalinterger.append(newstring[j])
    newinter = ''.join(finalinterger)
    return(newinter)
















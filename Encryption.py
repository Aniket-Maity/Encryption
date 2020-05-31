# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:25:22 2020

@author: Aniket Maity
"""
import math
import os
import random
import re
import sys

def encryption(s):
    s = s.replace(" ","")
#    len1 = math.floor(math.sqrt(len(s)))
    len2 = math.ceil(math.sqrt(len(s)))
    
    result = []
    for idx in range(0,len(s),len2):
    #    print(idx)
        v = s[idx:idx+len2]
    #    print(v)
        for cidx in range(len2):
            if len(v) > cidx:
                ele = v[cidx]
            else:
                ele = ""
                
            if idx > 0:
                result[cidx] += ele
            else:
                result.append(ele)
    return " ".join(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()


        
            
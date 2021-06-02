# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:56:15 2021

@author: dimit
"""

def solution(M, F):
    M = int(M)
    F = int(F)
    n_gen = 0
    while True:
        n_gen += max(M,F) // min(M,F)
        remainder = max(M,F) % min(M,F)
        F = min(M,F)
        M = remainder
        print(M, F)
        if F == 1:
            return str(n_gen-1)
        elif M == 0:
            return "impossible"
        
        
print(('1', '2'))
print(solution('1', '2'))

print(('4', '7'))
print(solution('4', '7'))

print(('4', '2'))
print(solution('4', '2'))
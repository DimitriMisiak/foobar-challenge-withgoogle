# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:21:44 2021

@author: dimit
"""
def int_to_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return ''.join(digits[::-1])

def solution(n, b):
    k = len(n)
    
    visited_values = [n, ]
    while True:
        n = visited_values[-1]
        n_inf = ''.join(sorted(n))
        n_sup = ''.join(sorted(n, reverse=True))
    
        print(f"{n} --> {n_inf}, {n_sup}")
    
        diff_n_base10 = int(n_sup, b) - int(n_inf, b)
    
        diff_n = int_to_base(diff_n_base10, b)
        print(f"{diff_n}")
        diff_n = '0'*(k-len(diff_n)) + diff_n
    
        
        print(f"{n} --> {n_inf}, {n_sup} --> {diff_n}")
    
        try:
            prev_idx = visited_values.index(diff_n)
        except:
            visited_values.append(diff_n)
            continue
    
        reached_constant = (prev_idx == len(visited_values)-1)
        # analyzing
        if reached_constant:
            return 1
        else:
            return len(visited_values[prev_idx:])

### TEST

input_0 = ('0000', 10)
print(solution(*input_0))
input_1 = ('210022', 3)
print(solution(*input_1))
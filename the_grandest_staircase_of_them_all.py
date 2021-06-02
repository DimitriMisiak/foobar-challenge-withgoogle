# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:03:53 2021

@author: dimit
"""

global_stairs_dict = {
    0:{0:1},
}

def gen_stairs(n):
    
    # last_step_max_height = n-1
    # last_step_min_height = int( (-1 + (1 + 8*n)**0.5)/ 2 )
    
    # print(last_step_max_height, last_step_min_height)
    
    stairs_per_height = {0:0}
    num = 0
    # for h in range(int(n**0.5), n+1):
    for h in range(1, n+1):
        try:
            stairs_dict = global_stairs_dict[n-h]
        except:
            stairs_dict = global_stairs_dict[n-h] = gen_stairs(n-h)
        
        limit_height = max([k for k in stairs_dict.keys() if k<h])
        num += stairs_dict[limit_height]

        stairs_per_height[h] = num
    
    
    global_stairs_dict[n] = stairs_per_height
    return stairs_per_height

def solution(n):
    gen_stairs(n)
    return global_stairs_dict[n][n]-1

print(3, solution(3))

print(200, solution(200))
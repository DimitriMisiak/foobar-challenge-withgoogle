# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:02:27 2021

@author: dimit
"""
# import numpy as np

# def solution(start, length):

#     checksum_arr = 0
#     for i in range((length+1)//2):
#         j = length-i-1
#         start_0 = start + length * i
#         start_1 = start + length * j
#         line_0 = start_0 + np.arange(length-i)
#         line_1 = start_1 + np.arange(length-j)

#         line = np.hstack((line_0, line_1))
#         print(line)
#         checksum_arr = np.bitwise_xor(checksum_arr, line)
    
#     checksum = np.bitwise_xor.reduce(checksum_arr)
#     return checksum

import numpy as np

def solution(start, length):

    checksum = 0
    for i in range(length):
        line = start + length * i + np.arange(length-i)
        checksum ^= np.bitwise_xor.reduce(line)

    return checksum




print(solution(0, 3))

print(solution(17, 4))

print(solution(17, 44000))
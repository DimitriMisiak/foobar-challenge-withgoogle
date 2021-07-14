# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:31:38 2021

@author: dimit
"""
import numpy as np

def solution(entrances, exits, paths):

    #%%
    size_arr = np.array(paths, dtype=int)
    flux_arr = np.zeros(shape=size_arr.shape, dtype=int)
    
    coords_list = [tuple(x) for x in np.transpose(np.nonzero(paths))]

    entrance_corridors = [
        coords for coords in coords_list if coords[0] in entrances
    ]

    exit_corridors = [
        coords for coords in coords_list if coords[1] in exits
    ]
    
    path_queue = [(coords,) for coords in entrance_corridors]
    
    coords_arr = np.transpose(np.nonzero(paths))
    
    path_list = []
    
    graph = {}
    
    while path_queue:
        print(path_queue)
        path = path_queue.pop(0)
        last_corr = path[-1]
        # adjacent_coords = [
        #     coords for coords in coords_list if coords[0]==last_corr[1]
        # ]
        
        try:
            adjacent_coords = graph[last_corr]
        except:
            graph[last_corr] = coords_arr[coords_arr[:,0]==last_corr[1]]
            adjacent_coords = graph[last_corr]
        
        for coords in adjacent_coords:
            coords = tuple(coords)
            if not (coords in  path):
                new_path = path + (coords,)
                if coords in exit_corridors:
                    path_list.append(new_path)
                else:
                    path_queue.append(new_path)
        
    # for path in path_list:
    #     # print(path)
    #     remainder_on_path = [size_arr[coords] - flux_arr[coords] for coords in path]
    #     flux_for_path = min(remainder_on_path)
    #     # print(flux_for_path)
    #     for coords in path:
    #         flux_arr[coords] += flux_for_path
            
    # total_bunnies = np.sum(flux_arr[:, exits])
    
    # return total_bunnies
    
    # return 'lol'


#%%
if __name__ == "__main__":

    x0 = solution(
        [0], [3],
        [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    )
    print(x0)
    x1 = solution(
        [0, 1], [4, 5],
        [[0, 0, 4, 6, 0, 0],
         [0, 0, 5, 2, 0, 0],
         [0, 0, 0, 0, 4, 4],
         [0, 0, 0, 0, 6, 6],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]
    )
    print(x1)
    # paths = np.triu(np.random.randint(2e6, size=(13, 13)))
    paths = np.random.randint(2e6, size=(6, 6))
    x2 = solution(
        [0, 1], [4, 5],
        paths
    )
    print(x2)
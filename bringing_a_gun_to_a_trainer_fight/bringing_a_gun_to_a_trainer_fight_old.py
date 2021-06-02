# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:26:40 2021

@author: dimit
"""
import numpy as np

# class Node():
    
#     def __init__(self, vector, is_mine):
#         self.vector = vector
#         self.is_mine = is_mine

# def generate_reflection(origin_coords, wall_position, wall_is_horizontal):
    
#     # if wall is horizontal, the reflection is done on the y-axis
#     # which needs te retrieve the index 1 of the coords
#     if wall_is_horizontal:
#         dir_idx = 1
#     else:
#         dir_idx = 0
        
#     vector_to_wall = np.zeros(2)
#     vector_to_wall[dir_idx] = (
#         wall_position - origin_coords[:, dir_idx]
#     )
#     vector_to_reflection = 2 * vector_to_wall
    
#     reflection_coords = origin_coords + vector_to_reflection
    
#     return reflection_coords

def generate_reflection(origin_coords, wall_positions):
    
    top, bottom, left, right = wall_positions
    dir_idx_list = [1, 1, 0, 0]
    
    vector_to_wall = np.zeros(shape=(4, 2))
    
    vect_list = []
    for i in range(4):
        dir_idx = dir_idx_list[i]
        
        vector_to_wall = wall_positions[i] - origin_coords[:, dir_idx]
        
        dir_vects = np.array(origin_coords)
        dir_vects[:, dir_idx] += 2 * vector_to_wall
        
        vect_list.append(dir_vects)
    
    return np.vstack(vect_list)


# def solution(dimensions, your_position, trainer_position, distance):
    
#     left_wall_x = 0
#     bottom_wall_y = 0
#     right_wall_x, top_wall_y = dimensions
    
#     beam_distance = distance
    
#     # nodes dict with keys as number of reflections from the beam to connect
#     # and values as "virtual" coordinates by creating reflections of nodes
#     # with the top, bottom, left, right wall-mirrors
#     my_nodes = {
#         0: (your_position,)
#     }
#     opp_nodes = {
#         0: (trainer_position,)
#     }

room_dimensions = [3,2]
left_wall_x = 0
bottom_wall_y = 0
right_wall_x, top_wall_y = room_dimensions

beam_distance = 4

# nodes dict with keys as number of reflections from the beam to connect
# and values as "virtual" coordinates by creating reflections of nodes
# with the top, bottom, left, right wall-mirrors
my_position = [1, 1,]
opp_position = [2,1]
wall_dimensions = (top_wall_y, bottom_wall_y, left_wall_x, right_wall_x)


my_nodes = {my_position,}
my_queue = [my_position,]
reflected_nodes = {}

# generate reflections while one of the origin is still in the gun range
for node in my_queue:
    
    coords_arr = my_nodes[n_refl]
    if np.all(np.linalg.norm(coords_arr - my_position, axis=1) > beam_distance):
        break
    
    my_nodes[n_refl+1] = generate_reflection(coords_arr, wall_dimensions)
    n_refl += 1

# opp_nodes = {opp_position}

# n_refl = 0
# while True:
    
#     coords_arr = opp_nodes[n_refl]
#     if np.all(np.linalg.norm(coords_arr - my_position, axis=1) > beam_distance):
#         break
    
#     opp_nodes[n_refl+1] = generate_reflection(coords_arr, wall_dimensions)
#     n_refl += 1
    
# =============================================================================
# PLOT TO VERIFY
# =============================================================================
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle, Circle
# plt.close('all')

# fig, ax = plt.subplots()
# ax.grid(alpha=0.3)

# for k,arr in my_nodes.items():
#     ax.scatter(
#         *arr.T,
#         color='b', marker='o'
#     )

# for k, arr in opp_nodes.items():
#     ax.scatter(
#         *arr.T,
#         color='r', marker='s',
#     )

# rect = Rectangle(
#     (0, 0), right_wall_x, top_wall_y,
#     linewidth=2, edgecolor='k', facecolor="none"
# ) 
# ax.add_patch(rect)

# circ = Circle(
#     my_position, radius=beam_distance,
#     facecolor="orange", alpha=0.3
# )
# ax.add_patch(circ)

# fig.tight_layout()

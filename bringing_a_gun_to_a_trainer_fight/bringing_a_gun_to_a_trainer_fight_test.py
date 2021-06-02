# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:26:40 2021

@author: dimit
"""
import numpy as np
import math as m

def solution(dimensions, your_position, trainer_position, distance):
    return NotImplemented
    #return number_of_angles


#%%
# =============================================================================
# MAIN
# =============================================================================
dimensions = [3,2]
my_position = [1, 1]
opp_position = [2,1]
beam_range = 4000

# dimensions = [300,275]
# my_position = [150,150]
# opp_position = [185,100]
# beam_range = 10000

my_position = np.array(my_position)
opp_position = np.array(opp_position)

# your_nodes_set = generate_node_set(your_position, your_position)
# trainer_nodes_set = generate_node_set(trainer_position, your_position)

my_pattern = {
    "TR": my_position,  # top right quadrant
    "BR": my_position * [-1, 1], # bottom right quadrant
    "TL": my_position * [1, -1], # top left quadrant
    "BL": my_position * [-1, -1], # bottom left quadrant
}

opp_pattern = {
    "TR": opp_position,  # top right quadrant
    "BR": opp_position * [-1, 1], # bottom right quadrant
    "TL": opp_position * [1, -1], # top left quadrant
    "BL": opp_position * [-1, -1], # bottom left quadrant
}


h_dist = 2 * dimensions[0]
v_dist = 2 * dimensions[1]

h_repetition = m.ceil(beam_range/h_dist)
v_repetition = m.ceil(beam_range/v_dist)

h_range = np.arange(-h_repetition, h_repetition+1) * h_dist
v_range = np.arange(-v_repetition, v_repetition+1) * v_dist

grid = np.meshgrid(h_range, v_range)
grid = np.array([grid[0].ravel(), grid[1].ravel()]).T

my_nodes_dict = {}
for k,pos in my_pattern.items():
    pos_arr = pos + grid
    my_nodes_dict[k] = pos_arr
my_nodes = np.vstack(list(my_nodes_dict.values()))

opp_nodes_dict = {}
for k,pos in opp_pattern.items():
    pos_arr = pos + grid
    opp_nodes_dict[k] = pos_arr
opp_nodes = np.vstack(list(opp_nodes_dict.values()))

### working in space centered
my_nodes -= my_position
opp_nodes -= my_position

## removing my position
my_nodes = my_nodes[np.any(my_nodes!=0, axis=1)]

all_nodes = np.vstack([my_nodes, opp_nodes])

def distance(arr):
    return np.linalg.norm(arr, axis=1)

my_angles = np.angle(
    my_nodes[:,0] + 1j * my_nodes[:,1],
    deg=True
)
my_distances = distance(my_nodes)

my_info = np.vstack(
    [my_angles, my_distances, np.zeros(my_angles.shape)]
).T

opp_angles = np.angle(
    opp_nodes[:,0] + 1j * opp_nodes[:,1],
    deg=True
)
opp_distances = distance(opp_nodes)

opp_info = np.vstack(
    [opp_angles, opp_distances, np.ones(opp_angles.shape)]
).T

all_info = np.vstack(
    [my_info, opp_info]
)

dtype = [('angle', float), ('distance', float)]
arr_to_be_sorted = np.array(
    [(ang, dist) for ang,dist in all_info[:,:-1]],
    dtype=dtype
)

sorting_indexes = np.argsort(arr_to_be_sorted, order=['angle', 'distance'])


all_info_sorted = all_info[sorting_indexes]

_, unique_indexes = np.unique(all_info_sorted[:,0], return_index=True)
all_info_unique = all_info_sorted[unique_indexes]

inrange_indexes = (all_info_unique[:,1] <= beam_range)

all_info_inrange = all_info_unique[inrange_indexes]

all_nodes_inrange = all_nodes[sorting_indexes][unique_indexes][inrange_indexes]

result = int(np.sum(all_info_inrange[:,-1]))

print(result)


#%%
# =============================================================================
# PLOT
# =============================================================================
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle, Circle
# plt.close('all')

# fig, ax = plt.subplots()
# ax.grid(alpha=0.3)

# ax.scatter(
#     *my_nodes.T,
#     color='b', marker='o'
# )

# ax.scatter(
#     *opp_nodes.T,
#     color='r', marker='s'
# )

# ax.scatter(
#     *all_nodes_inrange.T,
#     color='w', marker='.'
# )

# # for node in your_nodes_set:
# #     ax.scatter(
# #         h_range + 1,
# #         color='b', marker='o'
# #     )

# # for node in trainer_nodes_set:
# #     ax.scatter(
# #         *node,
# #         color='r', marker='s'
# #     )

# rect = Rectangle(
#     (0, 0)-my_position, *dimensions,
#     linewidth=2, edgecolor='k', facecolor="none"
# ) 
# ax.add_patch(rect)

# circ = Circle(
#     (0,0), radius=beam_range,
#     facecolor="orange", alpha=0.3, edgecolor='k'
# )
# ax.add_patch(circ)

# fig.tight_layout()


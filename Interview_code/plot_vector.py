#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:35:22 2018

@author: guweixi
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


x, y, z = np.meshgrid(np.arange(-2, 2, 0.5),
                      np.arange(-2, 2, 0.5),
                      np.arange(-2, 2, 0.5))

X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#myPoint=(1,1,1,1,2,3);
#ax.quiver(1,1,1,1,2,3)
previous_vector=[1,1,1];
transfer_matrix=[[4,12,-16],[12,37,-43],[-16,-43,98]];
after_vector=np.dot(previous_vector,transfer_matrix);


ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])
#ax.quiver(0,3,0,previous_vector[0],previous_vector[1],previous_vector[2])
#plt.show()
ax.quiver(0,3,0,after_vector[0],after_vector[1],after_vector[2])
plt.show()



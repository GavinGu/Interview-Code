#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:58:42 2018

@author: guweixi
"""
import numpy as np
import matplotlib.pyplot as plt

x=array(range(1,100));
y=0.3*np.exp(-0.7*x)+0.7*np.exp(0.7*x);
plt.plot(x,y)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:39:41 2018

@author: guweixi
"""

import feature_selection as fs
import numpy as np

class ID3_tree:
    def __init__(self):
        tree_func=[];
    def tree_construct(self,attribute):
        tree_func.append(lambda x, x)
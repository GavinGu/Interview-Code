#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 10:47:37 2018
@author: guweixi
"""

class Gradient_Boost:
    def __init__(self, func, dataset):
        self.F=func;
        self.Residule=[];
        self.Data=dataset;
        step=round(len(dataset)/5);
        self.M=range(1,len(dataset),step);
        print("M:"+str(self.M));
        

    def gradient_boost(self,func, training_dataset):
        f0=func_lst[0];
        #r=[if f0[instance[0]]>instance[1]: 1; elif f0[instance[0]]<instance[1]: -1; else 0;  for instance in training_dataset];
        
    def construct_tree(self):
        for  in self.M:
                        
        
            
        
if __name__ == '__main__':
    ins=[];
    ins.append(((0,1,3),-1));
    ins.append(((0,3,1),-1));
    ins.append(((1,2,2),-1));
    ins.append(((1,1,3),-1));
    ins.append(((1,2,3),-1));
    ins.append(((0,1,2),-1));
    ins.append(((1,1,2),1));
    ins.append(((1,1,1),1));
    ins.append(((1,3,1),-1));
    ins.append(((0,2,1),-1));
    
    Tree=lambda x: 2*(x[0] < 1.5)-1;
    gb=Gradient_Boost(Tree, ins);
    
        
        
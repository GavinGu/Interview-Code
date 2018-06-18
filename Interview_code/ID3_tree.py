#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:39:41 2018

@author: guweixi
"""

import feature_selection as fs
import numpy as np
class node:
     threshold=-1;
     left_branch=-1;
     right_branch=-1;
     leaf_node=False;
     label=-1;
     
class ID3_tree:
    def __init__(self, Dataset,F_index, Label_index):
        tree_func=[];
        tree_Di=0;
        tree_Ai=0;
        self.D_i=Dataset;
        self.Label_index=Label_index;
        self.F_index=F_index;
        
    def entropy_cmp(P):
        shapeP=np.shape(P);
        P_num=shapeP(1);
        H=0;
        for p in P:
            H+=-p*np.log2(p)
        return H;
    
    def maxlikelihoodP_cmp(self,x,y,condition_P):
        likehood_p=0;
        indicator_Y=0;
        indicator_XY=0;
        label=self.D_i(:,self.Label_index);
        feature=self.D_i(:,self.F_index);
        shape=np.shape(label);
        if condition_P==False:
            for label_i in label:
                if y==label_i:
                    indicator_Y+=1;
            likehood_p=indicator_Y/shape(1);
        else:
            for feature_i, label_i in zip(feature, label):
                if feature_i==x and label_i==y:
                    indicator_XY+=1;
            likehood_p=indicator_XY/shape(1);
        return likelihood_p;
    
    def Entropy_gain(self):
        feature=self.Di(:,self.F_index);
        label=self.Di(:,self.Label_index);
    
    def One_Label(label):
        shape=np.shape(np.unique(label));
        if 1==shape(1):
            return True;
        else:
            return False;
        
    def ID3(self.D_i):
        Label_i=self.D_i(:,Label_index);
        Feature_i=self.D_i(:,F_index);
        while true:
            current_node=node();
            if One_Label(Label_i)==True:
                cur
                return  
            
     
if __name__=="__main__":
        # simulate book:
    book_feature=[];
    book_feature.append([0,0,0,0,0,1,1,1,1,1,2,2,2,2,2])
    book_feature.append([0,0,1,1,0,0,0,1,0,0,0,0,1,1,0])
    book_feature.append([0,0,0,1,0,0,0,1,1,1,1,1,0,0,0])
    book_feature.append([0,1,1,0,0,0,1,1,2,2,2,1,1,2,0])
    book_feature.append([0,0,1,1,0,0,0,1,1,1,1,1,1,1,0])
    book_feature=np.transpose(np.asarray(book_feature));
    id3=ID3_tree(book_feature,[1:4],5);
    ID3_tree
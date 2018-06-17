#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:38:32 2018

@author: guweixi
"""

import numpy as np
class simulate_data_with_prob:
    def __init__(self,seq,pro,num):
        self.label_seq=seq;
        self.label_pro=pro;
        self.num=num;
        self.generate_data=[];
        
    def sim_data(self):
        x=np.random.uniform(0,1,self.num);
        for x_item in x:
            for label, pro in zip(self.label_seq, self.label_pro):
                if x_item<pro:
                    self.generate_data.append(label);
                    break;
        return self.generate_data;
    
# feature selection based on information gain
class feature_selection:
    def __init__(self, feature_matrix, label_array):
        self.label=label_array;
        self.feature_array=feature_matrix;
        self.Information_gain=0;
    def multivariant_to_singlevalue(self, feature):
        [row, col]=np.size(feature);
        feature_state=[];
        for r in range(row):
            single_value=0;
            for c in range(col):
                single_value+=(feature(r,c)-1)*np.power(2,c);
            feature_state.append(single_value);
        self.feature_array=np.asarray(feature_state);
        
    def information_gain(self):
        label_set=np.unique(self.label);
        H_D=0;
        for l_state in label_set:
            P_c=sum(self.label==l_state)/len(self.label);
            H_D+=-P_c*np.log2(P_c);
        shape=np.shape(self.feature_array)
        H_A_lst=[];
        
        for f_dim in range(shape[1]):
            H_DA_lst=[];
            cur_feature=self.feature_array[:,f_dim];
            cur_feature_set=np.unique(cur_feature);
            for cur_feature_ele in cur_feature_set:
                H_D_A=0;
                index_lst=[index for index, cur_f in enumerate(cur_feature) if cur_feature_ele==cur_f];
                cur_label=self.label[index_lst];
                cur_label_set=np.unique(cur_label);
                for cur_l_state in cur_label_set:
                    P_ca=sum(cur_label==cur_l_state)/len(cur_label);
                    H_D_A+=-P_ca*np.log2(P_ca);
                P_a=sum(cur_feature==cur_feature_ele)/len(cur_feature);
                H_DA_lst.append(P_a*H_D_A);
            H_DA=sum(np.asarray(H_DA_lst))
            H_A_lst.append(H_DA);
        
        self.Information_gain=np.add(-np.asarray(H_A_lst),H_D);
        
if __name__=='__main__':
    num=15;
    feature_dim=5;
    feature=np.zeros((num,feature_dim), dtype=int);
    # simulte feature:
    seq_lst=[[1,2,3],[1,2],[1,2],[1,2,3,4],[1,2]];
    cum_lst=[[1/3,2/3,1],[1/2,1],[1/2,1],[1/4,2/4,3/4,1],[1/2,1]];
    
    for f in range(feature_dim):
        seq=seq_lst[f];
        cum_pro=cum_lst[f];
        sim=simulate_data_with_prob(seq,cum_pro,num);
        generate_data=sim.sim_data();
        feature[:,f]=np.asarray(generate_data);
    # simulate book:
    book_feature=[];
    book_feature.append([0,0,0,0,0,1,1,1,1,1,2,2,2,2,2])
    book_feature.append([0,0,1,1,0,0,0,1,0,0,0,0,1,1,0])
    book_feature.append([0,0,0,1,0,0,0,1,1,1,1,1,0,0,0])
    book_feature.append([0,1,1,0,0,0,1,1,2,2,2,1,1,2,0])
    book_feature.append([0,0,1,1,0,0,0,1,1,1,1,1,1,1,0])
    book_feature=np.transpose(np.asarray(book_feature));
    
    Y=book_feature[:,4];
    FS=feature_selection(book_feature[:,0:4], Y);
    FS.information_gain();
    print(FS.Information_gain)
    # compute H(D)
     

    
    
    
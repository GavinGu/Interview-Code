#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:20:23 2018

@author: guweixi
"""

from __future__ import division
from numpy import *
import matplotlib.pyplot as plt
class AdaBoost:

    def __init__(self, training_set):
        self.training_set = training_set
        self.N = len(self.training_set)
        self.D_t = ones(self.N)/self.N
        self.weights = ones(self.N)/self.N
        self.RULES = []
        self.ALPHA = []

    def set_rule_pro(self,func,test=False):
        errors=array([(t[1]!=func(t[0])) for t in  self.training_set]); # Train a classifer ht from training dataset under distribution D_T
        Pe=dot(errors,self.D_t);
        print("Pe")
        print(Pe)
        if Pe>0.5:
            print("the current model is not suitable");
    
        alpha_t=0.5*log((1-Pe)/Pe); # alpha_t is a co-efficient for a specific model
        print("alpha_t");
        print(alpha_t);
        
        self.ALPHA.append(alpha_t);
        #P_t=array([(exp(-alpha_t*t[1]*func(t[0]))) for t in self.training_set]);
        
        Z=sum([(exp(-alpha_t*t[1]*func(t[0]))) for t in self.training_set]);
        
        for i in range(self.N):
            #print(P_t);
            t=self.training_set[i];
            if errors[i]==1:
                new_Dt=self.D_t[i]*(exp(-alpha_t*t[1]*func(t[0])));
                print ("initial_dt={0}  update_dt={1}".format(self.D_t[i],new_Dt));
            self.D_t[i]=(self.D_t[i]*exp(-alpha_t*t[1]*func(t[0])))
        self.D_t=self.D_t/sum(self.D_t);
        print("sum_dt={0}".format(sum(self.D_t)))
        self.RULES.append(func);
        print("=========================")
    
    
        
        
    def evaluate_pro(self):
        Func_num=len(self.RULES);
        for (x,l) in self.training_set:
            hx=[self.ALPHA[i]*self.RULES[i](x) for i in range(Func_num)];
            print(x,(l==sign(sum(hx))))    
        
    def set_rule(self, func, test=False):
        errors = array([t[1]!=func(t[0]) for t in self.training_set])
        
        e = (errors*self.weights).sum()
        if test: return e
        alpha = 0.5 * log((1-e)/e)
        #print "e=%.2f a=%.2f" %(e, alpha)
        print ('e={0} a={1}'.format(e, alpha));
        print (e, alpha); 
        w = zeros(self.N)
        for i in range(self.N):
            if errors[i] == 1: w[i] = self.weights[i] * exp(alpha)
            else: w[i] = self.weights[i] * exp(-alpha)
        self.weights = w / w.sum()
        self.RULES.append(func)
        self.ALPHA.append(alpha)
    
    def evaluate(self):
        
        NR = len(self.RULES)
        for (x,l) in self.training_set:
            hx = [self.ALPHA[i]*self.RULES[i](x) for i in range(NR)]
            print (x, sign(l) == sign(sum(hx)))
        
if __name__ == '__main__':

    examples = []
    examples.append(((1,  2  ), 1))
    examples.append(((1,  4  ), 1))
    examples.append(((2.5,5.5), 1))
    examples.append(((3.5,6.5), 1))
    examples.append(((4,  5.4), 1))
    examples.append(((2,  1  ),-1))
    examples.append(((2,  4  ),-1))
    examples.append(((3.5,3.5),-1))
    examples.append(((5,  2  ),-1))
    examples.append(((5,  5.5),-1))
    
    x_lst=[e[0] for e in examples];
    x1_lst=[];
    x2_lst=[];
    for x_tuple in x_lst:
        x1_lst.append(x_tuple[0]);
        x2_lst.append(x_tuple[1]);
    
    y=[e[1] for e in examples];
    
    plt.plot(x1_lst,x2_lst,y);
    
    m = AdaBoost(examples)
    print(m);
    #m.set_rule(lambda x: 2*(x[0] < 1.5)-1)
    #m.set_rule(lambda x: 2*(x[0] < 4.5)-1)
    #m.set_rule(lambda x: 2*(x[1] > 5)-1)
    
    m.set_rule_pro(lambda x: 2*(x[0] < 1.5)-1)
    m.set_rule_pro(lambda x: 2*(x[0] < 4.5)-1)
    m.set_rule_pro(lambda x: 2*(x[1] > 5)-1)
    m.evaluate_pro()
    
    
    
    
    
    
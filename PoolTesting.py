# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:55:53 2020

@author: Sajinu
"""
import numpy as np
from matplotlib import pyplot as plt

class Pool_Test:
    def __init__(self,P=100,npct=0.50):
        self.test_results={}
        self.P=P
        self.npct=npct
        self.threshold=npct
        self.sample_pop = np.random.uniform(low=0,high=1,size=self.P)
        self.infected_pop = self.sample_pop[self.sample_pop > self.npct]
        self.negative_pop = self.sample_pop[self.sample_pop <= self.npct]
        self.all_test_result=[]
    
    def do_poolTest(self):
        self.test_and_divide(self.sample_pop)
    
    def test_and_divide(self,given_pop):
        curr_size=np.size(given_pop)
        if(curr_size==0):
            return
        test_result=self.check_sample_positive(given_pop)
        self.all_test_result.append(test_result)
        #print("data:",given_pop)
        #print("size,result",curr_size,test_result)
        if(curr_size==1):
            return
        if test_result == False:
            return
        if(curr_size>1):
            first_sample=given_pop[:curr_size//2]
            second_sample=given_pop[curr_size//2:]
            self.test_and_divide(first_sample)
            self.test_and_divide(second_sample)

    def check_sample_positive(self,given_pop):
        if(np.size(given_pop[given_pop>self.threshold])==0):
            return False
        else:
            return True

test_count=[]
pct_infected=range(0,101,1)
repeat=50
P=100 # population
for icount in pct_infected:
    value=0
    #print(icount)
    for jcount in range(repeat):
        myPoolTest=Pool_Test(P,(100-icount)/100)
        #print("data :",myPoolTest.sample_pop)
        myPoolTest.do_poolTest()
        #print("No of tests : ",np.size(myPoolTest.all_test_result))
        #print("Test results : ",myPoolTest.all_test_result)
        value+=np.size(myPoolTest.all_test_result)
    test_count.append(value/repeat)

fig, axs = plt.subplots(1, 1)
axs.plot(pct_infected,test_count,".b")
axs.set_xlabel("Percentage of infected")
axs.set_ylabel("No of test kits")
#title_text="Test kit per "+str(P)+" people"
axs.set_title('Test kit per '+str(P)+' people')
axs.grid(True)
plt.show()

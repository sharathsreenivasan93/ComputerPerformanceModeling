# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:50:51 2015

@author: sharathsreenivasan
"""

import math
import pandas as pd

down_time_list = []

def calculate(operational_time):
    global down_time_list
    repair_time = 5.0
    po=calculatep0(operational_time,repair_time)
    w = float((3/(1-po) * repair_time)) - operational_time
    down_time_list.append(w)
    
def calculatep0(operational_time,repair_time):
    sum = 0.0
    for i in range(0,4):
        sum = sum + (math.factorial(3)/math.factorial(3-i)) * math.pow(float(repair_time/operational_time),i)
    p0 = float(1/sum)
    return p0

if __name__ == '__main__':
    for i in range(1,51):
        calculate(i)
    df1 = pd.DataFrame(down_time_list)
    df1.to_csv('assignment4b.csv')
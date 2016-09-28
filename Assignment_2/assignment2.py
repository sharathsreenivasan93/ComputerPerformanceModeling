# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:35:45 2015

@author: sreenivasanh
"""

import random

indi_clock_list=[1.0,4.0,9.0,-1.0]
in_queue_list=[]
mc=0.0
number_in_queue=0
repair_time_mean = 0.0
operational_time_mean = 0.0
operational_time = 0.0
repair_time = 0.0

def min_pos(n):
    min_value=100
    min_pos=-1
    k=0
    for i in n:
        if i<min_value and i!=-1:
            min_value=i
            min_pos=k
        k=k+1
    return min_pos

def min_val(n):
    min_value=100
    for i in n:
        if i<min_value and i!=-1:
            min_value=i
    return min_value

def arrival():
    global mc
    global indi_clock_list
    global number_in_queue
    global in_queue_list
    global operational_time_mean
    global repair_time_mean
    global repair_time
    global operational_time
    repair_time = random.expovariate(1.0/repair_time_mean)
    i_pos=min_pos(indi_clock_list)
    mc=indi_clock_list[i_pos]
    if indi_clock_list[3] < mc:
        indi_clock_list[3]=mc+repair_time
    in_queue_list.append(i_pos)
    indi_clock_list[i_pos]=-1
    number_in_queue=number_in_queue+1
    return

def departure():
    global mc
    global indi_clock_list
    global number_in_queue
    global in_queue_list
    global operational_time_mean
    global repair_time_mean
    global repair_time
    global operational_time
    pos=in_queue_list.pop(0)
    repair_time = random.expovariate(1.0/repair_time_mean)
    operational_time = random.expovariate(1.0/operational_time_mean)
    indi_clock_list[pos]=mc+operational_time
    number_in_queue=number_in_queue-1
    indi_clock_list[3]=mc+repair_time
    return

def event_caller():
    global mc
    global indi_clock_list
    global number_in_queue
    global repair_time_mean
    global operational_time_mean
    global repair_time
    global operational_time
    mc=1
    repair_time_mean = float(input("Enter the mean repair time\n"))
    operational_time_mean = float(input("Enter the mean operational time\n"))
    if operational_time_mean < repair_time_mean:
        print "Input the mean repair and operational time again. Mean operational time > Mean repair time"
        event_caller()
    else:
        max_mc = input("Enter the maximum value for the master clock\n")
        print "Output is  of the form -\n"
        print "mc [CL1, CL2, CL3, CL4] n operational_time repair_time\n"
        print mc, indi_clock_list, number_in_queue
        while mc<max_mc:
            mc = min_val(indi_clock_list)
            if min_val(indi_clock_list[0:3]) == indi_clock_list[3]:
                departure()            
                arrival()
            elif mc == indi_clock_list[3] and number_in_queue>0:
                departure()
            else:
                arrival()
            if mc < max_mc:
                print round(mc,2),"[" ,round(indi_clock_list[0],2), round(indi_clock_list[1],2), round(indi_clock_list[2],2), round(indi_clock_list[3],2), "]" ,number_in_queue, round(operational_time,2), round(repair_time,2)
            
if __name__ == '__main__':
    event_caller()
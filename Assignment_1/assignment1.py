# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:35:45 2015

@author: sreenivasanh
"""

indi_clock_list=[1,4,9,-1]
in_queue_list=[]
mc=0
number_in_queue=0
service_time = 0
operational_time = 0

def min_pos(n):
    i = min_val(n)
    min_pos = n.index(i)
    return min_pos

def min_val(n):
    min_value=5000
    for i in n:
        if i<min_value and i!=-1:
            min_value=i
    return min_value

def arrival():
    global mc
    global indi_clock_list
    global number_in_queue
    global in_queue_list
    global operational_time
    global repair_time
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
    global operational_time
    global repair_time
    pos=in_queue_list.pop(0)
    indi_clock_list[pos]=mc+operational_time
    number_in_queue=number_in_queue-1
    indi_clock_list[3]=mc+repair_time
    return

def event_caller():
    global mc
    global indi_clock_list
    global number_in_queue
    global repair_time
    global in_queue_list
    global operational_time
    mc=1
    repair_time = input("Enter repair time\n")
    operational_time = input("Enter operational time\n")
    n = input("Enter the number of iterations\n")
    print "Output is  of the form -\n"
    print "mc [CL1, CL2, CL3, CL4] n\n"
    print mc, indi_clock_list, number_in_queue
    i = 1
    while i<=n:
        mc = min_val(indi_clock_list)
        if min_val(indi_clock_list[0:3]) == indi_clock_list[3]:
            departure()            
            arrival()
        elif mc == indi_clock_list[3] and number_in_queue>0:
            departure()
        else:
            arrival()
        i = i+ 1
        print mc, indi_clock_list, number_in_queue, in_queue_list
            
if __name__ == '__main__':
    event_caller()
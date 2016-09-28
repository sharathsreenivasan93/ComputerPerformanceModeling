# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:35:45 2015

@author: sreenivasanh
"""

import random
import numpy
import math

indi_clock_list=[1.0,4.0,9.0,-1.0]
in_queue_list=[]
mc=0.0
number_in_queue=0
repair_time_mean = 0.0
operational_time_mean = 0.0
operational_time = 0.0
repair_time = 0.0
start_time=[0,0,0]
break_down_time=[]
counter = 0

def min_pos(n):
    i = min_val(n)
    min_pos = n.index(i)
    return min_pos

def min_val(n):
    min_value=50000
    for i in n:
        if i<=min_value and i!=-1:
            min_value=i
    return min_value

def arrival():
    global mc
    global indi_clock_list
    global number_in_queue
    global in_queue_list
    global repair_time
    global start_time
    if mc == indi_clock_list[3] and number_in_queue == 0:
        mc = min_val(indi_clock_list[0:3])
        i_pos=indi_clock_list.index(mc)
    else:
        i_pos=min_pos(indi_clock_list)
        mc=indi_clock_list[i_pos]
    if number_in_queue==0:
        indi_clock_list[3]=mc+repair_time
    in_queue_list.append(i_pos)
    start_time[i_pos]=mc
    indi_clock_list[i_pos]=-1
    number_in_queue=number_in_queue+1
    return

def departure():
    global mc
    global indi_clock_list
    global number_in_queue
    global in_queue_list
    global repair_time
    global operational_time
    global break_down_time
    pos=in_queue_list.pop(0)
    break_down_time.append(mc - start_time[pos])
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
    global in_queue_list
    global break_down_time
    mc=1
    repair_time_mean = float(input("Enter the mean repair time\n"))
    operational_time_mean = float(input("Enter the mean operational time\n"))
    number_in_each_batch = int(input("Enter the number of elements in each batch\n"))
    number_of_batches = int(input("Enter the number of batches\n"))    
    if operational_time_mean < repair_time_mean:
        print "Input the mean repair and operational time again. Mean operational time > Mean repair time"
        event_caller()
    else:
        while len(break_down_time)<=10000:
            mc = min_val(indi_clock_list)
            repair_time = random.expovariate(1.0/repair_time_mean)
            operational_time = random.expovariate(1.0/operational_time_mean)
            if min_val(indi_clock_list[0:3]) == indi_clock_list[3]:
                departure()            
                arrival()
            elif mc == indi_clock_list[3] and number_in_queue>0:
                departure()
            else:
                arrival()
        
        break_down_time_rounded = [ round(elem, 2) for elem in break_down_time ]
        mean = numpy.mean(break_down_time_rounded[50:1050])
        standard_deviation = numpy.std(break_down_time_rounded[50:1050])
        #correlogram(break_down_time_rounded[50:1050])
        print "BEFORE BATCH MEANS METHOD"        
        print "Mean of 1000 elements = ",mean
        print "Standard Deviation of 1000 elements = ",standard_deviation 
        print "AFTER BATCH MEANS METHOD"        
        batchmeans(break_down_time_rounded[51:],number_in_each_batch,number_of_batches)

def batchmeans(n,number_in_each_batch,number_of_batches):
    batch_means=[]
    i=0
    while i <= number_in_each_batch*number_of_batches:
        sum = 0
        for j in range(i,i+number_in_each_batch):
            sum = sum + n[j]
        batch_means.append(float(sum/number_in_each_batch))
        i = i + number_in_each_batch
    mean_of_batch_means = numpy.mean(batch_means)
    sum = 0.0
    for i in batch_means:
        sum = sum + (i - mean_of_batch_means)*(i - mean_of_batch_means)
    square_sum = float(sum/(number_of_batches-1))
    sum = math.sqrt(square_sum)
    ci_lower = mean_of_batch_means - (1.96)*(sum/math.sqrt(number_of_batches))
    ci_higher = mean_of_batch_means + (1.96)*(sum/math.sqrt(number_of_batches))
    delta = ci_higher - ci_lower
    ratio = float (delta/mean_of_batch_means)
    if ratio > 0.1:
        k2 = math.pow((delta/(0.1*mean_of_batch_means)),2)*number_of_batches   
        batchmeans(n,number_in_each_batch,k2)
    else:
        print "Ratio after sequential procedure = ",ratio
        print "Lower CI = ",ci_lower
        print "Higher CI = ",ci_higher
        print "CI Range = ",delta
        print "Mean obtained from batch means method = ",mean_of_batch_means
        percentile = numpy.percentile(n,95)
        print "95% Percentile = ",percentile
"""
def correlogram(break_down_time):
    print "To obtain correlogram for 1000 elements"
    xcoordinates_list = []
    ycoordinates_list = []
    avg = numpy.mean(break_down_time)
    variance = numpy.var(break_down_time)
    for j in range(1,11):
        sum_y = 0.0
        for i in range(0,(len(break_down_time)-j-1)):
            sum_y = sum_y + (break_down_time[i]-avg)*(break_down_time[i+j]-avg)
        sumbyn = sum_y/len(break_down_time)
        rk = float(sumbyn/(variance*variance))
        ycoordinates_list.append(rk)
        xcoordinates_list.append(j)
    print xcoordinates_list
    print ycoordinates_list
"""    
    
if __name__ == '__main__':
    event_caller()
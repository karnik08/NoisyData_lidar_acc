#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:51:43 2021

@author: oorjamajgaonkar
"""
'''
FORMAT OF ACCURACY DICTIONARY
training size : [[train accuracy, test accuracy, class accuracy], ... ]

key: training size (40, 120, etc.)
value: array of 100 arrays (one for each epoch)

'''
import json
acc = {}
ind = -1
sizes = [40, 120, 240, 320, 400, 600, 800, 1000]
test_size = [40]
for size in sizes:
    with open (f'/Users/oorjamajgaonkar/Documents/capstone/Pointnet_Pointnet2_pytorch/log/logfile-{size}-balanced.txt', 'r') as f:
        for line in f:
            if line.find("Epoch") != -1:
                epoch = int(line.split(" ")[-2]) # epoch number
                #ind += 1
            elif line.find("Train Instance Accuracy") != -1:
                arr = [float(line.split(": ")[1])]
            elif line.find("Test Instance Accuracy") != -1:
                arr.append(float(line.split(" ")[-4].strip(","))) # overall test accuracy
                arr.append(float(line.split(" ")[-1])) # class accuracy
                if size in acc:
                    acc[size].append(arr)
                else:
                    acc[size] = []
                    acc[size].append(arr)
                
import matplotlib.pyplot as plt
acc_array = []
for size in sizes:
    acc_array.append([a[1] for a in acc[size]])
# xvals = []
# for size in sizes[:-1]:
#     xvals.append([size * i for i in range(1, 101)])
# xvals.append([800*i for i in range(1, 121)])
# ind = 0
# for arr in acc_array:
#     plt.plot(xvals[ind], arr, label = str(sizes[ind]))
#     ind += 1
# plt.figure(num=1, figsize=(20, 10))
# plt.legend()
# plt.axis([0, 10000, 0, 0.7])
# plt.show()

with open("sample.json", "w") as outfile: 
    json.dump(acc_array, outfile)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:54:45 2016

@author: tranlaman
"""
import json
import matplotlib.pyplot as plt
import numpy as np

json_file = 'activity_net.v1-3.min.json'
with open(json_file, "r") as fobj:
    anet_v_1_0 = json.load(fobj)
    
database = anet_v_1_0.get('database')
data_values = database.values()
durations = []
for sample in data_values:
    dur = sample.get('duration')
    durations.append(dur)
assert(len(durations) == len(data_values))

# some statistics of 
print('total number of videos: %0.2f' % len(durations))
print('min, max duration: %0.2f, %0.2f' % (np.min(durations), np.max(durations)))
print('mean, median duration: %0.2f, %0.2f' % (np.mean(durations), np.median(durations))) 
print('5, 95 quantiles of duration: %0.2f, %0.2f' % (np.percentile(durations, 5), np.percentile(durations, 95)))

# draw histogram
n, bins, patches = plt.hist(durations, 50, normed=True, facecolor='green', alpha=0.75)
plt.title('Histogram of video durations in ActivityNet dataset')
plt.ylabel('Frequency')
plt.xlabel('Duration in seconds')
plt.show()
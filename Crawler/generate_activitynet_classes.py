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
labels = []
for sample in data_values:
    subset = sample.get('subset')
    if subset == 'training':
        annotations = sample.get('annotations')
        for ann in annotations:
            label = ann.get('label')
            labels.append(label)

classes = np.unique(labels)
# write it into files
fid = open('classes.txt', 'w')
for cl in classes:
    fid.write('%s\n' % cl)
fid.close()

samples_per_class = dict((k, 0) for k in classes)
# counting number of samples per categories
for sample in data_values:
    subset = sample.get('subset')
    if subset == 'training':
        annotations = sample.get('annotations')
        for ann in annotations:
            label = ann.get('label')
            labels.append(label)
            samples_per_class[label] += 1

# draw bar chart
heights = []        # heights according to the class names
for label in classes:
    heights.append(samples_per_class[label])
    
fig = plt.figure(1)
plt.bar(np.arange(len(classes)), heights, color='r')
fig.suptitle('General graph: number of samples per class')
plt.waitforbuttonpress()

# visualize bar chart in a segment
num_figure = 4
segment = len(classes)/num_figure
h_index = 0
fig = plt.figure(2)
for ind in xrange(num_figure):
    plt.barh(np.arange(segment), heights[h_index:h_index+segment], color='g', tick_label=classes[h_index:h_index+segment])
    title = 'Number of samples per class: %d/%d' % (ind + 1, num_figure)
    fig.suptitle(title)
    plt.waitforbuttonpress()
    fig.clear()
    h_index += segment

plt.show()

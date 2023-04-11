# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:49:28 2023

@author: aaron
"""

import numpy as np
import matplotlib.pyplot as plt

# reading the data and storing it as an array
data = np.genfromtxt('data7.csv')

# creating distribution array and class interval edges for histogram
dist, edge = np.histogram(data, bins=32, range=[np.round(min(data) - 0.01, 2),
                                                np.round(max(data) + 0.01, 2)])

# calculating centre of each class interval
xdist = 0.5 * (edge[1:] + edge[:-1])
# calculating width of each class interval
wdist = edge[1:] - edge[:-1]

# normalising the distribution
ydist = dist / np.sum(dist)

# calculating the average
avg = np.sum(xdist * ydist)

# calculating the value X such that 0.75 of the distribution are below X
# cumulative distribution
cdist = np.cumsum(ydist)


# plotting histogram
plt.figure()
plt.bar(xdist, ydist, width=0.9*wdist)

# plotting and displaying mean
plt.plot([avg, avg], [0.0, max(ydist)], c='red')
text = ''' Average weight: {}kg'''.format(np.round(avg, 2))
plt.text(x=avg, y=max(ydist) + 0.001, s=text, c='red')

plt.show()

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
cdist = np.cumsum(ydist)
indx = np.argmin(np.abs(cdist - 0.75))
X = edge[indx]


# plotting histogram
plt.figure(figsize=(11, 8))
plt.bar(xdist, ydist, width=0.9*wdist)

plt.xticks(edge[::4], fontsize=17)
plt.yticks(np.linspace(min(ydist), max(ydist), num=10), fontsize=15)

plt.xlabel('Weight (kg)', fontsize=22)
plt.ylabel('Probability', fontsize=22)
plt.title('Distribution of Weight of Newborns', fontsize=25)

# plotting and displaying mean
plt.axvline(avg, ymax=0.76, c='black', linestyle='-.',
            label='W˜(Average Weight)')
text1 = '''W˜= {}kg'''.format(np.round(avg, 2))
plt.text(x=3.05, y=0.0725, s=text1, fontsize=20, c='black')

# plotting and displaying X value
plt.axvline(X, ymax=0.97, c='red', linestyle='-.',
            label='X(75% are born with a weight above X)')
text2 = '''X = {}kg'''.format(np.round(X, 2))
plt.text(x=X + 0.01, y=max(ydist) + 0.0008, s=text2, fontsize=19, c='red')
plt.bar(xdist[:indx], ydist[:indx], width=0.9*wdist[:indx], color='green')

plt.legend(fontsize=14)
plt.show()

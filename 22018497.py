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

# plotting histogram
plt.figure(figsize=(11, 8))

plt.bar(xdist, ydist, width=0.9*wdist)

plt.xticks(edge[::4], fontsize=17)
plt.yticks(np.linspace(0, 0.1, 11), fontsize=17)

plt.xlabel('Weight (kg)', fontsize=22)
plt.ylabel('Probability', fontsize=22)
plt.title('Distribution of Weight of Newborns', fontsize=25)


# calculating the average
avg = np.sum(xdist * ydist)

# plotting and displaying mean
text1 = r'$\tilde{W} = $' + str(np.round(avg, 2)) + 'kg'
plt.axvline(avg, c='black', lw=3.25, linestyle='-.', label=text1)


# calculating the value X such that 0.75 of the distribution are below X
cdist = np.cumsum(ydist)
indx = np.argmin(np.abs(cdist - 0.75))
X = edge[indx]

# plotting and displaying X value
text2 = 'X = {}kg'.format(np.round(X, 2))
plt.axvline(X, c='red', lw=3.25, linestyle='--', label=text2)

plt.bar(xdist[:indx], ydist[:indx], width=0.9*wdist[:indx], color='green',
        label='75% of the distribution')


# customising legend
plt.legend(loc='upper left', fancybox=True, shadow=True, borderpad=1,
           fontsize=16)
# showing the plot
plt.show()

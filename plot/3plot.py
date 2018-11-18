# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
from numpy.random import randn
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plot_data1 = randn(50).cumsum()
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.plot(plot_data1,marker=r'o',color=u'blue',linestyle='-',label='Blue Solid')
ax1.plot(plot_data2,marker=r'+',color=u'red',linestyle='--',label='Red Dashed')
ax1.plot(plot_data3,marker=r'*',color=u'green',linestyle='-.',label='Green Dash Dot')
ax1.plot(plot_data4,marker=r's',color=u'orange',linestyle=':',label='Orange Dotted')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Draw')
plt.ylabel('Random Number')

plt.legend(loc='best')

plt.savefig('img/line_plot.png',dpi=400,bbox_inches='tight')
plt.show()

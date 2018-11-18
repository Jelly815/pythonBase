# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

#Data
fig,axes = plt.subplots(nrows=1,ncols=2)
ax1,ax2 = axes.ravel()
data_frame = pd.DataFrame(np.random.rand(5,3),index=['Customer 1','Customer 2','Customer 3','Customer 4','Customer 5'],columns=pd.Index(['Metric 1','Metric 2','Metric 3'],name='Metrics'))
data_frame.plot(kind='bar',ax=ax1,alpha=0.75,title='Bar Plot')

plt.setp(ax1.get_xticklabels(),rotation=45,fontsize=10)
plt.setp(ax1.get_yticklabels(),rotation=0,fontsize=10)

ax1.set_xlabel('Customer')
ax1.set_ylabel('Value')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.title('Box plots:Resampling of Two Distributions')
plt.xlabel('Distribution')
plt.ylabel('Value')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

colors = dict(boxes='DarkBlue',whiskers='Gray',medians='Red',caps='Black')

data_frame.plot(kind='box',color=colors,sym='r.',ax=ax2,title='Box Plot')

plt.setp(ax2.get_xticklabels(),rotation=45,fontsize=10)
plt.setp(ax2.get_yticklabels(),rotation=0,fontsize=10)

ax2.set_xlabel('Metric')
ax2.set_ylabel('Value')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

plt.savefig('img/6plot.png',dpi=400,bbox_inches='tight')
plt.show()

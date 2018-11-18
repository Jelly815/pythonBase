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
N=500
normal = np.random.normal(loc=0.0,scale=1.0,size=N)
lognormal = np.random.lognormal(mean=0.0,sigma=1.0,size=N)
index_value = np.random.randint(low=0,high=N-1,size=N)
normal_sample = normal[index_value]
lognormal_sample = normal[index_value]
box_plot_data = [normal,normal_sample,lognormal,lognormal_sample]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#繪圖
box_lables= ['normal','normal_sample','lognormal','lognormal_sample']
ax1.boxplot(box_plot_data,notch=False,sym='.',vert=True,whis=1.5,showmeans=True,labels=box_lables)

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.title('Box plots:Resampling of Two Distributions')
plt.xlabel('Distribution')
plt.ylabel('Value')

#....

plt.savefig('img/5plot.png',dpi=400,bbox_inches='tight')
plt.show()

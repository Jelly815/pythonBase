# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig

sns.set(color_codes=True)

#長條圖
x=np.random.normal(size=100)
sns.distplot(x,bins=20,kde=False,rug=True,label="Histogram w/o Density")
sns.utils.axlabel("Value","Frequency")
plt.title("Histogram of a Random Sample from a Normal Distribution")
plt.legend()

#散布圖,包含回歸線與單變數圖
mean,cov = [5,10],[(1,.5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)
data_frame = pd.DataFrame(data,columns=["x","y"])
sns.jointplot(x="x",y="y",data=data_frame,kind="reg").set_axis_labels("x","y")
plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")

#成對雙變量散布圖與單變量色階分布圖
iris=sns.load_dataset("iris")
sns.pairplot(iris)

#各種變數條件的盒鬚圖
tips = sns.load_dataset("tips")
sns.factorplot(x="time",y="total_bill",hue="smoker",col="day",data=tips,kind="box",size=4,aspect=.5)

#使用複式抽樣信賴區間的線性迴歸
sns.lmplot(x="total_bill",y="tip",data=tips)

#使用複式抽樣信賴區間的羅吉斯迴歸
tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill",y="big_tip",data=tips,logistic=True,y_jitter=.03).set_axis_labels("Total Bill","Big Tip")

plt.title("Logistic Regression of Big Tip vs. Total Bill")
plt.show()
savefig("img/8plot.png")


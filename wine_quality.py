# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:27:49 2018

@author: hgiga
"""

#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols,glm

#將資料集讀入pandas DataFrame
wine = pd.read_csv('data/winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')
print("\r\n將資料集讀入pandas DataFrame\r\n",wine.head())

#顯示所有變數的描述性統計
print("\r\n顯示所有變數的描述性統計\r\n",wine.describe())

#找出不重複的值
print("\r\n找出不重複的值\r\n",sorted(wine.quality.unique()))

#計算值的頻率
print("\r\n計算值的頻率\r\n",wine.quality.value_counts())

#按照酒的類型來顯示品質的描述性統計數據
print("\r\n按照酒的類型來顯示品質的描述性統計數據\r\n",wine.groupby('type')[['quality']].describe().unstack('type'))

#按照酒的類型，顯示特定的品質分位值
print("\r\n照酒的類型，顯示特定的品質分位值\r\n",wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))

#按照酒的類型，查看品質的分布
red_wine = wine.loc[wine['type']=='red','quality']
white_wine = wine.loc[wine['type'] == 'white','quality']

sns.set_style('dark')
print("\r\n紅酒品質的分布\r\n",sns.distplot(red_wine,norm_hist=True,kde=False,color="red",label="Red wine"))
print("\r\n白酒品質的分布\r\n",sns.distplot(white_wine,norm_hist=True,kde=False,color="white",label="White wine"))

sns.utils.axlabel("Quality Score","Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

#測試紅酒與白酒的平均品質是否不同
print("\r\n測試紅酒與白酒的平均品質是否不同\r\n",wine.groupby(['type'])[['quality']].agg(['std']))

tstat,pvalue,df = sm.stats.ttest_ind(red_wine,white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat,pvalue))

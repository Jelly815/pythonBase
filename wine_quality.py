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
print("\n將資料集讀入pandas DataFrame\n",wine.head())

#顯示所有變數的描述性統計
print("\n顯示所有變數的描述性統計\n",wine.describe())

#找出不重複的值
print("\n找出不重複的值\n",sorted(wine.quality.unique()))

#計算值的頻率
print("\n計算值的頻率\n",wine.quality.value_counts())

#按照酒的類型來顯示品質的描述性統計數據
print("\n按照酒的類型來顯示品質的描述性統計數據\n",wine.groupby('type')[['quality']].describe().unstack('type'))

#按照酒的類型，顯示特定的品質分位值
print("\n照酒的類型，顯示特定的品質分位值\n",wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))

#按照酒的類型，查看品質的分布
red_wine = wine.loc[wine['type']=='red','quality']
white_wine = wine.loc[wine['type'] == 'white','quality']

sns.set_style('dark')
print("\n紅酒品質的分布\n",sns.distplot(red_wine,norm_hist=True,kde=False,color="red",label="Red wine"))
print("\n白酒品質的分布\n",sns.distplot(white_wine,norm_hist=True,kde=False,color="white",label="White wine"))

sns.utils.axlabel("Quality Score","Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

#測試紅酒與白酒的平均品質是否不同
print("\n測試紅酒與白酒的平均品質是否不同\n",wine.groupby(['type'])[['quality']].agg(['std']))

tstat,pvalue,df = sm.stats.ttest_ind(red_wine,white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat,pvalue))

#計算所有變數的相關性矩陣
print("\n計算所有變數的相關性矩陣\n",wine.corr())

#取出"一小部分"的紅酒與白酒樣本來繪圖
def take_sample(data_frame,replace=False,n=200):
    return data_frame.loc[np.random.choice(data_frame.index,replace=replace,size=n)]

reds_sample = take_sample(wine.loc[wine['type']=='red',:])
whites_sample = take_sample(wine.loc[wine['type']=='white',:])
wine_sample = pd.concat([reds_sample,whites_sample])

wine['in_sample']=np.where(wine.index.isin(wine_sample.index),1.,0.)
print("\n取出'一小部分'的紅酒與白酒樣本來繪圖\n",pd.crosstab(wine.in_sample,wine.type,margins=True))

#查看每一對變數之間的關係
sns.set_style("dark")
g = sns.pairplot(wine_sample,kind='reg',plot_kws={"ci":False,"x_jitter":0.25,"y_jitter":0.25},hue='type',diag_kind='hist',diag_kws={"bins":10,"alpha":1.0},palette=dict(red="red",white="white"),markers=["o","s"],vars=['quality','alcohol','residual_sugar'])
print("\n查看每一對變數之間的關係\n",g)

plt.suptitle('Histograms and Scatter Plots of Quality,Alcohol,and Residual Sugar',fontsize=14,horizontalalignment='center',verticalalignment='top',x=0.5,y=0.999)
plt.show()

#使用statsmodels套件來執行線性迴歸:
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity +free_sulfur_dioxide +pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'

lm = ols(my_formula,data=wine).fit()

#或者，使用廣義線性模型(glm)語法的線性迴歸
#lm=glm(my_formula,data=wine,family=sm.families.Gaussian()).fit()

print(lm.summary())
print("\n你可以從結果中提取的數量:\n%s" % dir(lm))
print("\n係數:\n%s" % lm.params)    #係數
print("\n係數標準錯誤:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f P-value: %.2f" % (lm.fvalue,lm.f_pvalue))
print("\n觀察次數: %d Number of fitted values: %d" % (lm.nobs,len(lm.fittedvalues)))

#標準化自變數
#建立一個Series Dependent_variable來保存原始資料集
dependent_variable = wine['quality']

#建立一個DataFrame independent_variables來保存原始資料
#除了quality,type與in_sample之外的所有變數
independent_variables=wine[wine.columns.difference(['quality','type','in_sample'])]

#標準化自變數,對於每一個變數，將每一個觀測值減去變數的平均值(mean)
#並將結果除以變數的標準差(std)
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()

#將應變數quality加為自變數的DataFrame的一個欄位
#來以標準化的自變數建立一個新資料集
wine_standardized = pd.concat([dependent_variable,independent_variables_standardized],axis=1)

lm_standardized = ols(my_formula,data=wine_standardized).fit()
print(lm_standardized)

new_observations = wine.loc[wine.index.isin(range(10)),independent_variables.columns]
#使用新觀測紀錄的特性來預測品質分數
y_predicted = lm.predict(new_observations)
#將預測值進位成兩位小數,並將它們印到螢幕
y_predicted_rounded = [round(score,2) for score in y_predicted]
print(y_predicted_rounded)
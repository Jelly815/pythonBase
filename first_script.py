# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:25:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
from math import exp,log,sqrt

print("output #1:learn python")

#將兩數字相加
x=4
y=5
z=x+y
print("Output #2:Four plus five equals {0:d}.".format(z))
      
a = [1,2,3,4]
b = ["first","second","three","four"]
c=a+b
print("Output #3:{0},{1},{2}".format(a,b,c))
      
x=9
print("Output #4:{0}".format(x))
print("Output #5:{0}".format(3**4))
print("Output #6:{0}".format(int(8.3)/int(2.7)))
      
print("Output #7:{0:.3f}".format(8.3/2.7))
y=2.5*4.8
print("Output #8:{0:.1f}".format(y))
r=8/float(3)
print("Output #9:{0:.2f}".format(r))
print("Output #10:{0:4f}".format(8.0/3))
      
print("Output #11:{0:4f}".format(exp(3)))  
print("Output #12:{0:2f}".format(log(4)))   
print("Output #13:{0:1f}".format(sqrt(81))) #平方根

string1 = "This is a "
string2 = "short string."
sentence = string1+string2
print("Output #18:{0:s}".format(sentence))
print("Output #19:{0:s} {1:s}{2:s}".format("She is","very "*4,"beautiful."))
m = len(sentence)
print("Output #20:{0:d}".format(m))
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:25:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
from math import exp,log,sqrt

#############String#############
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
print("Output #13:{0:1f}".format(sqrt(81))) # 平方根

string1 = "This is a "
string2 = "short string."
sentence = string1+string2
print("Output #18:{0:s}".format(sentence))
print("Output #19:{0:s} {1:s}{2:s}".format("She is","very "*4,"beautiful."))
m = len(sentence)
print("Output #20:{0:d}".format(m))
#############Split#############      
string1 =  "My deliverable is due in May"
string1_list1=string1.split()
string1_list2=string1.split(" ",3)      # 3是分割幾次    
print("Output #21:{0}".format(string1_list1))
print("Output #22:FIRST PIECE:{0}。SECOND PIECE:{1}。THIRD PIECE:{2}。4 PIECE:{3}。"\
      .format(string1_list2[0],string1_list2[1],string1_list2[2],string1_list2[3])) 

string2 =  "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23:{0}".format(string2_list))
print("Output #24:{0} {1} {2}".format(string2_list[1],string2_list[5],\
      string2_list[-1]))
#############Join############# 
print("Output #25:{0}".format(','.join(string1_list1)))
#############Strip#############
string3 = " Remove  unwanted characters  from this string.\t\t  \n"
print("Output #26:string3: {0:s}".format(string3))
string3_lstrip=string3.lstrip()     # 移除左側空格
print("Output #27:lstrip: {0:s}".format(string3_lstrip))
string3_rstrip=string3.rstrip()     # 移除右側空格,tab與換行字元
print("Output #28:rstrip: {0:s}".format(string3_rstrip)) 
string3_strip=string3.strip()       # 移除兩側空格,tab與換行字元
print("Output #29:strip: {0:s}".format(string3_strip)) 

string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30:strip: {0:s}".format(string4))
string4 = "$$Here's unwanted characters have been removed.__---++" 
string4_strip = string4.strip('$_-+')    # 移除其他字元
print("Output #31: {0:s}".format(string4_strip))   

#############Replace#############
string5 = "Let's replace the spaces in this sentence with other characters"
string5_replace=string5.replace(" ","!@!")
print("Output #32 (with !@!):{0:s}".format(string5_replace))
string5_replace=string5.replace(" ",",")
print("Output #33 (with commas):{0:s}".format(string5_replace))

#############lower,upper ,capitalize#############
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's WHAT Happens WHEN You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string8 = "Here's WHAT Happens WHEN You Use Capitalize."
print("Output #36: {0:s}".format(string8.capitalize()))
string8_list = string8.split()
print("Output #37 (on each word):")
for word in string8_list:
    print("{0:s}".format(word.capitalize()))
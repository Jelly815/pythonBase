# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:25:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta

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
    
#############regexp#############
#每次在字串發現組合時，就印出它
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)",re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))
        
#將字串中的單字'the'換成字母'a'
string = 'The quick brown fox jumps over the lazy dog.'
string_to_find = r"The"
pattern = re.compile(string_to_find,re.I)
print("Output #40: {:s}".format(pattern.sub("a",string)))

#############datetime#############
#印出今天日期以及年、月、日
today = date.today()
print("Output #41: today:{0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #43: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))
      
#使用timedelta
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46:one_day: {0!s} yesterday: {1!s}".format(one_day,yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

#計算兩個日期相差幾天
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))
    
#用strftime建立特定格式的字串
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

#建立不同日期字串格式
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
print("Output #56: {!s}".format(datetime.date(datetime.strptime\
(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime\
(date4, '%B %d, %Y'))))
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
#讀
with open(input_file,'r',newline='') as filereader:
    #寫
    with open(output_file,'w',newline='') as filewriter:
        header = filereader.readline()  #讀取輸入檔的第一行
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
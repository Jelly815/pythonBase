# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import csv
import sys
import re

input_file = sys.argv[1]
output_file = sys.argv[2]
pattern = re.compile(r'(?P<my_pattern_group>^001-1.*)',re.I) #re.I:不區分大小寫

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        header = next(filereader)
        filewriter.writerow(header)
        
        for row_list in filereader:
          invoice_number = row_list[1]
          if pattern.search(invoice_number):
              filewriter.writerow(row_list)
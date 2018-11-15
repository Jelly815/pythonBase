# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file,sheet_name='january_2013')
writer =  pd.ExcelWriter(output_file)
data_frame.to_excel(writer,sheet_name='jan_13_output',index=False)
writer.save()
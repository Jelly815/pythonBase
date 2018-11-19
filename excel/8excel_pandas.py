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

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_name = data_frame.iloc[:,['Customer ID','Purchase Date']]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
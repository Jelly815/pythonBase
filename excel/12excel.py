# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import glob
import os
import sys
from xlrd import open_workbook

input_directory = sys.argv[1]
workbook_counter = 0

for input_file in glob.glob(os.path.join(input_directory,'sales_*.xls*')):
    workbook = open_workbook(input_file)
    print('Workbook:%s' % os.path.basename(input_file))
    print('Number of worksheet: %d' % workbook.nsheets)
    
    for worksheet in workbook.sheets():
        print('Worksheet name:',worksheet.name,'t\Rows:',worksheet.nrows,'\tColumns:',worksheet.ncols)
    workbook_counter += 1
print('Number of Excel workbooks: %d' % (workbook_counter))
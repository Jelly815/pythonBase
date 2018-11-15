# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:57:25 2018

@author: Jelly
"""

#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index,col_index) == 3:  #3:代表該資料格含有日期
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index,col_index),workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index,col_index,date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index,col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index,col_index,non_date_cell)

output_workbook.save(output_file)
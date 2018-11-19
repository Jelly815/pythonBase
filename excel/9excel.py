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
output_worksheet = output_workbook.add_sheet('filtered_row_all_worksheets')
sales_column_index = 3
threshold = 2000.0
first_worksheet=True

with open_workbook(input_file) as workbook:
    data = []
    
    for worksheet in workbook.sheets():
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False
    
    for row_index in range(1,worksheet.nrows):
        row_list = []
        sale_amount = worksheet.cell_value(row_index,sales_column_index)
        
        if sale_amount > threshold:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index,column_index)
                
                cell_type = worksheet.cell_type(row_index,column_index)
                
                if cell_type == 3:  #3:代表含有日期
                    date_cell =xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        
        data.append(row_list)
    
    for list_index,output_list in enumerate(data):
        for element_index,element in enumerate(output_list):
            output_worksheet.write(list_index,element_index,element)
output_workbook.save(output_file)
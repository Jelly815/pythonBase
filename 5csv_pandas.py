#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file,error_bad_lines=False)

data_frame_value = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_value.to_csv(output_file, index=False)
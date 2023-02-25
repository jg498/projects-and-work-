#make a parsing script for excel files by size using panda
#this script will parse a directory of excel files and output a csv file with the file name, size, and date modified
#this script will also output a csv file with the file name, size, and date modified for files larger than 1MB

import os
import pandas as pd
import datetime
import csv

#set the directory to parse
directory = '/home/username/Desktop/parse'

#set the output file name
output_file = 'output.csv'

#set the output file name for files larger than 1MB
output_file_large = 'output_large.csv'

#set the size to filter by
size_filter = 1000000

#set the date to filter by
date_filter = datetime.datetime(2018, 1, 1)

#set the date format
date_format = '%Y-%m-%d %H:%M:%S'

#set the column names
column_names = ['File Name', 'Size', 'Date Modified']

#set the column names for files larger than 1MB
column_names_large = ['File Name', 'Size', 'Date Modified']

#set the output file path
output_file_path = os.path.join(directory, output_file)

#set the output file path for files larger than 1MB
output_file_path_large = os.path.join(directory, output_file_large)

#begin pandas dataframe
df = pd.DataFrame(columns=column_names)

#begin pandas dataframe for files larger than 1MB 
df_large = pd.DataFrame(columns=column_names_large)

#loop through the directory
for filename in os.listdir(directory):
    #set the file path
    file_path = os.path.join(directory, filename)
    #check if the file is a file
    if os.path.isfile(file_path):
        #get the file size
        file_size = os.path.getsize(file_path)
        #get the file modified date
        file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        #check if the file is larger than 1MB
        if file_size > size_filter:
            #check if the file was modified after 2018
            if file_modified > date_filter:
                #add the file to the dataframe
                df_large = df_large.append({'File Name': filename, 'Size': file_size, 'Date Modified': file_modified.strftime(date_format)}, ignore_index=True)

        #add the file to the dataframe
        df = df.append({'File Name': filename, 'Size': file_size, 'Date Modified': file_modified.strftime(date_format)}, ignore_index=True)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:10:51 2020

@author: ahmedomar
"""

import pandas as pd
pd.set_option('display.max_rows', None) ## by default dataframe results are truncated so this option display all data
pd.set_option('display.max_columns', None) ## same but for columns
df1 = pd.read_csv("/pat/to/.csv files", usecols=["column1", "column2", "column2"]) ## get csv from specific path and use only some columns
df1.column1 = df1.column1.astype(str).str.slice(0,15) ## take only first 16 numbers of all the values 
df1=df1[(df1.column2 == "value inside the column") & (df1.column3 == "value inside the column")] ## display specific values in columns 
df2=pd.read_csv("/path/to/.csv files", usecols=["column1", "column2"]) ## create dataframe 2 with another csv file and specific columns
df2=df2.astype(str) ## convert all dataframe to str type for easy comparison
df1=df1.astype(str)
df1
df3 = pd.merge(df1,df2,on="column2") ## pd.merge compare 2 columns from 2 different csv files and display all intersection values between them
df3=df3.to_csv("/path/to/output location with .csv") ## export the output of the comparision to new csv file

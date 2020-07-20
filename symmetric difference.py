#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:42:16 2020

@author: ahmedomar
"""

import pandas as pd

df=pd.read_csv("/path/to/1.csv")
df1=pd.read_csv("/path/to/2.csv")

df2=pd.merge(df, df1, on=["column1", "column2"], how='outer', indicator=True) ## compare between 2 different csv files
## on column1 and coulmn2 and print the symmetric difference between them or print values which are not intersected then indicate which of the values found in 
## coulmn1 or column2

df3=df2.to_csv("/path/to/output location.csv")

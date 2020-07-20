#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:42:16 2020

@author: ahmedomar
"""

import pandas as pd

df=pd.read_csv("/home/ahmedomar/Desktop/Kibana.csv")
df
df1=pd.read_csv("/home/ahmedomar/Desktop/EDR28.csv")
df1
del df
del df1


df3=pd.merge(df, df1, on=["msisdn", "darwinLoanId"])
df3
df.count()
df1.count()
df3.count()

df3=df3.astype(str)
df3
df4=df3.to_csv("/home/ahmedomar/Desktop/test.csv")

df5=pd.merge(df, df1, on=["msisdn", "darwinLoanId"], how='outer', indicator=True)
df5
df5=df5.astype(str)
df5
df5.count()

df6=df5.to_csv("/home/ahmedomar/Desktop/test2.csv")

df7=df5[~df5._merge.str.contains("both")]
df7
df8=df7.to_csv("/home/ahmedomar/Desktop/test4.csv")


clear

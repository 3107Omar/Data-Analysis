#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:10:51 2020

@author: ahmedomar
"""

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df1 = pd.read_csv("/home/ahmedomar/Desktop/19-3-2020/CVAS_EDR_ORDERS.csv", usecols=["IMEI", "orderStatus", "handsetBrand"])
df1.IMEI = df1.IMEI.astype(str).str.slice(0,15)
df1=df1[(df1.orderStatus == "DELIVERED") & (df1.handsetBrand == "Samsung")]
df2=pd.read_csv("/home/ahmedomar/Desktop/19-3-2020/kg_devices (3).csv", usecols=["IMEI", "STATUS"])
df2=df2.astype(str)
df1=df1.astype(str)
df1
df3 = pd.merge(df1,df2,on="IMEI")
df3=df3.to_csv("/home/ahmedomar/Desktop/19-3-2020/result.csv")




x = 100
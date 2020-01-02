#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:59:33 2019

@author: fransalles
"""

#Entrada e Saída de Dados

import numpy as np
import pandas as pd

df = pd.read_csv('exemplo.csv',sep=',')
df

df = df+1
df

df.to_csv('exemplo2.csv',sep=';',decimal=',')

df = pd.read_excel('Exemplo_Excel.xlsx', sheetname='Sheet1')
df

df.to_excel('exemplo3.xlsx', sheet_name='Sheet1')


df = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

df[0]
df[0]['Bank Name'] #lista com nomes dos bancos
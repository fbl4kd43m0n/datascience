#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:34:34 2019

@author: fransalles
"""

#Operações

import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc',
                   'def','ghi','xyz']})
df.head()

#Verificando os valores únicos
df['col2'].unique()

import numpy as np
np.unique(df['col2'])

len(df['col2'].unique())

df['col2'].nunique() #quantidade de elementos únicos

df['col2'].value_counts()

df[df['col1']>2]
df[(df['col1']>2) & (df['col2']==444)]

def vezes2(x):
    return x*2


df.sum()
df['col1'].sum()
df['col1'].apply(vezes2)

df['col3'].apply(len)
df['col1'].apply(lambda x: x*x)

#apagando colunas
del df['col2']
df

df.columns

df.index

df.sort_values(by='col2')

df

df.sort_values(by='col2', inplace=True)

#Verificando se há valores nulos
df.isnull()

#Apagando valores nan
df.dropna()

df = pd.DataFrame({'col1':[1,2,3,np.nan],'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
    
df.head()
df['col1'].fillna(value=df['col1'].mean())
df


#Pivot Table (trabalha como tabela dinamica no excel)
data = {'A':['foo','foo','foo','bar','bar','bar'],'B':['one','one',
        'two','two','one','one'], 'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df

df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
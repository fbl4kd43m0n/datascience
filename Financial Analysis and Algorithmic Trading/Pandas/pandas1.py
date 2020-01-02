#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:19:22 2019

@author: fransalles
"""

#Instalar: pip install pandas / conda install pandas
# Séries - DataFrames - Dados ausentes - GroupBy - Concatenar,
# juntar e mesclar - Operações - Entrada e saída de dados

# Começando com Séries
# Objeto básico do pandas, tem dois basicamente DataFrames e Séries

import numpy as np
import pandas as pd

labels = ['a','b','c']
minha_lista=[10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':30}

#Transformando em Series
pd.Series(data=minha_lista, index=labels)
series = pd.Series(data=minha_lista, index=labels)
series['b']
pd.Series(minha_lista,labels)
pd.Series(arr,labels)
pd.Series([sum,print,len])

#Fazendo operações
ser1 = pd.Series([1,2,3,4], index=['USA','Alemanha','URSS','Japão'])
ser1
ser2 = pd.Series([1,2,3,4], index=['USA','Alemanha','Itália','Japão'])
ser2
ser1 + ser2

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(), 
                  columns='W X Y Z'.split())

df['W']
type(df['W']) #Series
type(df) #DataFrame
df[['W', 'Z']]
df.W #Não é aconselhavel utilizar essa forma
df['new'] = df['W'] + df['X']
df
df.drop('new', axis=1)
df
df.drop('new', axis=1, inplace=True)
df

#Baseado no nome das colunas
df.loc['A','W']
df.loc['A']
df.loc[['A','B'],['X','Y','Z']]


#iloc - utilizando notação de numpy
df.iloc[1:4,2:]

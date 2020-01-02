#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:21:07 2019

@author: fransalles
"""

import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), index='A B C D E'.split(),columns='W X Y Z'.
                  split())

df

#resultados maiores que zero
df > 0
bol = df > 0
df[bol]
df[df['W']>0]
df[df['W']>0]['Y']
bol = df['W']>0
df2 = df[bol]
df2['Y']
df[(df['W']>0) and (df['Y']>1)] #vai gerar erro
df[(df['W']>0) & (df['Y']>1)]


#resetar o index
df.reset_index()
df.reset_index(inplace=True)
df
col = 'RS RJ SP AM SC'.split()
col
df['Estado'] = col
df
df.set_index('Estado')
df

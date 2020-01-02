#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:40:59 2019

@author: fransalles
"""

import numpy as np
import pandas as pd

d={'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}

d

df = pd.DataFrame(d)
df

df.dropna() #exclui valores ausentes (nan)
df.dropna(thresh=2)

df.fillna(value='Fill na') #substitui os valores ausentes por algo
df['A'].fillna(value=df['A'].mean())
df
df.fillna(method='ffill')


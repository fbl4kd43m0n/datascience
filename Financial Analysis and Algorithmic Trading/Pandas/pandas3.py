#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:32:03 2019

@author: fransalles
"""

import numpy as np
import pandas as pd

#Níveis de ïndice
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

outside
inside

hier_index

df = pd.DataFrame(np.random.randn(6,2),index=hier_index, columns=['A','B'])
df

df.loc['G1'].loc[1]
df.loc['G2']

df.index.names = ['Grupo','Numero']
df
df.xs('G1')
df.xs(1,level='Numero')


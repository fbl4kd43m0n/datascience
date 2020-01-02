#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:47:18 2019

@author: fransalles
"""

#GroupBy

import pandas as pd

#criando um dataframe
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Nome':['Franciny',
        'Patty','Andres','Flavio','Jesus','Verinha'],'Venda':[200,120,340,124,
                                                   243,450]}

df = pd.DataFrame(data)

df

group = df.groupby('Empresa')
group

#Soma das vendas por empresa
group.sum()

#Média de vendas por empresa
group.mean()

#Info estatisitca
group.describe()

#contanto elementos
group.count()

group = df.groupby('Nome')

#total de vendas por vendendor
group.sum().loc['Franciny']
group.sum().loc['Patty']



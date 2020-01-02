#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:57:27 2019

@author: fransalles
"""

#Junçao de dataframes: conctenar, juntar e mesclar

import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']},
                           index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                           'B': ['B4', 'B5', 'B6', 'B7'],
                           'C': ['C4', 'C5', 'C6', 'C7'],
                           'D': ['D4', 'D5', 'D6', 'D7']},
                            index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                           'B': ['B8', 'B9', 'B10', 'B11'],
                           'C': ['C8', 'C9', 'C10', 'C11'],
                          'D': ['D8', 'D9', 'D10', 'D11']},
                           index=[8, 9, 10, 11])

df1
df2
df3

#concatenando
pd.concat([df1,df2,df3])
pd.concat([df1,df2,df3],axis=1)

#Mesclando
esquerda = pd.DataFrame({'key2': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})
   
direita = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                             'D': ['D0', 'D1', 'D2', 'D3']}) 

esquerda
direita

pd.merge(esquerda,direita,how='inner',on='key')

pd.merge(esquerda,direita,on=['key1', 'key2'])

pd.merge(esquerda,direita,how='outer', on=['key1','key2'])



#Juntar
esquerda = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                          index=['K0', 'K1', 'K2'])

direita = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                        'D': ['D0', 'D2', 'D3']},
                          index=['K0', 'K2', 'K3'])

esquerda.join(direita)
esquerda.join(direita, how='outer')
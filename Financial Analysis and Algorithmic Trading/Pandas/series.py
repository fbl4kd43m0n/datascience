#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:00:43 2019

@author: fransalles
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

'''
Series
Uma Series é como um array unidimensional, uma lista de valores. 
Toda Series possui um índice, o index, que dá rótulos a cada elemento da lista. 
Abaixo criamos uma Series notas, o index desta Series é a coluna à esquerda, 
que vai de 0 a 4 neste caso, que o pandas criou automaticamente, já que não 
especificamos uma lista de rótulos.


Dicionário 
É um tipo diferente de coleção. Ele é um tipo de mapeamento nativo do Python. 
Um mapa é uma coleção associativa desordenada. A associação, ou mapeamento, 
é feita a partir de uma chave, que pode ser qualquer tipo imutável, para um 
valor, que pode ser qualquer objeto de dados do Python.
Não importa em que ordem escrevemos os pares. Os valores em um dicionário são 
acessados com chaves, não com índices, por isso não há necessidade de se 
preocupar com a ordenação.
Vamos definir um dicionário como sendo um tipo abstrato de dados que associa 
uma chave a um valor. A chave precisa ser única, ou seja, não pode haver 
chaves repetidas e também deve ser imutável, ou seja, uma vez criada, 
ela permanece a mesma.
Em algumas situações, ao invés de utilizar um número inteiro como índice, 
desejamos utilizar alguma informação, como por exemplo, o nome de um objeto.



'''

notas = pd.Series([2,7,5,10,6])
notas
notas.values
notas.index

notas2 = pd.Series([2,7,5,10,6], index=["Wilfred", "Abbie", "Harry", "Julia", 
                   "Carrie"])
notas2
notas2.values
notas2.index

'''
O index nos ajuda para referenciar um determinado valor, ele nos permite 
acessar os valores pelo seu rótulo:
'''
notas2['Julia'] # Resultado: 10

'''
Outra facilidade proporcionada pela estrutura são seus métodos que fornecem 
informações estatísticas sobre os valores, como média .mean() e 
desvio padrão .std(). 
'''
print("Informações estatísticas de notas")
print("---------------------------------")
print("Média.........: ", notas.mean())
print("Desvio padrão.: ", notas.std())

print("Informações estatísticas de notas2")
print("---------------------------------")
print("Média.........: ", notas2.mean())
print("Desvio padrão.: ", notas2.std())

notas.describe()
notas2.describe()


'''
A estrutura é flexível o suficiente pra aplicarmos algumas expressões 
matemáticas e funções matemáticas do numpy diretamente:
'''

notas ** 2
notas2 ** 3


'''
DataFrame
Já um DataFrame é uma estrutura bidimensional de dados, como uma planilha. 
Abaixo criaremos um DataFrame que possui valores de diferentes tipos, 
usando um dicionário como entrada dos dados:
'''
df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas': [3,4,2,1,4],
                   'Prova': [2,7,5,10,6],
                   'Seminario': [8.5,7.5,9.0,7.5,8.0]})
df.dtypes
df.columns
df['Seminario']
df.describe()


'''
Outra tarefa comum aplicada em DataFrames é ordená-los por determinada coluna:
'''
df.sort_values(by="Seminario")


'''
Muitas vezes é necessário selecionarmos valores específicos de um DataFrame, 
seja uma linha ou uma célula específica, e isso pode ser feito de diversas 
formas. A documentação oficial contém vasta informação para esse tipo de tarefa, 
aqui nos concentraremos nas formas mais comuns de selecionarmos dados.
Para selecionar pelo index ou rótulo usamos o atributo .loc:
'''
df.loc[3]
df.loc[1]

'''
Para selecionar de acordo com critérios condicionais, se usa o que se chama 
de Boolean Indexing.
Suponha que queiramos selecionar apenas as linhas em que o valor da coluna 
Seminário seja acima de 8.0, podemos realizar esta tarefa passando a condição 
diretamente como índice:
'''
df[df["Seminario"]>8.0]


'''
Este tipo de indexação também possibilita checar condições de múltiplas 
colunas. Diferentemente do que estamos habituados em Python, aqui se usam 
operadores bitwise, ou seja, &, |, ~ ao invés de and, or, not, respectivamente. 
Suponha que além de df["Seminário"] > 8.0 queiramos que o valor da coluna 
Prova não seja menor que 3:
'''
df[(df["Seminario"]>8.0) & (df["Prova"]>3)]






labels = ['a', 'b', 'c']
minha_lista = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':30}
pd.Series(data=minha_lista, index=labels)
series = pd.Series(data=minha_lista, index=labels)


lista_fran = [666, 333, 777, 999]
labels_fran = ['diabo', 'deus', 'biblia', 'fudencio']
series2 = pd.Series(data=lista_fran, index=labels_fran)
series2['diabo']

series + series2

df2 = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

df2.head() # Visualizando os 5 primeiros dados do dataframe
df2.tail() # Visualizando as últimos 5 linhas do dataframe

# Listando os valores únicos numa coluna
df2['bairro'].unique()

# Verificando a hegemoneidade da amostra
df2['bairro'].value_counts() 

# Os valores contados também podem ser normalizados para expressar porcentagens
df2['bairro'].value_counts(normalize=True)
df2['bairro'].value_counts(normalize=True) * 100


'''
Agrupar os dados se baseando em certos critérios é outro processo que o pandas 
facilita bastante com o .groupby(). Esse método pode ser usado para resolver 
os mais amplos dos problemas, aqui abordarei apenas o agrupamento simples, 
a divisão de um DataFrame em grupos.
Abaixo agrupamos o nosso DataFrame pelos valores da coluna "bairro", e em 
seguida aplicamos o .mean() para termos um objeto GroupBy com informação 
das médias agrupadas pelos valores da coluna bairros.
'''
df2.groupby('bairro').mean()


'''
Para extrairmos dados de uma coluna deste objeto basta acessá-lo 
convencionalmente, para obtermos os valores da média do preço do metro 
quadrado em ordem crescente, por exemplo:
'''
df2.groupby('bairro').mean()['pm2'].sort_values()



'''
É comum queremos aplicar uma função qualquer aos dados, ou à parte deles, 
neste caso o pandas fornece o método .apply. Por exemplo, para deixar os 
nomes dos bairros como apenas as suas três primeiras letras:
'''
def truncar(bairro):
    return bairro[:3]

df2['bairro'].apply(truncar)

# Usando uma função lambda
df2['bairro'].apply(lambda x: x[:3])


'''
Uma das tarefas na qual o pandas é reconhecidamente poderoso é a habilidade de 
tratar dados incompletos. Por muitos motivos pode haver incompletude no 
dataset, o np.nan é um valor especial definido no Numpy, sigla para 
Not a Number, o pandas preenche células sem valores em um DataFrame lido 
com np.nan.
Vamos criar um novo dataframe usando as 5 primeiras linhas do nosso original, 
usando o já visto .head(). Abaixo é usado o .replace para substituir um valor 
específico por um NaN.
'''
df3 = df2.head()
df3 = df2.replace({'pm2': {12031.25: np.nan}})
df3


'''
O pandas simplifica a remoção de quaiquer linhas ou colunas que possuem um 
np.nan, por padrão o .dropna() retorna as linhas que não contém um NaN:
'''
df3.dropna()
print(df3.fillna(99)) # Preenchendo todos os valores NaN por um outro valor



'''
Acaba sendo muitas vezes conveniente termos um método que indica quais valores 
de um dataframe são NaN e quais não são:
'''
df3.isna()



'''
Visualização de Dados
Partiremos agora para visualização de dados com o pandas. Os métodos de 
visualização do pandas são construídos com base no matplotlib para exploração 
rápida dos dados. Para se ter mais liberdade no conteúdo e possibilidades de 
visualização se recomenda usar diretamente o matplotlib ou ainda, para 
visualização estatística, o seaborn. Nesta introdução tratarei apenas dos 
métodos de visualização incluídos no pandas, que por outro lado, oferece uma 
sintaxe bastante simples para realizar a tarefa.
Comecemos verificando que tanto Series como DataFrame possuem um método .plot() 
que também é um atributo e pode ser encadeado para gerar visualização de 
diversos tipos, como histograma, área, pizza e dispersão, com respectivamente 
.hist(), .area(), .pie() e .scatter(), além de vários outros.
Vamos verificar a distribuição dos preços usando o encadeamento .plot.hist(), 
o eixo x, que é o preço, está numa escala de *10^7, como mostrado na imagem:
'''
df3["preco"].plot.hist()


'''
Por padrão esse método usa 10 bins, ou seja, divide os dados em 10 partes, 
mas é claro que podemos especificar um valor para a plotagem. Abaixo, além de 
especificar a quantidade de bins, também especifiquei a cor das bordas como 
preta, que por padrão é transparente.
'''
df3['preco'].plot.hist(bins=30, edgecolor='black')


'''
Podemos usar os valores de contagem de cada bairro como exemplo de dado para 
um plot tanto de barras verticais quando de barras horizontais, para verificar 
visualmente esses dados:
'''
df3['bairro'].value_counts().plot.bar()
df3['bairro'].value_counts().plot.barh()


'''
Os métodos são flexíveis o suficiente para aceitarem argumentos como um título 
para a imagem:
'''
df3['bairro'].value_counts().plot.barh(title="Número de apartamentos")



'''
Um gráfico de dispersão usando um DataFrame pode ser usado especificando-se 
quais colunas usar como dados no eixo x e y:
'''
df3.plot.scatter(x='preco', y='area')


'''
Para fins estéticos, o matplotlib fornece uma série de styles diferentes que 
podem ser usados, um deles é o ggplot
'''
plt.style.use('ggplot')


# Agora este estilo será usado em todas as imagens geradas após essa linha
df3.plot.scatter(x='pm2', y='area')
df3.plot.scatter(x='preco', y='area')


# Lista de estilos
plt.style.available


'''
A coluna de quartos diz quantos quartos tem um determinado apartamento, também 
se pode ver a contagem e distribuição usando outros métodos de plotagem 
oferecidos pelo pandas:
'''
df3['quartos'].value_counts().plot.pie()


'''
Uma coisa a se notar do gráfico de scatter é a poluição causada pela enorme 
quantidade de dados agrupadas num dos cantos do gráfico, além de podermos 
diminuir o tamanho dos pontos passando o argumento s ao método .scatter podemos 
também usar um método do pandas que cria uma amostragem aleatória dos dados.
O .sample pode receber tanto um argumento frac, que determina uma fração dos 
itens que o método retornará (no caso abaixo, 10%), ou n, que determina um 
valor absoluto de itens.
'''
df3.plot.scatter(x='preco',y='area',s=.5)
df3.sample(frac=.1).plot.scatter(x='preco',y='area')





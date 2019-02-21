#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:37:51 2019

@author: Franciny Salles
"""

# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('train.csv')

def missing_data(data):
    total = data.isnull().sum()
    percent = (data.isnull().sum()/data.isnull().count()*100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    return(np.transpose(tt))

missing_data(dataset)

%matplotlib inline
import seaborn
seaborn.set() 

#-------------------- Sobreviveu / Morreu por Classe --------------------
sobreviventes = dataset[dataset['Survived']==1]['Pclass'].value_counts()
#Pclass é o ticket vendido por classe: 1, 2, 3
mortos = dataset[dataset['Survived']==0]['Pclass'].value_counts()
classes = pd.DataFrame([sobreviventes, mortos])
classes.index = ['Sobreviventes', 'Mortos']
classes.plot(kind='bar', stacked=True, figsize=(5,3), title="Sobrevientes e Mortos por Classe")

classe1_sobreviventes = classes.iloc[0,0] / classes.iloc[:,0].sum()*100
classe2_sobreviventes = classes.iloc[0,1] / classes.iloc[:,1].sum()*100
classe3_sobreviventes = classes.iloc[0,2] / classes.iloc[:,2].sum()*100
print("Porcentagem da Primeira Classe que sobreviveram.: ", 
      round(classe1_sobreviventes), "%")
print("Porcentagem da Segunda Classe que sobreviveram..: ", 
      round(classe2_sobreviventes), "%")
print("Porcentagem da Terceira Classe que sobreviveram.: ", 
      round(classe3_sobreviventes), "%")

from IPython.display import display
display(classes)


#-------------------- Sobreviveu / Morreu por Sexo --------------------
sobreviventes_sexo = dataset[dataset.Survived == 1]['Sex'].value_counts()
mortos_sexo = dataset[dataset.Survived == 0]['Sex'].value_counts()
classes_sexo = pd.DataFrame([sobreviventes_sexo, mortos_sexo])
classes_sexo.index = ['Sobreviventes', 'Mortos']
classes_sexo.plot(kind='bar', stacked=True, figsize=(5,3), title="Sobreviventes / Mortos - por Sexo")

mulheres_sobreviventes = classes_sexo.female[0]/classes_sexo.female.sum()*100
homens_sobreviventes = classes_sexo.male[0]/classes_sexo.male.sum()*100
print("Porcentagem de mulheres sobreviventes: ", round(mulheres_sobreviventes), "%")
print("Porcentagem de homens sobreviventes: ", round(homens_sobreviventes), "%")

from IPython.display import display
display(classes_sexo)

'''
O pré-processamento dos dados é uma parte crucial. Se apenas dermos o conjunto 
de dados sem limpá-lo, provavelmente os resultados não serão bons! Assim, 
nesta etapa, iremos pré-processar o conjunto de dados de treinamento e isso 
envolverá seleção de recursos, limpeza de dados e engenharia de recursos.

Vou começar com a seleção de recursos. Como vimos anteriormente, "P-Class", 
"Sex", "Age" e "Embarked" mostraram alguma relação com a taxa de Survived. 
Assim, descartarei os recursos restantes, exceto "Nome", porque ele será 
útil em uma etapa adicional do processo de limpeza.

'''

X = dataset.drop(['PassengerId', 'Cabin', 'Ticket', 'Fare', 'Parch', 'SibSp'], 
                  axis=1)
y = X.Survived
X = X.drop(['Survived'], axis=1)
X.head(20)

'''
Podemos ver, a partir desse DataFrame exibido, que "Sex" e "Embarked" são 
recursos categóricos e possuem strings em vez de valores numéricos. 
Precisamos codificar essas strings em dados numéricos, para que o algoritmo 
possa realizar seus cálculos.

Para o recurso "Sex", podemos usar a classe LabelEncoder da biblioteca sklearn.
preprocessing.

Outra maneira de fazer isso é usando os get_dummies dos pandas. Nós estaremos 
usando isso para codificar o recurso "Embarcado". Mas primeiro, como 
"Embarcado" tem dois valores NaN, precisamos cuidar desses valores ausentes. 
Nesta abordagem, fornecerei a categoria 'S' porque é a mais frequente nos 
dados. Depois disso, é possível usar os get_dummies e obter três novas colunas 
(Embarked_C, Embarked_Q, Embarked_S) que são chamadas de variáveis ​​dummy (
elas atribuem "0" e "1" para indicar associação em uma categoria). O anterior 
"Embarcado" pode ser removido do X, já que ele não será mais necessário e 
agora podemos concatenar o dataframe X com o novo "Embarcado", que possui as 
três variáveis ​​fictícias. Finalmente, como o número de variáveis ​​fictícias 
necessárias para representar um único recurso é igual ao número de categorias 
nesse recurso menos um, podemos remover um dos dummies criados, digamos 
Embarked_S, por exemplo. Isso não removerá nenhuma informação porque, 
tendo os valores de Embarked_C e Embarked_Q, o algoritmo pode entender 
facilmente os valores da variável dummy remanescente (quando Embarked_C e 
Embarked_Q são '0' Embarked_S será '1', caso contrário, será '0' ).
'''


# ----------------- Encoding dados categóricos -------------------------
# Encoding "Sex"
from sklearn.preprocessing import LabelEncoder
labelEncoder_X = LabelEncoder()
X.Sex=labelEncoder_X.fit_transform(X.Sex)

# Encoding "Embarked"
print ('Quantidade de valores nulos em Embarked: ', sum(X.Embarked.isnull()))
row_index = X.Embarked.isnull()
X.loc[row_index, 'Embarked']='S'
Embarked = pd.get_dummies(X.Embarked, prefix='Embarked')
X = X.drop(['Embarked'], axis=1)
X = pd.concat([X, Embarked], axis=1)
X = X.drop(['Embarked_S'], axis=1)
X.head()

'''
Você pode se perguntar por que ainda estamos mantendo a coluna "Nome". 
Na verdade, o nome não parece ter influência, não importa se uma pessoa é 
chamada Owen ou William, no entanto, esta coluna tem o título localizado após 
o sobrenome e a vírgula ("Mr", "Mrs", "Miss", etc.) que pode ser útil.

Se dermos uma olhada na tabela X exibida anteriormente, poderemos ver muitos 
valores ausentes para a coluna "Idade". Remover essas linhas com valores 
ausentes envolveria remover 177 linhas (o que é bastante!) E teríamos menos 
informações para criar o modelo. Em alguns casos, é aceitável tomar a média 
da coluna e substituir os valores nulos, no entanto, neste caso, é possível 
estimar a idade da pessoa pelo título, presente na coluna "Nome".

Portanto, primeiro identificarei os diferentes títulos apresentados e, em 
seguida, classificarei a Idade para cada título. Podemos fornecer essa Idade 
média encontrada para cada título para as pessoas com valores de Idade 
ausentes, de acordo com o título em "Nome".

Depois de usar as informações em "Nome", podemos soltar esta coluna.

'''

#-------------- Dando um jeito na informação faltante  -----------------------
print('Número de valores nulos em Idade (Age): ', sum(X.Age.isnull()))

got=dataset.Name.str.split(',').str[1]
X.iloc[:,1]=pd.DataFrame(got).Name.str.split('\s+').str[1]

# Média da idade por título
ax = plt.subplot()
ax.set_ylabel('Média da idade')
X.groupby('Name').mean()['Age'].plot(kind='bar', figsize=(13,8), ax=ax)

title_mean_age=[]
title_mean_age.append(list(set(X.Name)))
title_mean_age.append(X.groupby('Name').Age.mean())
title_mean_age

# Preenchendo as idades faltantes
n_training = dataset.shape[0]
n_titles = len(title_mean_age[1])
for i in range(0, n_training):
    if np.isnan(X.Age[i])==True:
        for j in range(0, n_titles):
            if X.Name[i] == title_mean_age[0][j]:
                X.Age[i] = title_mean_age[1][j]

X=X.drop(['Name'], axis=1)


'''
Nós também podemos fazer a transformação de recursos. Por exemplo, poderíamos 
transformar o recurso "Idade" para simplificá-lo. Podemos distinguir os jovens 
(com menos de 18 anos) dos adultos.
'''

for i in range(0, n_training):
    if X.Age[i] > 18:
        X.Age[i]=0
    else:
        X.Age[i]=1
X.head()

'''
Agora, podemos dizer que temos um conjunto de dados bastante limpo para 
fornecer ao nosso algoritmo classificador.

Sempre teste diferentes classificadores
Tendo os dados pré-processados, podemos agora fornecer os dados para
diferentes classificadores e ver qual deles executa melhor na criação de um
modelo de classificação para esses dados.

Usaremos a validação cruzada, que é uma técnica de validação de modelo para
avaliar o quanto um modelo será generalizado para um conjunto de dados 
independente. O Python tem a classe cross_val_score da biblioteca
sklearn.model_selection para executar a validação cruzada.

'''

#----------------------- Regressão Logística ---------------------------------
# Fitando a Regressão Logística ao Training set
from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression(penalty='l2', random_state=0)

# Aplicando k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classificador, X=X, y=y, cv=10)
print("Regressão Logística:\ Accuracy:", accuracies.mean(), "+/-", 
      accuracies.std(), "\n")

#---------------------------------- K-NN --------------------------------------
# Fitando K-NN ao Training set
from sklearn.neighbors import KNeighborsClassifier
classificador = KNeighborsClassifier(n_neighbors = 9, metric = 'minkowski', p=2)

# Aplicando k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classificador, X=X, y=y, cv=10)
print("K-NN:\n Accuracy:", accuracies.mean(), "+/-", accuracies.std(), "\n")


#---------------------------------- SVM ---------------------------------------
# Fitando Kernel SVM ao Training set
from sklearn.svm import SVC
classificador = SVC(kernel = 'rbf', random_state=0)

# Aplicando k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classificador, X=X, y=y, cv=10)
print("SVM:\n Accuracy: ", accuracies.mean(), "+/-", accuracies.std(), "\n")


#------------------------------- Naive Bayes ----------------------------------
# Fitando Naive Bayes ao Training set
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()

# Aplicando k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classificador, X=X, y=y, cv=10)
print("Naive Bayes:\n Accuracy: ", accuracies.mean(), "+/-", accuracies.std(), "\n")


#------------------------------ Random Forest----------------------------------
# Fitando Random Forest Classification ao Training set
from sklearn.ensemble import RandomForestClassifier
classificador = RandomForestClassifier(n_estimators = 100, criterion='entropy', random_state=0)

# Aplicando k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classificador, X=X, y=y, cv=10)
print("Random Forest:\n Accuracy: ", accuracies.mean(), "+/-", accuracies.std())


'''
Como podemos ver, de todos os 5 classificadores testados neste tutorial, 
a Random Forest obteve melhores resultados.

Depois de alterar o conjunto de testes executando as mesmas transformações 
feitas no conjunto de treinamento, podemos usar o modelo Random Forest criado 
e fazer as previsões. 
'''

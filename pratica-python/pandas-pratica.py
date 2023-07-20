# Específico para tratar dados tabulares (Linhas/Colunas)/(Planilha)
# Pode-se ter diferentes colunas com tipos diferentes de dados
import pandas as pd
import numpy as np

# Carrega arquivo para dataframe Pandas
dados = pd.read_csv("pratica-python\Credit.csv")
# Formato
dados.shape

# Resumo estatístico de colunas numéricas
dados.describe()

# Primeiros registros
dados.head()
# Últimos registros, com parâmetros
dados.tail(2)

# Filtrar por nome da coluna
dados[["duration"]]
# Filtrar linhas por índice
dados.loc[1:3]

# Linhas 1 e 3
dados.loc[[1, 3]]

# Filtro
dados.loc[dados['purpose'] == "radio/tv"]

# Outra condição
dados.loc[dados['credit_amount'] > 18000]

# Atribuimos resultado a variável, criando outro df (dataframe)
credito2 = dados.loc[dados['credit_amount'] > 18000]
print(credito2)

# Definimos apenas algumas colunas
credito3 = dados[['checking_status', 'duration']].loc[dados['credit_amount'] > 18000]
print(credito3)

# Séries, única coluna
# Pode ser criada a partir de listas, array do numpy ou coluna de dataframe
s1 = pd.Series([2,5,3,34,54,23,1,16])
print(s1)

# Serie a partir de um array do numpy
array1 = np.array([2,5,3,34,54,23,1,16])
s2 = pd.Series(array1)
print(s2)

# Serie a partir de um dataframe
s3 = dados['purpose']
print(s3)
type(s3)

# Note a diferença, temos um dataframe
d4 = dados[['purpose']]
type(d4)

# Renomear
dados.rename(columns={"duration": "duracao", "purpose": "proposito"})

# Porém, a alteração não é persistida
dados.head(1)

# Para persistir
dados.rename(columns={"duration": "duracao", "purpose": "proposito"}, inplace=True)
dados.head(1)

# Excluir coluna
dados.drop('checking_status', axis=1, inplace=True)
print(dados)

dados.head(1)

# Verificar dados nulos
dados.isnull()
# Verificar dados nulos
dados.isnull().sum()
# Retirar colunas com NaN (Not a Number)
dados.dropna()

# Preencher dados faltantes
dados['duracao'].fillna(0, inplace=True)

#iloc
dados.iloc[0:3, 0:5]
dados.iloc[[0,1,2,3,7], 0:5]

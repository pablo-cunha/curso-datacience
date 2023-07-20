import numpy as np

# Criando uma matriz unidimensional usando numpy, exibindo-a e imprimindo seu tipo
mt = np.array([12, 34, 26, 18, 10])
print(mt)
print(type(mt))

# Criando um array com um tipo específico
# Cria o array como float de 64 bits
mtfloat = np.array([1, 2, 3], dtype = np.float64)
print(mtfloat)
print(type(mtfloat))
mtint = np.array([1, 2, 3], dtype = np.int32)
print(mtint)
print(type(mtint))

# Fazendo a conversão de tipos com os arrays
mtnew = np.array([1.5, 3.9, 77.7, -5.6, 18.98])
print(mtnew)
# Quando transformamos de float para int os valores são truncados
mtnewint = mtnew.astype(np.int32)
print(mtnewint)

# Podemos fazer o inverso também
mt5 = np.array([1, 2, 3, 4])
print(mt5)
mt6 = mt5.astype(float)
print(mt6)

# Matrizes com mais de uma dimensão
# Bidimensional
mt7 = np.array([[7, 9, 11], [25, 8, 64], [2, 3, 6]])
print(mt7)

# Criando arrays vazios tipificados
# empty significa que não são inicializados, não que são vazios
vazio = np.empty([3, 2], dtype = int)
print(vazio)
print("-----")

# Criando uma matriz 4x3 com valores zero
zeros = np.zeros([4,3])
print(zeros)
print("-----")

# Com valores iguais a um
um = np.ones([2,2])
print(um)
print("-----")

# Cria matriz quadrada com diagonal peincipal com valores um e os outros valores zero (Matriz Identidade)
identidade = np.eye(3)
print(identidade)

# Valores aleatórios entre zero e um
random = np.random.random((5))
print(random)
print("-----")
# Valores aleatórios distr. normal contendo negativos
random2 = np.random.randn((5))
print(random2)
print("-----")
# Valores aleatórios numa matriz 3x4
random3 = (10*np.random.random((3,4)))
print(random3)
print("-----")

# Outra forma de gerar aleatórios é usando sementes
gnr = np.random.default_rng(1)
random4 = gnr.random(3)
print(random4)
print("-----")

# Gerando inteiros
random5 = gnr.integers(10, size=(3, 4))
print(random5)
print("-----")

# Função 'unique' remove repetições
j = np.array([11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 18, 19, 20])
j = np.unique(j)
print(j)
print("-----")

# Funções específicas
# Cria a matriz bidimensional k
k = np.array([[77, 99, 11], [8, 10, 5], [4, 3, 1]])

# Exibe a matriz k
print(k)
print("-----")
# Imprime um elemento específico da matriz
print(k[0][1])
# Imprime o tamanho das dimensões da matriz k
print(k.shape)

# Funções Matemáticas
# Mostra o maior valor da matriz k
print(k.max())
# Mostra o menor valor da matriz k
print(k.min())
# Mostra a soma dos valores de k
print(k.sum())
# Mostra a média dos valores de k
print(k.mean())
# Mostra o desvio padrão (standard deviation) dos valores da matriz k
print(k.std())

# Funções universais, aplicadas a todos os elementos
# Mostra o valor da raiz quadrada de todos os elementos
k1 = np.array([[10, 9, 16], [36, 45, 25], [72, 4, 1]])
print(np.sqrt(k1))
# Mostra o valor do exponencial de todos os elementos
print(np.exp(k1))

# Extração de elementos
m = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Mostra o elemento na segunda posição
print(m[1])
print("-----")
# Mostra o array dois elementos a partir da posição 0
print(m[0:2])
print("-----")
# Mostra o array a partir da antepenúltima posição até o final
print(m[-3:])

# Extração de linhas e colunas
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print("-----")
# Armazenando a primeira linha, todas as colunas
matrix_linha_1 = matrix[0, :]
print(matrix_linha_1)
print("-----")
# Segunda linha
matrix_linha_2 = matrix[1, :]
print(matrix_linha_2)
print("-----")
# Todas as linhas, primeira coluna
matrix_coluna_1 = matrix[:, 0]
print(matrix_coluna_1)
print("-----")
# Segunda coluna
matrix_coluna_2 = matrix[:, 1]
print(matrix_coluna_2)
print("-----")

# Adição e Multiplicação de matrizes
matriz1 = gnr.random(3)
matriz2 = gnr.random(1)
adicao = matriz1 + matriz2
print(adicao)
print("-----")
mult = matriz1 * matriz2
print(mult)
print("-----")
# Poderia também...
print(matriz1*matriz2)
print("-----")

# Transposição, rearranja um conjunto de 15 elementos de 0 a 14 em 3 linhas e 5 colunas
matriz3 = np.arange(15).reshape((3,5))
print(matriz3)
print("-----")
matriz4 = matriz3.T
print(matriz4)
print("-----")

# Expressões lógicas
# Usando where
# Criando matriz com valores aleatórios positivos e negativos
matriz5 = np.random.randn(4, 4)
print(matriz5)
print("-----")
# Criando matriz com valores booleanos baseado no array 'matriz5'
matriz6 = (matriz5 > 0)
print(matriz6)
print("-----")
# Criando matriz com valores -1 e 1 baseado nos valores do array 'matriz6'
matriz7 = np.where(matriz6 > 1, 1, -1)
print(matriz7)
print("-----")
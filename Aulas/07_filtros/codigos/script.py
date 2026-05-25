import pandas as pd


# Filtro simples — Boolean Indexing
df = pd.read_csv('funcionarios.csv')

# Numérico — maior que
df[df['idade'] > 25]

# Numérico — maior ou igual
df[df['salario'] >= 3000]

# Texto — igual a
df[df['cidade'] == 'Fortaleza']

# Texto — diferente de
df[df['cargo'] != 'Estagiario']


# Operadores lógicos — AND, OR e NOT

# AND (&) — ambas as condições devem ser verdadeiras
df[(df['idade'] > 25) & (df['cidade'] == 'Natal')]

# OR (|) — pelo menos uma condição deve ser verdadeira
df[(df['cidade'] == 'Fortaleza') | (df['cidade'] == 'Recife')]

# NOT (~) — inverte a condição
df[~(df['cidade'] == 'Fortaleza')]


# Múltiplas condições

# Duas condições AND
df[(df['idade'] > 25) & (df['cidade'] == 'Fortaleza')]

# Duas condições OR
df[(df['salario'] > 5000) | (df['cargo'] == 'Gerente')]

# Três condições AND
df[(df['idade'] >= 18) & (df['ativo'] == True) & (df['salario'] > 2000)]

# Salvando máscaras em variáveis antes de combinar
mask1 = df['idade'] > 25
mask2 = df['cidade'] == 'Fortaleza'
df[mask1 & mask2]


# Método .query() — sintaxe similar ao SQL

df.query('idade > 25 and cidade == "Fortaleza"')

# Usando variável externa com @
idade_min = 25
df.query('idade > @idade_min')


# Filtros de string (.str)

# Verifica se contém o texto
df[df['nome'].str.contains('Silva')]

# Verifica se começa com o texto
df[df['cidade'].str.startswith('For')]

# Verifica se o valor está em uma lista
cidades = ['Fortaleza', 'Recife']
df[df['cidade'].isin(cidades)]


# Parte prática — combinando todos os filtros

# Filtro simples
df[df['idade'] > 25]

# Múltiplas condições (AND)
df[(df['idade'] > 25) & (df['cidade'] == 'Fortaleza')]

# Usando .query()
df.query('idade > 25 and cidade == "Fortaleza"')

# Filtro de string
df[df['nome'].str.contains('Silva', case=False, na=False)]

# Filtro por lista
df[df['cidade'].isin(['Fortaleza', 'Recife', 'Natal'])]

# Encadeando dois .query()
df.query('idade > 18 and salario >= 2000').query('cidade != "Natal"')

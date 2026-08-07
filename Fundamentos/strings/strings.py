# Posicionamento de cada string.

# Imprimindo a pósição de cada letra 
posicao_letra = "PYTHON"

print(posicao_letra[0])
print(posicao_letra[1])
print(posicao_letra[2])
print(posicao_letra[3])
print(posicao_letra[4])
print(posicao_letra[5])

"""
Slicing (Fatiamento em Python)
Para extrair partes de uma string.

"""

# Obtendo uma parte de uma string usando slice
frase = "Olá, Me chamo Daniel"
parte = frase[2:3]
print(parte)

# Obtendo os primeiros 5 caracteres da string
primeiros = frase[:5]
print(primeiros)

# Obtendo os últimos 6 caracteres da string
ultimos = frase[-6:]
print(ultimos)


# Verificando se a palavra python está na frase
"""
O operador in é usado em Python para verificar a presença de um valor a presença de um valor 
dentro de uma sequencia (Como uma String,lista ou tupla).
Neste caso, esta sendo usado para verificar se determinada substring está contida em uma string maior

"""
print("Olá" in frase)
print("Olás" in frase)

# if - se

if "Olás" in frase:
        print("Sim tem a palavra Olá na frase")

# else - se não
else:
        print("Não tem")


"""
split()

O método split() divide uma string em várias partes.

O resultado sempre será uma lista.
"""

frase = "Python é uma linguagem incrível"

palavras = frase.split()

print(palavras)

# Saída:
# ['Python', 'é', 'uma', 'linguagem', 'incrível']


# Dividindo utilizando outro separador

nomes = "Daniel,Pedro,Maria"

lista = nomes.split(",")

print(lista)

# Saída:
# ['Daniel', 'Pedro', 'Maria']


"""
join()

O método join() faz o contrário do split().

Ele junta os elementos de uma lista em uma única string.
"""

nomes = ["Daniel", "Pedro", "Maria"]

resultado = " ".join(nomes)

print(resultado)

# Saída:
# Daniel Pedro Maria


resultado2 = ", ".join(nomes)

print(resultado2)

# Saída:
# Daniel, Pedro, Maria


"""
strip()

O método strip() remove os espaços do início e do final da string.
"""

nome = "      Daniel      "

print(nome)

print(nome.strip())

# Saída:
# Daniel

"""
lstrip()

Remove apenas os espaços do início da string.
"""

texto = "       Python"

print(texto.lstrip())

# Saída:
# Python

"""
rstrip()

Remove apenas os espaços do final da string.
"""

texto = "Python        "

print(texto.rstrip())

# Saída:
# Python


"""
Exemplo prático utilizando split() e strip()

Muito utilizado para tratar dados de arquivos CSV,
APIs e banco de dados.
"""

dados = "Daniel, 20, São Paulo"

lista = dados.split(",")

print(lista)

print(lista[0].strip())
print(lista[1].strip())
print(lista[2].strip())
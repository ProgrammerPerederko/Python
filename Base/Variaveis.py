
# Tipos de Variaveis

"""
Python é uma linguagem de tipagem dinâmica.

O tipo da variável é definido automaticamente de acordo
com o valor atribuído.

Boas práticas:
- Utilize nomes descritivos.
- Utilize sempre o padrão snake_case.
"""

# Sempre usar snake_case - declarar variaveis assim:

# numero_complexo
# dicionario
# idade
# nome_completo
# lista_de_clientes

# Mutavel - Siginifica que podemos alterar o conteudo do objeto depois que ele foi criado.
# Exemplos de variaveis:
# list
# dict
# set

# Imutavel - Significa que depois de declarada o conteudo do objeto, não pode ser alterado após sua criação.
# Exemplos de variaveis:
# str
# int
# float
# tuple
# bool
# complex

# String (str) - Sequencia de caracteres que ocupam um espaço na memoria.
string = "Daniel"
print(type(string))
# Inteiros (int) - Números inteiros, sem a parte decimal.
inteiro = 25

# Ponto Flutuante (Float) - Números Reais, que tem uma parte decimal
flutuante = 24.0

# Complexos (Complex) - Números complexos, que têm uma parte real e uma parte imaginaria
numeros_complexos = 2 + 4j

# Lista (list) - Uma coleção ordenada e mutavel.
lista = [ 1,2,3]

# Tuplas (Tuple): Uma coleção ordenada e imutavel.
tuplas = (1,2,3,4,5)

# Conjunto (set): Uma coleção não ordenada de itens unicos, Não permite elementos duplicados.
conjunto = {1,2,3}

# Dicionarios (dict): os dicionários preservam a ordem de inserção. Embora não sejam acessados por índice, mantêm a ordem em que as chaves foram adicionadas.
# Sendo definido por Pares chave-valor. 
dicionario = {"chave": "valor"}

# Booleanos (bool) - Valores Verdadeiros ou Falsos
boolean = True

# NoneType (None) - um tipo especial que representa a ausencia de valor.
nenhum = None

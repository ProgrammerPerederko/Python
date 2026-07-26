
# Tipos de Variaveis

"""
Python é uma linguagem de tipagem dinâmica.

O tipo da variável é definido automaticamente de acordo
com o valor atribuído.

Boas práticas:
- Utilize nomes descritivos.
- Utilize sempre o padrão snake_case.
- As variaveis sempre diferenciam maisculas de minusculas.
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


# Descobrindo tipos de variaveis no console:
# Exemplo:
print(type(boolean))
print(type(string))
print(type(inteiro))
print(type(dicionario))
print(type(lista))



print(f"Valor: {string} | Tipo: {type(string).__name__}")
print(f"Valor: {inteiro} | Tipo: {type(inteiro).__name__}")
print(f"Valor: {flutuante} | Tipo: {type(flutuante).__name__}")
print(f"Valor: {numeros_complexos} | Tipo: {type(numeros_complexos).__name__}")
print(f"Valor: {lista} | Tipo: {type(lista).__name__}")
print(f"Valor: {tuplas} | Tipo: {type(tuplas).__name__}")
print(f"Valor: {conjunto} | Tipo: {type(conjunto).__name__}")
print(f"Valor: {dicionario} | Tipo: {type(dicionario).__name__}")
print(f"Valor: {boolean} | Tipo: {type(boolean).__name__}")
print(f"Valor: {nenhum} | Tipo: {type(nenhum).__name__}")

# Podemos tambem atribuir varios valores de variaveis em uma só linha.
# Nesse caso é chamado de desacoplamento de tupla onde ele separa e coloca cada valor em uma operação diferente.
var1,var2,var3,var4 = 1,2,3,4

print(var1)
print(var2)
print(var3)
print(var4)

#Podemos tambem declarar o mesmo valor para varias variaveis em uma unica linha.
var1 = var2 = var3 = var4 = 1
print(var1)
print(var2)
print(var3)
print(var4)

# Se eu tiver uma coleção de valores em uma lista, podemos extrair em variaveis. Isso é chamado de descompactar.

exemplo = 1 , 2, 3, 4
var1, var2, var3, var4 = exemplo

print(var1)
print(var2)
print(var3)
print(var4)

# Para juntarmos variaveis em python usamos o caracter + ou ,

nome = "Ana paula"
# No caso de strings e tipos iguais podemos somar com o +
print("Seu nome é " +  nome)

idade = 10
# Não podemos tentar somar tipos diferentes, por que ele tenta somar tipos diferentes oq causa erro no computador.
 # print("Sua idade é " + idade)
# Por isso usamos a virgula para chamar o tipo diferente e evitar o erro
print("Sua idade é ",idade)

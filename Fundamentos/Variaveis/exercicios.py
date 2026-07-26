# Exercicios em Python para treinar variaveis:

# 1 Declare uma variavel chamada idade e atribua o valor 25 a ela
idade = 25

# 2 Declare uma variavel chamada nome e atribua o valor João a ela
nome = "João"

# 3 Declare uma variavel chamada saldo e atribua o valor 100.50 a ela.
saldo = 100.50

# 4 Crie uma Variavel chamada soma e atribua a ela a soma das variaveis  idade e saldo.
soma = idade + saldo

# 5 imprima na tela o valor de soma
print(soma)

#-----------------------------------------------------------------|

# 1 Crie uma Variavel chamada nota1 e atribua o valor 7.5 a ela
# 2 Crie uma Variavel chamada nota2 e atribua o valor 8.3 a ela
# 3 Crie uma Variavel chamada nota3 e atribua o valor 6.9 a ela
# 4 Calcule a media das tres notas e atribua o resultado  a uma variavel chamada media.
# 5 imprima o valor na tela formatado com duas casas decimais

nota1,nota2,nota3 = 7.5,8.3,6.9

media = (nota1 + nota2 + nota3) / 3

#() (parênteses) têm prioridade na execução.

#:.2f em uma f-string formata o número com duas casas decimais.

print(f"Média: {media:.2f}")
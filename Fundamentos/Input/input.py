"""
Solicita ao usuário que insira seu nome e duas notas,calcula a média dessas notas,em seguida, 
imprime uma mensagem contendo o nome do aluno e a média calculada.

O resultado final combina os valores das variaveis, nome e media com as strings
literais para criar a saida completa.

"""

# Treinando Input 

nome = input("Digite seu nome:")
print("Seu nome é",nome)

# Declaramos variaveis para armazenar os valores do input

nota1,nota2,nota3 = input("Digite sua Nota1"),input("Digite sua Nota2"),input("Digite sua Nota3")

print("Sua Nota1 é",nota1)
print("Sua Nota2 é",nota2)
print("Sua Nota3 é",nota3)


# Exercício: Tabuada Personalizada 

tabuada_exercicio = int(input("\nInsira o número da tabuada que quer ver: "))

for i in range(1, 11):
    print(f"{tabuada_exercicio} x {i} = {tabuada_exercicio * i}")


    nora = 1
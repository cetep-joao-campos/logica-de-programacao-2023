# Crie um programa que peça três notas e exiba a média.

nota_1: float = float(input("Unidade I: "))
nota_2: float = float(input("Unidade II: "))
nota_3: float = float(input("Unidade III: "))
soma: float = nota_1 + nota_2 + nota_3
media: float = soma/3

print(media)
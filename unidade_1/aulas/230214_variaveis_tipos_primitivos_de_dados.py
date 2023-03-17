"""
VARIÁVEIS E TIPOS DE DADOS PRIMITIVOS

Variáveis em programação é um local onde podemos armazenar valores que, como
o nome já diz, PODEM variar (não é regra que o valor irá mudar, mas se preci-
sar ele irá mudar).

VARIÁVEIS
Para criar uma variável é preciso dar um nome a ela, inserir um sinal de atri-
buição:

+---------------------------+
| nome da variável          |
|  |                        |
| nota = 3.5 <- informação  |
|      |                    |
| sinal de atribuição       |
+---------------------------+

TIPOS DE DADOS PRIMITIVOS

Para armazenar uma inforção em uma variável é preciso saber qual o tipo de 
dado em que essa informação se encaixa. Existem 4 tipos primitivos de dados:

- Inteiro: toda e qualquer informação numérica que pertença ao conjunto dos 
números inteiros relativos, negativa, nula ou positiva (1, 2, 10, 243, 0,
-23, -1, -17);

- Caracter ou string ou cadeia de caracteres: toda e qualquer informação
composta de um conjunto de caracteres alfanuméricos:
numéricos (0...9), alfabéticos (A...Z, a...z) e especiais (#, ?, !, @...);

- Real ou float ou ponto flutuante: toda e qualquer informação numérica que 
pertença ao conjunto dos números reais, negativa, nula ou positiva (-2.5,
-0.5, 0.0, 1.6, 6.4, 200.89)

- Booleano ou Lógico: toda e qualquer informação que pode assumir apenas duas
situações (biestável). Ex: Verdadeiro ou Falso, ligado ou desligado, 1 ou 0.
"""

# Observe o código abaixo:

nota: float = 6.4
print(nota)

# No código foi criado uma variável `nota` onde especificamos o tipo dela com 
# `: float` e atribuímos um valor de `6.4` utilizando o sinal de igual (`=`).
#
# A linguagem utilizada para esse código é chamada de Python. Python é uma lin-
# guagem de tipagem dinâmica, isso significa que não é obrigatório especificar 
# o tipo de dado que será armazenado na variável. Observe:

nota = 6.4
print(nota)

# O trecho de código foi modificado removendo a especificação do tipo de dado
# `: float`. O programa irá funcionar do mesmo jeito. Para facilitar o aprendi-
# zado, iremos utilizar a anotação de tipo do Python só para a finalidade de 
# melhor compreensão de como as informações são armazenadas nas variáveis e 
# para documentar o nosso código.
# 
# Veja mais algumas variáveis de outros tipos abaixo:

mensagem: str = "Olá, bom dia!"
nome: str = "Michael Jordan"
altura: float = 1.98
idade: int = 60
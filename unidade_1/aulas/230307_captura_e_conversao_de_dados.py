"""
CAPTURA DE DADOS PELO TECLADO

Um programa para ser realmente funcional é preciso que ofereça ao usuário a pos-
sibilidade dele inserir informações para serem processadas. Existe uma função em
Python que traz essa capacidade: `input()`.

A função `input()` captura uma informação e armazena em uma variável com o for-
mato de string. Caso preciso utilizar a informação captura como outro formato, 
será preciso utilizar uma função para convertê-la. Abaixo alguns exemplos:
"""

nome: str = input("Digite seu nome: ")
idade: int = input("Digite sua idade: ")

print(type(nome))
print(type(idade))

"""
CONVERSÃO DE TIPOS DE DADOS
Ao executar esse boco de código, teremos a seguinte saída:

Digite seu nome: Thiago
Digite sua idade: 28
<class 'str'>
<class 'str'>

O tipo de dado armazenado em `nome` está correto, pois nome é uma string (`str`),
mas idade não deveria ser uma string, mas sim um inteiro. Se não fizermos a con-
versão para inteiro, futuramente não vamos conseguir fazer operações matemáticas
com essa informação de idade, pois não é possível fazer operações matemáticas em
strings.

Para resolver esse problema, vamos utilizar uma função chamada de int():
"""

nome: str = input("Digite seu nome: ")
idade: int = int(input("Digite sua idade: "))

print(type(nome))
print(type(idade))

"""
Ao colocar a função `input()` dentro da função `int()` o valor capturado por
`input()` será convertido para inteiro e armazenado na variável idade.

Além da função `input()`, existe também a função `float()`, que converte pra um
número real e a função str, que converte para caractere (string).
"""
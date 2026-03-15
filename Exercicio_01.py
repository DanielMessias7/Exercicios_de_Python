# ==============================
# EXERCÍCIO 0
# ==============================

nome = input('Digite seu nome: \n')
idade = input('Digite sua idade: \n')

print(f'\n{nome}. Prazer, você {idade} anos de idade')


# ==============================
# EXERCÍCIO 1
# ==============================

# Peça para o usuário digitar o nome dele e depois exiba a mensagem:
# "Olá, [nome], seja bem-vindo ao Python!"

nome = input('Digite seu nome: ')
print(f'Olá, {nome}, seja bem-vindo ao Python!')


# ==============================
# EXERCÍCIO 2
# ==============================

# Peça para o usuário digitar dois números inteiros.
# Mostre a soma, subtração, multiplicação e divisão entre eles.

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

soma = numero1 + numero2
print(f'{numero1} + {numero2} é {soma}')

subtracao = numero1 - numero2
print(f'{numero1} - {numero2} é {subtracao}')

multiplicacao = numero1 * numero2
print(f'{numero1} * {numero2} é {multiplicacao}')

divisao = numero1 / numero2
print(f'{numero1} / {numero2} é {divisao:.2f}')


# ==============================
# EXERCÍCIO 4
# ==============================

# Peça para o usuário digitar um número.
# Verifique se o número é par ou ímpar e mostre o resultado.

n1 = int(input('Digite um numero: '))

if n1 % 2 == 0:
    print(f'{n1} é par')
else:
    print(f'{n1} é impar')


# ==============================
# EXERCÍCIO 5
# ==============================

# Peça para o usuário digitar um número.
# Mostre a tabuada desse número de 1 até 10.

n1 = int(input('Digite um numero: '))

print(f'{n1} * 1 = {n1 * 1}')
print(f'{n1} * 2 = {n1 * 2}')
print(f'{n1} * 3 = {n1 * 3}')
print(f'{n1} * 4 = {n1 * 4}')
print(f'{n1} * 5 = {n1 * 5}')
print(f'{n1} * 6 = {n1 * 6}')
print(f'{n1} * 7 = {n1 * 7}')
print(f'{n1} * 8 = {n1 * 8}')
print(f'{n1} * 9 = {n1 * 9}')
print(f'{n1} * 10 = {n1 * 10}')


# ==============================
# EXERCÍCIO 6
# ==============================

# Peça para o usuário digitar uma senha.
# Se a senha for igual a "1234", mostre "Acesso permitido".
# Caso contrário, mostre "Acesso negado".

senha = 1234
senha_digitada = int(input('Digite uma senha: '))

if senha_digitada == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')


# ==============================
# EXERCÍCIO 7
# ==============================

# Peça para o usuário digitar 3 números.
# Mostre qual é o maior número entre eles.

print('Solicito que digite 3 números!')

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} é maior')

elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2} é maior')

elif numero3 > numero1 and numero3 > numero2:
    print(f'{numero3} é maior')

else:
    print('Números repetidos, não é possível fazer a comparação')

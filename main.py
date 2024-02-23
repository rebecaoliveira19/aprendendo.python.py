Calcular a media de tres numeros
n1 = float(input('Qual número?   '))
n2 = float(input('Qual o número? '))
n3 = float(input('Qual e o número? '))
media = (n1 + n2 + n3)/2
print('A média foi de ',media)

# 4-Faça um Programa que peça as 4 notas bimestrais e mostre a média

n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
n3 = float(input('nota3: '))
n4 = float(input('nota4: '))
media = (n1 + n2 + n3 + n4)/4
print(f'A media foi de {media:.2f}')


# 5-Faça um Programa que converta metros para centímetros.

m = float(input('Metros:  '))
c = m *100
print(f'{m:.2f} metros para centímetros {c:.2f}')

# 6-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input('Qual e o raio? '))
calcular = 2*3.14*raio
area = 3.14*((raio)**2)
print(' Um círculo de raio',raio)
print('tem comprimento',calcular)
print('Tem a Area',area)

# 7-Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Qual e a area de um quadrado?   '))
area = lado ** 2

print(' O resultado que vc quer ve  {}  '.format(area))

# 9-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) /

f = float(input('What is the temperature? '))
c = (f - 32)* 5/9

print(f'The temperature is {c:.2f}')

# 10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input('What is the temperature? '))
F = (C *9)/ 5 + 32

print(f'The temperature is {F:.2f}')

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('Number:  '))
n2 = int(input('Number:  '))
n3 = float(input('Number:  '))

product = (2 * n1) * (n2 / 2)
plus = (3*n1) + n3
mare = n3 ** 3

print(product)
print(plus)
print(mare)


# 14-João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Qual e o peso?  '))

if peso > 50 :
    excesso = peso - 50
    multa = peso * 4
    print('Você ultrapassou o regulamento irá pagar a multa.')
else:
    print('O peso está de acordo com o regulamento.')

print(f'O excesso a quantidade de quilos foi {excesso:.2f}')

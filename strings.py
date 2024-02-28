# 1-Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.


print('Compara as duas strings!')

string1 = input('string 1:  ')
string2 = input('string 2:  ')

print(f'O tamanho de "{string1}:" ',len(string1),'caracteres')
print(f'O tamanho de "{string2}:" ',len(string2),'caracteres')


if string1 != string2:
    print('As duas strings são de tamanhos diferentes')
elif string1 == string2 or string1 != string2:
    print('As duas strings possuem conteudos diferentes')
print('fim')

#2-Nome ao contrário em maiúsculas.
#Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

#title
#upper
#lower

name = input('Qual e o seu nome?  ')
invertida = ' ' .join(palavra[::-1] for palavra in name.split())
print(name.title())
print(name.upper())
print(name.lower())
print(f'O seu nome inverdito fica assim {invertida}')

# 4-Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

your = input('Qual e o seu nome?  ')

for i in range(len(your)):
    print(your[:i+1])

# 5-Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

nom = input('Seu nome? ')
for an in range(len(nom), 0, -1):
    print(nom[:an])

# 6- Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

data = str(input('Que dia voce nasceu?  '))
dia,mes,ano = data.split('/')

print(f'Voce nasceu em {dia} ', end='')

if mes == '01':
    print('Janeiro', end='')
elif mes == '02':
    print('Fevereiro', end='')
elif mes == '03':
    print('Março', end='')
elif mes == '04':
    print('April', end='')
elif mes == '05':
    print('Maio', end='')
elif mes == '06':
    print('Junho', end='')
elif mes == '07':
    print('Julho', end='')
elif mes == '08':
    print('Agosto', end='')
elif mes == '09':
    print('Sembro', end='')
elif mes == '10':
    print('Outubro', end='')
elif mes == '11':
    print('Novembro', end='')
elif mes == '12':
    print('Dezembro', end='')

print(f' de {ano}')

# 7-Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# entrada do dados
frase = input('Qual e a frase?: ')
#contadores
contagem_vogais = 0
contagem_espacos = 0

for caractere in frase:
    if caractere.lower() in 'aeiou':
        contagem_vogais  += 1

    elif caractere == ' ':
        contagem_espacos += 1

print(f'A frase tem {contagem_vogais} vogais e {contagem_espacos} espaços')

# 8-Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

polindromo = input('Escreve uma frase:  ')

if polindromo == polindromo[::-1]:
    print('A palavra é um polindromo')
else:
    print('Não e um polindromo')


# 9- Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
#e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.


cpf = input('Solicitando o CPF: xxx.xxx.xxx-xx ')
#remover os caracteres se o CPF tem 11 dígitos
if len(cpf) != 11:
    print('Seu CPF e válido')
elif cpf.isdigit():
    print('Seu CPF e válido')
else:
    print('O seu CPF e inválido')



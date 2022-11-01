import os

idade: int;                                                         altura: float;                                         peso: float;                          qtdcad: int 
somaIdade: int;                                                     alturaAcDe150ePesoAcDe90: int;                         
mediaIdade: float
percDePessoasEntre10e30comAlturaAcDe190: float

idade = 0
somaIdade = 0
percDePessoasEntre10e30comAlturaAcDe190 = 0
altura = 0
alturaAcDe150ePesoAcDe90 = 0
peso = 0
qtdcad = 0

qtdcad = int(input('Digite a quantidade de cadastros que deseja: '))

for n in range(1,qtdcad + 1):
    print(f'{n}º pessoa ')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))

    os.system('cls')

    if idade > 0:
        somaIdade += idade
        mediaIdade += 1
    if peso > 90 and altura < 1.50:
        alturaAcDe150ePesoAcDe90 += 1
    if idade > 10 and idade < 30 and altura > 1.50:
        percDePessoasEntre10e30comAlturaAcDe190 += 1

print(f'Média das idades das  pessoas informadas{somaIdade/mediaIdade * 100}')

if peso > 90 and altura < 1.50:
    print(f'Quantidade de pessoas com peso acima de 90kg e altura maior que 1.50 {alturaAcDe150ePesoAcDe90}')
elif peso > 90 and altura >= 1.50:
    print('Não ha pessoas com o peso acima de 90kg e aktura acima de 1.50')
elif peso < 90 and altura < 1.50:
    print('Não ha pessoas com o peso acima de 90kg e aktura acima de 1.50')
else:
    print('Não ha pessoas com o peso acima de 90kg e aktura acima de 1.50')

if percDePessoasEntre10e30comAlturaAcDe190 >= 1:
    print(f'porcentagem de pessoas informadas que tem idade entre  10 e 30 anos com altura acima de 1.90 {percDePessoasEntre10e30comAlturaAcDe190/n * 100}')
else:
    print('Não foi informada pessoas com idade entre 10 e 30 anos com altura acima de 1.90')
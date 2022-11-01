import math

num: int
numPrimo: int
numPar: int
contPrimo: int

num = 0
numPrimo = 0
numPar = 0
contPrimo = 0

for n in range(1,11):

    num = int(input("Digite um número: "))

    if num % 2 == 0:
        numPar += num

        for m in range (2,int(math.sqrt(num) + 1)):

            if num % m == 0:
                contPrimo += 1

        if contPrimo == 0:
            numPrimo += num



print(f'Essa é a soma dos números primos informados: {numPrimo}')
print(f'Essa é a soma dos numeros pares informados: {numPar}')
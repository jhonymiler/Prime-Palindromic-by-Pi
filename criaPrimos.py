
from math import floor


def grava(texto, filename='primos.txt'):
    with open(filename, 'a') as f:
        f.write(str(texto)+'\n')


def ePrimoTurbo(n):
    # vamos calular até a metade do número
    limiteDivisao = round(n/2)+1
    with open("primos.txt") as file:
        for line in file:
            primo = int(line)
            if primo < limiteDivisao:
                quociente = n / primo
                resto = n % primo
                # se der zero, é porque é um número composto
                if resto == 0:
                    return False

                else:
                    # se o quociente for menor que o divisor, Bingooo
                    if floor(quociente) <= primo:
                        return True
            else:
                break


def geraPrimos(n):
    ultimoPrimo = 1
    for i in range(1, n+1):
        if (ePrimoTurbo(i) == 1):
            if i > ultimoPrimo:
                ultimoPrimo = i
                grava(i)
            print(i, "\r")


# Encontrar todos n primos até a metade desse número
# Encontrar todos n primos até a metade desse número
num = round(368721912111219127863 / 2)+1
geraPrimos(num)


# Teste se é primo usando os números já salvo no arquivo txt
print(ePrimoTurbo(368721912111219127863))

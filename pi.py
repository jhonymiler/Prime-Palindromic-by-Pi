from math import floor
import wget
import os
import re
import time
import timeit
import termcolor
from termcolor import colored
# -------------------------------------------------------------------------


from discord_webhook import DiscordWebhook, DiscordEmbed

# Coloque o token do seu discord
webhook = DiscordWebhook(
    url='https://discordapp.com/api/webhooks/452345234345245/rl1Awq-qidHztc1a9e1fjeb5fJPDBoJOrAnP-_gGQxLENo4WR1AvkefkQ31kCKQgznoN')


# -------------------------------------------------------------------------

file_url = [
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_01.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_02.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_03.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_04.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_05.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_06.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_07.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_08.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_09.zip',
    'https://archive.org/download/pi_dec_1t/pi_dec_1t_10.zip'
]


dir_zip = './zip'
dir_zip_descompactado = './zip_descompactado'
dir_pi = './pi_particionado'
dir_ultimo = './ultimo'


def criaDiretorio(dir):
    if os.path.isdir(dir) != True:
        os.mkdir(dir)


def listar_arquivos(caminho=None):
    lista_arqs = [arq for arq in os.listdir(caminho)]
    lista_arqs.sort()
    return lista_arqs


def is_prime(n):
    for i in range(2, round((n/2)+1)):
        if (n % i) == 0:
            return False
    return True


def is_palindrome(num):
    pal = str(num)
    if (pal == num[::-1]):
        return True
    else:
        return False


def grava(texto, filename='data.txt'):
    with open(filename, 'a') as f:
        f.write(texto+'\n')


def particiona_arq():
    os.system(
        f"split --byte=21000000 --additional-suffix=.txt {dir_zip_descompactado}/*.txt {dir_pi}/pi_ && cd {dir_zip_descompactado} && rm *.txt")


def ePrimoTurbo(n):
    limiteDivisao = round(n/2)+1  # vamos calular até a metade do número
    with open("primos.txt") as file:
        for line in file:
            primo = int(line)
            if primo < limiteDivisao:
                quociente = n / primo
                resto = n % primo
                if resto == 0:  # se der zero, é porque é um número composto
                    return False
                else:
                    if floor(quociente) <= primo:  # se o quociente for menor que o divisor, Bingooo
                        return True
            else:
                break


pos = 0


def run(lote):
    global pos
    regex = r'(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)\10\9\8\7\6\5\4\3\2\1'
    inicio = timeit.default_timer()
    for arquivo in listar_arquivos(dir_pi):
        with open(dir_pi+'/'+arquivo, 'r') as arq:
            texto = arq.read()

        entradas = re.findall(regex, str(texto))
        # print(colored(str(arquivo), 'magenta'))
        if (len(entradas) > 0):
            i = 0
            for num in entradas:
                frente = ''.join(num)
                verso = num[:-1]
                verso = ''.join(verso)

                palindrome = frente+verso[::-1]

                log = ''
                log += lote+' '+arquivo + ' ' + str(num)+' '+str(i)
                print(
                    colored('Lote:', 'red'),
                    colored(lote, 'blue'),
                    colored('Arquivo', 'red'),
                    colored(arquivo, 'magenta'),
                    colored('Num', 'blue'),
                    colored(str(palindrome), 'green'),
                    colored('Pos arquivo', 'red'),
                    colored(str(i), 'magenta'),
                    colored('Pos Geral', 'red'),
                    colored(str(pos), 'yellow'),
                    sep=' ', end='\r'
                )

                if ePrimoTurbo(int(palindrome)):
                    log += ' Sim'
                    print(log)
                    grava(log)
                    embed = DiscordEmbed(title='Encontrou a porra do Palíndromo',
                                         description=log, color='03b2f8')

                    # add embed object to webhook
                    webhook.add_embed(embed)
                    webhook.execute(remove_embeds=True)
            i += 1
            pos += 21

    fim = timeit.default_timer()
    print('duracao: %f' % (fim - inicio))


# run('arquivo_04')

a = 0
for arquivo in file_url:

    criaDiretorio(dir_zip)
    criaDiretorio(dir_zip_descompactado)
    criaDiretorio(dir_pi)
    criaDiretorio(dir_ultimo)

    os.system(
        f"cd {dir_zip} && wget {arquivo} && unzip *.zip -d ../{dir_zip_descompactado} && rm *.zip")

    particiona_arq()

    if (a == 0):
        primeiro_arquivo = listar_arquivos(dir_pi)[0]
        os.system(f"sed -i 's/3.14/14/g' {dir_pi}/{primeiro_arquivo}")

    os.system(
        f"mv {dir_ultimo}/*.txt {dir_pi}/a.txt && cat {dir_pi}/*.txt > {dir_zip_descompactado}/pi.txt")

    os.system(f"cd {dir_pi} && rm *.txt")

    particiona_arq()

    os.system(f"rm -rf {dir_zip_descompactado}")

    ultimo_arquivo = listar_arquivos(dir_pi)[-1]
    os.system(f"cp {dir_pi}/{ultimo_arquivo} {dir_ultimo}")
    criaDiretorio('./tmp')

    os.system(
        f"cp {dir_pi}/{ultimo_arquivo} ./tmp && mv ./tmp/*.txt ./ultimo__{a}.txt ")

    print("Roda script PI....")
    run(arquivo)

    os.system(f"rm -rf {dir_pi}")
    a += 1

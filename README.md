# Prime-Palindromic-by-Pi

Challenge to find the palindromic prime number of the decimal expansion of the PI number

## Versão 2.1.0

### Aplicações do Sistema

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:


- [x] Baixa o arquivo
- [x] Descompacta
- [x] Divide em bytes específicos
- [x] Limpa as pastas
- [x] Processas os arquivos
- [x] Envia alerta via bot no Discord

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->

- Você instalou a versão mais recente de `<Python>`
- Compatível com `<Linux / Git Bash>`.

## 🚀 Instalando

Para instalar, siga estas etapas:

Arquivo <pi.py> Coloque o token do seu discord para receber a notificação

```
from discord_webhook import DiscordWebhook, DiscordEmbed

# Coloque o token do seu discord
webhook = DiscordWebhook(
    url='https://discordapp.com/api/webhooks/452345234345245/rl1Awq-qidHztc1a9e1fjeb5fJPDBoJOrAnP-_gGQxLENo4WR1AvkefkQ31kCKQgznoN')

```

Se quiser usar o cálculo Turbo dos números primos, primeiro vc deve gerar uma boa quantidade deles
pelo arquivo <geraPrimos.py>
Para isso, coloque um número grande na função <geraPrimos()> e deixe gerar alguns milhares ou quanto for necessário.

```
## Encontrar todos n primos até a metade desse número
num = round(368721912111219127863 / 2)+1 # Encontrar todos n primos até a metade desse número
geraPrimos(num)

```

Se não for usar a função Turbo, apenas realize a seguinte algeração:
Troque a função da linha 132 do arquivo <pi.py>

DE:

```
if ePrimoTurbo(int(palindrome)):

```

PARA:

```
if is_prime(int(palindrome)):

```

## ☕ Usando

Agora você pode rodar no seu terminal:

```
python pi.py
```

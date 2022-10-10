# Digitar um número de 0 a 10 até acertar o valor que computador selecionou de forma randômica.
from random import randint
from time import sleep
num = int(input('Tente acertar o número de 0 a 10 que o computador está pensando: '))
tentativas = 1
print('\033[034mProcessando...\033[m')
sleep(1)
numpc = randint(0, 10)
while num != numpc:
    num = int(input('\033[31mTente novamente acertar o número de 0 a 10 que o computador está pensando: \033[m'))
    tentativas +=1
print('Parabéns, o número que o computador estava pensando é {} e você tentou {} vezes.'.format(numpc, tentativas))

"""
Gerador de Senhas - v0.1
Neste projeto utilizei algumas informações como letras em caixa alta e caixa baixa, números e símbolos.
Utilizei do rep random onde executa sequencias de formas aleatórias.

Desenvolvido por Rafael Rosário.
"""
import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@_"

s = lower + upper + numbers + symbols

passlen = 16
print('Sua senha é: ')
password = "".join(random.sample(s, passlen))
print(password)

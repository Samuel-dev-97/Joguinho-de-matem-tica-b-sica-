import random
import time

OPERADORES = ["+", "-", "*"]
MIN_OPERANDO = 3
MAX_OPERANDO = 12
TOTAL_PROBLEMAS = 10


def gerar_problema():
    esquerda = random.randint(MIN_OPERANDO, MAX_OPERANDO)
    direita = random.randint(MIN_OPERANDO, MAX_OPERANDO)
    operador = random.choice(OPERADORES)

    expressao = str(esquerda) + " " + operador + " " + str(direita)
    resposta = eval(expressao)
    return expressao, resposta


erros = 0
input("Pressione Enter para começar!")
print("----------------------")

tempo_inicio = time.time()

for i in range(TOTAL_PROBLEMAS):
    expressao, resposta = gerar_problema()
    while True:
        tentativa = input("Problema #" + str(i + 1) + ": " + expressao + " = ")
        if tentativa == str(resposta):
            break
        erros += 1

tempo_fim = time.time()
tempo_total = round(tempo_fim - tempo_inicio, 2)

print("----------------------")
print("Bom trabalho! Você terminou em", tempo_total, "segundos!")

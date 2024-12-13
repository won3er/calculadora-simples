import tkinter
from tkinter import messagebox

def calculadora():
    # Funções
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b != 0:
            return a / b
        else:
            return "Erro, divisão por zero."

    # Exibe as opções de operação
    print("Escolha uma operação: ")
    print("1. Soma ")
    print("2. Subtração ")
    print("3. Multiplicação ")
    print("4. Divisão ")

    # Recebe a operação
    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Verifica se a operação é válida
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")
        return  # Sai da função se a operação for inválida

    # Recebe números para operação
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        return  # Sai da função se os valores não forem válidos

    # Executa a operação
    if operacao == '1':
        resultado = somar(num1, num2)
    elif operacao == '2':
        resultado = subtrair(num1, num2)
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
    elif operacao == '4':
        resultado = divisao(num1, num2)

    # Exibe o resultado
    print(f"Resultado: {resultado}")

# Chama a função calculadora
calculadora()

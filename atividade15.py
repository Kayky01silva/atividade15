# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

def calcular(numero1, numero2, operacao):
    if operacao == "soma":
        return numero1 + numero2
    elif operacao == "subtração":
        return numero1 - numero2
    elif operacao == "multiplicação":
        return numero1 * numero2
    elif operacao == "divisão":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, subtração, multiplicação, divisão): ").lower()

resultado = calcular(numero1, numero2, operacao)
print(f"O resultado da operação é: {resultado}")
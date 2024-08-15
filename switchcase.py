# Turminha, primeiro vocês devem criar a função!

def calculadora(operacao, num1, num2):
    match operacao:
        case "soma":
            return num1 + num2
        case "subtracao":
            return num1 - num2
        case "multiplicacao":
            return num1 * num2
        case "divisao":
            if num2 != 0:
                return num1 / num2
            else:
                return "Erro: Divisão por zero"
        case _:
            return "Operação inválida"

# Depois vocês devem, de fato, criar o algorítmo que vai chamar a função!

operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = calculadora(operacao, num1, num2)

print(f"O resultado da {operacao} é: {resultado}")

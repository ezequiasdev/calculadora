'''Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.'''


soma = 1
subtracao = 2
multiplicacao = 3
divisao = 4
resultado = 0

operacao = int(input("Indique a operação que você deseja realizar (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))
numero1 = int(input("Indique o primeiro número da operação: "))
numero2 = int(input("Indique o segundo número da operação: "))

def calculadora(numero1, numero2, operacao):
    if (operacao == soma):
        return numero1 + numero2
    elif (operacao == subtracao):
        return numero1 - numero2
    elif(operacao == multiplicacao):
        return numero1 * numero2
    elif(operacao == divisao):
        return numero1/numero2
    else:
        print("Operação inválida.")
        return 0
    
resultado = calculadora(numero1, numero2, operacao)
print("Resultado:", resultado)

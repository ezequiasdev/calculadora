'''Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.'''


def calcularIdade():
    while True:
        nome = input("Digite seu nome completo: ")
        anoNascimento = input("Digite seu ano de nascimento (entre 1922 e 2021): ")

        try:
            anoNascimento = int(anoNascimento)
            if 1922 <= anoNascimento <= 2021:
                idade = 2022 - anoNascimento
                print(f"{nome}, você completou ou completará {idade} anos em 2022.")
                break
            else:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Por favor, digite um número válido para o ano.")

# Chama a função para calcular a idade
calcularIdade()

'''Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.
Recursos'''


def calculadora():
    while True:
        print("Escolha uma opção:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação ou 0 para sair: ")

        if opcao == '0':
            break
        elif opcao in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            if opcao == '1':
                print("Resultado: ", num1 + num2)
            elif opcao == '2':
                print("Resultado: ", num1 - num2)
            elif opcao == '3':
                print("Resultado: ", num1 * num2)
            elif opcao == '4':
                try:
                    print("Resultado: ", num1 / num2)
                except ZeroDivisionError:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Essa opção não existe")


calculadora()


#Para não ocorrer divisões por 0, basta transferir o controle utilizando a função try, e após a função except
def menu():
    print("Bem-vindo à CapibaTech!")
    print("Já possui Cadastro?")
    print("Escolha uma opção:")
    print("1. Entrar")
    print("2. Cadastrar")
    print("3. Sair")
    

    while True:
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("Você escolheu a Opção 1. Faça algo aqui.")    

        elif escolha == "2":
            print("Você escolheu a Opção 2. Faça algo aqui.")
              
        elif escolha == "3":
            print("Saindo do menu.")
            break

        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    menu()

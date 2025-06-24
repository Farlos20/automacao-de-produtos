import time
def menu():
    while True:
        print("\n----MENU-----")
        print("1 - Dizer Olá")
        print("2 - Mais informações")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Digite seu nome: \n")
            print(f"Ola {nome} Seja Bem Vindo 😜")
            time.sleep(1)   
        elif escolha == "2":
            print("Este é um menu Criado Por Carlos")
            time.sleep (2)
        elif escolha == "3":
            print("Saindo do programa... TCHAUU 🎇 ")
            time.sleep(1)
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()


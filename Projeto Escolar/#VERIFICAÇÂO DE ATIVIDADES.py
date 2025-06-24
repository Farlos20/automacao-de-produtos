#VERIFICAÇÂO DE ATIVIDADES
import time
print(" 👌 Ola, Sou o seu mais novo Parceiro de Organização de Atividades e Trabalhoes em Geral \n \n 👀 Sou responsavel de te Lembrar de atividades pendentes, Trabalhos,Projetos e ETC")
nome_usuario = input("Para Começarmos Digite seu Nome:\n \n ")
print("🎪 Este é o MENU destinado para adicionar seus afazeres e verificar suas pendencias \n")

dica_01 = False
tarefas = []

def remover_tarefa():
    if not tarefas:
        print("Não há tarefas para remover.\n")
        time.sleep(1)
        return
    print("Selecione o número da tarefa que deseja remover:")
    print("----------------------------")
    print("Nº - Atividade               - Data Limite")
    print("----------------------------")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i} - {tarefa[0]:<25} - {tarefa[1]}")
    print("----------------------------")
    try:
        escolha = int(input("Número da tarefa a remover: "))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            print(f"🎉 {nome_usuario}, tarefa '{tarefa_removida[0]}' removida com sucesso!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Por favor, digite um número válido.\n")



def Menu() :
    while True :
        global dica_01
        print(" 🏆 (1) Adicionar tarefas pendentes")
        print(" 👨‍✈️ (2) Verificar Tarefas Pendentes")
        print(" 💎 (3) remover atividade Feitas")
        print(" 🚀 (4) Sair do Codigo \n")
        escolha = input('Selecione o numero da ação desejada: \n' )
        if escolha == "1" :
            if dica_01 == False :
                print("OBSERVAÇÂO, Adicione uma atividade por vez, caso queira adicionar mais de uma, repita o processo e adicione a nova \n")
                dica_01 = True
            atividade_nome = input("👾 Digite O Nome da Materia ou Atividade Pendente: ")
            data_limite = input("\n 👻 Agora Digite a Data Limite de entrega da atividade: ")
            time.sleep(1)
            print("\n Otimo Agora caso queira relembrar as atividades ja pendentes volte e vá a opção 2 \n")
            time.sleep(1.5)
            tarefas.append([atividade_nome,data_limite ])
            print("\n \n \n")        
            
        elif escolha == "2":
            if not tarefas :
                print("Não há atividades pendentes \n \n ")
                time.sleep(1)
            else :
                print("😜 Atividades ---  Data de Entrega")
                print("--------------------------------")
                for tarefa in tarefas :
                    print(tarefa[0],"-",tarefa[1])
                    time.sleep(2.3)
                    print("\n \n \n")

        elif escolha == "3":
            remover_tarefa()
            print("\n \n \n")

        elif escolha == "4" :
            print("Saindo do codigo ✨")
            time.sleep(1)
            break
            

Menu()


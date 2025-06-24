# VERIFICAÇÃO DE ATIVIDADES
import time

print("\n👌 Olá! Sou o seu parceiro para organizar tarefas e trabalhos escolares.")
print("👀 Minha função é lembrar você de atividades pendentes, provas, projetos e muito mais!\n")

nome_usuario = input("💬 Para começarmos, digite seu nome: ")
print(f"\n🎪 Bem-vindo(a), {nome_usuario}! Este é o menu principal para adicionar e verificar suas pendências.\n")

dica_01 = False
tarefas = []

def remover_tarefa():
    if not tarefas:
        print("\n⚠️ Nenhuma tarefa para remover.\n")
        time.sleep(1)
        return

    print("\n🗑️ Selecione o número da tarefa que deseja remover:")
    print("------------------------------------------------------")
    print(" Nº | Atividade                   | Data de Entrega")
    print("------------------------------------------------------")
    for i, tarefa in enumerate(tarefas, 1):
        print(f" {i:<2} | {tarefa[0]:<25} | {tarefa[1]}")
    print("------------------------------------------------------")

    try:
        escolha = int(input("Digite o número da tarefa a remover: "))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            print(f"\n✅ Tarefa '{tarefa_removida[0]}' removida com sucesso!\n")
        else:
            print("\n⚠️ Número inválido.\n")
    except ValueError:
        print("\n⚠️ Digite um número válido.\n")


def Menu():
    while True:
        global dica_01
        print("📋 MENU DE OPÇÕES")
        print("  🏆 (1) Adicionar nova tarefa")
        print("  📂 (2) Verificar tarefas pendentes")
        print("  ✅ (3) Remover tarefa concluída")
        print("  🚪 (4) Sair\n")

        escolha = input("Escolha uma opção (1 a 4): ")

        if escolha == "1":
            if not dica_01:
                print("\nℹ️ Dica: Adicione uma tarefa por vez. Para mais, repita o processo.\n")
                dica_01 = True

            atividade_nome = input("📝 Nome da matéria ou atividade: ")
            data_limite = input("📅 Data de entrega (ex: 28/05/2025): ")
            tarefas.append([atividade_nome, data_limite])

            print("\n✅ Tarefa adicionada com sucesso!")
            print("🔁 Para revisar suas tarefas, escolha a opção 2.\n")
            time.sleep(1.5)

        elif escolha == "2":
            if not tarefas:
                print("\n📭 Nenhuma tarefa pendente no momento.\n")
                time.sleep(1)
            else:
                print("\n📌 TAREFAS PENDENTES")
                print("--------------------------------------")
                print(" Atividade                 | Entrega")
                print("--------------------------------------")
                for tarefa in tarefas:
                    print(f" {tarefa[0]:<25} | {tarefa[1]}")
                print("--------------------------------------\n")
                time.sleep(2)

        elif escolha == "3":
            remover_tarefa()
            time.sleep(1)

        elif escolha == "4":
            print("\n👋 Encerrando... Bons estudos!\n")
            time.sleep(1)
            break

        else:
            print("\n⚠️ Opção inválida. Tente novamente.\n")


Menu()

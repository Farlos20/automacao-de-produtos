# IDEIA:REVISAR MATERIAS ESCOLARES ENSINO MEDIO 1,2,3 ANO
import time
import sys
#Mostar Print DIGITADO
def print_digitado(mensagem, velocidade=0.05):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def mostrar_conteudos(ano, materia):
    print(f"\n📘 Conteúdos de {materia} - {ano}:")

    if ano == "1º Ano":
        if materia == "Matemática":
            print("- Equações do 1º grau")
            print("- Expressões algébricas")
            explicação_1 = input (" \n Gostaria que explique algum assunto ? \n ")
            if explicação_1.lower() == "sim" :
                pergunta_01 = input ("Quer saber qual assunto ? \n (1) Equação do   1º grau \n (2) Expressões algébricas \n responda conforme numero desejado \n")
                if pergunta_01 == "1" :
                    print_digitado ("Aqui esta revisão sobre a Equação: 🧧 \n Equação do 1º grau é uma igualdade com uma incógnita elevada a 1, onde se busca o valor dessa incógnita que satisfaz a igualdade.")
                    print_digitado ("O resultado da equação 2x + 3 = 7 é: \n \n Primeiro, subtraia 3 dos dois lados: \n\n 2x = 7 - 3 \n 2x = 4 \n\n Depois, divida os dois lados por 2: \n\n x = 4 ÷ 2 \n x = 2 \n \n Então, x = 2.")
                    pergunta_02 = input ("Gostaria de saber sobre Expressoes algebricas tambem ? ")
                    time.sleep (1)
                    if pergunta_02.lower() == "sim":
                        print_digitado("Expressões algébricas são combinações de números, letras e operações.\nExemplo: 3x + 5")
                    else:
                        print("Ok, vamos continuar.")
                elif pergunta_01 == "2":
                    print_digitado("Expressões algébricas são combinações de números, letras e operações.\nExemplo: 3x + 5")
                else :
                    print (" \n OPS,caracter incorreto ")
                    time.sleep (1)
            elif explicação_1.lower() == "não" :
                print(" \n OK, Volte Mais Tarde")
                time.sleep (1)
            else :
                print(" \nCaracter Incorreto, tente novamente")
                time.sleep (1)
        
        elif materia == "Português":
            print("- Gêneros textuais ")
            print("- Classes gramaticais ")
            explicação_1 = input("Quer explicação? (sim/não) ")
            if explicação_1.lower() == "sim":
                escolha = input("Escolha: (1) Gêneros textuais (2) Classes gramaticais ")
                if escolha == "1":
                    print_digitado("Gêneros textuais são tipos de textos com características específicas.\nExemplo: Carta, notícia, poema.")
                elif escolha == "2":
                    print_digitado("Classes gramaticais são categorias das palavras.\nExemplo: Substantivo, verbo, adjetivo.")
                else:
                    print("Opção inválida.")
            else:
                print("Ok, vamos continuar.")

    elif ano == "2º Ano":
        if materia == "Matemática":
            print("- Função do 1º grau")
            print("- Progressões Aritméticas ")
            explicação_2 = input("Quer explicação? (sim/não) ")
            if explicação_2.lower() == "sim":
                escolha = input("Escolha: (1) Função do 1º grau (2) Progressões Aritméticas ")
                if escolha == "1":
                    print_digitado("Função do 1º grau tem fórmula y = ax + b.\nExemplo: y = 2x + 3")
                elif escolha == "2":
                    print_digitado("PA é sequência com diferença constante.\nExemplo: 2, 4, 6, 8...")
                else:
                    print("Opção inválida.")
            else:
                print("Ok, vamos continuar.")

        elif materia == "Português":
            print("- Figuras de linguagem ")
            print("- Funções da linguagem ")
            explicação_2 = input("Quer explicação? (sim/não) ")
            if explicação_2.lower() == "sim":
                escolha = input("Escolha: (1) Figuras de linguagem (2) Funções da linguagem ")
                if escolha == "1":
                    print_digitado("Figuras de linguagem são formas de dar expressividade.\nExemplo: Metáfora - 'Ele é uma fera'")
                elif escolha == "2":
                    print_digitado("Funções da linguagem são finalidades da comunicação.\nExemplo: Função emotiva - expressa sentimentos.")
                else:
                    print("Opção inválida.")
            else:
                print("Ok, vamos continuar.")

    elif ano == "3º Ano":
        if materia == "Português":
            print("- Produção de texto dissertativo-argumentativo ")
            print("- Análise de textos multimodais ")
            explicação_3 = input("Quer explicação? (sim/não) ")
            if explicação_3.lower() == "sim":
                escolha = input("Escolha: (1) Produção dissertativo-argumentativa (2) Análise textos multimodais ")
                if escolha == "1":
                    print_digitado("Texto para defender uma opinião com argumentos.\nExemplo: Redação do ENEM.")
                elif escolha == "2":
                    print_digitado("Textos que combinam imagens, sons e palavras.\nExemplo: Propaganda.")
                else:
                    print("Opção inválida.")
            else:
                print("Ok, vamos continuar.")
        elif materia == "Matemática":
            print("- Função Exponencial")
            print("- Probabilidade")
            explicação_3 = input("Quer explicação? (sim/não) ")
            if explicação_3.lower() == "sim":
                escolha = input("Escolha: (1) Função Exponencial (2) Probabilidade ")
                if escolha == "1":
                    print_digitado("Função onde a variável está no expoente.\nExemplo: y = 2^x")
                elif escolha == "2":
                    print_digitado("Probabilidade é chance de um evento ocorrer.\nExemplo: Cara ou coroa = 50%.")
                else:
                    print("Opção inválida.")
            else:
                print("Ok, vamos continuar.")

while True:

    print("\n=== REVISÃO DE CONTEÚDOS DO ENSINO MÉDIO ===")
    print("1 - 1º Ano")
    print("2 - 2º Ano")
    print("3 - 3º Ano")
    print("4 - Sair")

    escolha_ano = input("Escolha o ano (1/2/3/4): ").strip()

    if escolha_ano == "1":
        ano = "1º Ano"
        print("\nMatérias disponíveis:")
        print("1 - Matemática")
        print("2 - Português")
        materia_escolha = input("Escolha a matéria: ").strip()
        if materia_escolha == "1":
            mostrar_conteudos(ano, "Matemática")
        elif materia_escolha == "2":
            mostrar_conteudos(ano, "Português")

    elif escolha_ano == "2":
        ano = "2º Ano"
        print("\nMatérias disponíveis:")
        print("1 - Matemática")
        print("2 - Português")
        materia_escolha = input("Escolha a matéria: ").strip()
        if materia_escolha == "1":
            mostrar_conteudos(ano, "Matemática")
        elif materia_escolha == "2":
            mostrar_conteudos(ano, "Português")

    elif escolha_ano == "3":
        ano = "3º Ano"
        print("\nMatérias disponíveis:")
        print("1 - Matemática")
        print("2 - Português")
        materia_escolha = input("Escolha a matéria: ").strip()
        if materia_escolha == "1":
            mostrar_conteudos(ano, "Matemática")
        elif materia_escolha == "2":
            mostrar_conteudos(ano, "Português")

    elif escolha_ano == "4":
        print("Saindo... Bons estudos! 👋")
        break

    else:
        print("Opção inválida. Tente novamente.")

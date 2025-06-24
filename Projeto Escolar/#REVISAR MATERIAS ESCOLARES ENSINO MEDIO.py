import time
import sys

#FUNÇÃO PRINT DIGITADO
def print_digitado(mensagem, velocidade=0.05):
    for letra in mensagem:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

#FUNÇÃO DE CONTEÚDOS E REVISÃO
def mostrar_conteudos(ano, materia):
    print(f"\n📘 Conteúdos de {materia} - {ano}:")

    if ano == "1º Ano":
        if materia == "Matemática":
            print("- Equações do 1º grau")
            print("- Expressões algébricas")
            explicação_1 = input("Gostaria que explique algum assunto ?  ")
            if explicação_1.lower() == "sim":
                pergunta_01 = input("Quer saber qual assunto ? \n (1) Equação do 1º grau \n (2) Expressões algébricas \n responda conforme numero desejado\n ")
                if pergunta_01 == "1":
                    print_digitado("Aqui esta revisão sobre a Equação: 🧧 \n Equação do 1º grau é uma igualdade com uma incógnita elevada a 1, onde se busca o valor dessa incógnita que satisfaz a igualdade.")
                    print_digitado("O resultado da equação 2x + 3 = 7 é: \n \n Primeiro, subtraia 3 dos dois lados: \n\n 2x = 7 - 3 \n 2x = 4 \n\n Depois, divida os dois lados por 2: \n\n x = 4 ÷ 2 \n x = 2 \n \n Então, x = 2.")
                    time.sleep(1)                    
                elif pergunta_01 == "2":
                    print_digitado("Expressões algébricas são combinações de números, letras e operações matemáticas (como +, −, ×, ÷). \n As letras (como x, y) representam valores desconhecidos ou variáveis.")
                    print_digitado("Exemplo: \n 👉 3x + 2 é uma expressão algébrica. \n Aqui, 3x significa 3 vezes x, e + 2 é somado ao resultado. \n Você não resolve a expressão, apenas simplifica ou substitui o valor da letra para encontrar um resultado.    ")
                else:
                    print("\n OPS,caracter incorreto ")
                    time.sleep(1)
            elif explicação_1.lower() == "não":
                print("\n OK, Volte Mais Tarde")
                time.sleep(1)
            else:
                print("\nCaracter Incorreto, tente novamente")
                time.sleep(1)

        elif materia == "Português":
            print("- Gêneros textuais ")
            print("- Classes gramaticais ")
            explicação_2 = input("Gostaria que explique algum assunto ?  ")
            if explicação_2.lower() == "sim":
                pergunta_02 = input("Quer saber qual assunto ? \n (1) Gêneros textuais \n (2) Classes gramaticais \n responda conforme numero desejado \n ")
                if pergunta_02 == "1":
                    print_digitado("Gêneros textuais são tipos de textos com funções sociais diferentes, como informar, argumentar, narrar, etc. \n  os principais gêneros são: \n")
                    print_digitado("Artigo de opinião - defende um ponto de vista. \n Narrativa - conta uma história com começo, meio e fim. \n Carta argumentativa - tenta convencer alguém por escrito. \n Reportagem - informa sobre um fato real e atual. \n Cada gênero tem estrutura e linguagem próprias, conforme o objetivo.")
                elif pergunta_02 == "2":
                    print_digitado("Classes gramaticais são os tipos de palavras conforme a função que têm na frase.\n As principais são: \n Substantivo - nomeia: casa, João \n Adjetivo - qualifica: bonito, rápido \n Verbo - ação ou estado: correr, ser \n Advérbio - modifica verbo: rapidamente, ontem \n Pronome - substitui ou acompanha o nome: ele, meu \n Preposição – liga termos: de, com, em \n Conjunção - liga orações: e, mas, porque \n Cada uma tem uma função específica na frase.")

        elif materia == "Historia":
            print("Antiguidade ")
            print("Idade Média ")
            explicação_3 = input("Gostaria que explique algum assunto ? ")
            if explicação_3.lower() == "sim":
                pergunta_03 = input("Quer saber qual assunto ? \n (1) Antiguidade \n (2) Idade Média \n responda conforme numero desejado ")
                if pergunta_03 == "1":
                    print_digitado("A antiguidade é o Período das primeiras civilizações e impérios. \n Mesopotâmia/Egito: agricultura, religião e escrita. \n Hebreus/Fenícios/Persas: monoteísmo, comércio, império. \n")
                    print_digitado("Grécia: democracia, filosofia. \n Roma: leis, exército, império.")
                elif pergunta_03 == "2":
                    print_digitado("A Idade media é o Período entre a queda de Roma e o Renascimento (476 a 1453).\n Feudalismo: sociedade rural, nobres, servos e Igreja.\n Igreja Católica: muito poder. \n Cruzadas: guerras religiosas.\n Renascimento comercial e urbano: crescimento das cidades e do comércio.")

        elif materia == "Geografia":
            print("Cartografia")
            print("Formação do Espaço Geográfico")
            explicação_4 = input("Gostaria que explique algum assunto ? ")
            if explicação_4.lower() == "sim":
                pergunta_04 = input("Quer saber qual assunto ? \n (1) Cartografia \n (2) Formação do espaço Geografico \n responda conforme numero desejado  \n")
                if pergunta_04 == "1":
                    print_digitado("Cartografia É o estudo e a criação de mapas. \n Mostra o espaço geográfico. \n Usa escalas, coordenadas e projeções.")
                elif pergunta_04 == "2":
                    print_digitado("Formação do Espaço Geográfico é como o ser humano transforma a natureza ao viver e construir.\n Envolve: cidades, estradas, fábricas, paisagens. \n Espaço = natureza + ação humana. ")
                    time.sleep(1)

    elif ano == "2º Ano":
        if materia == "Matemática":
            print("- Função do 1º grau")
            print("- Progressões Aritméticas ")
        elif materia == "Português":
            print("- Figuras de linguagem ")
            print("- Funções da linguagem ")
        elif materia == "Historia":
            print("Idade Moderna")
            print("Revoluções Burguesas")
            explicação_3 = input("Gostaria que explique algum assunto ? ")
            if explicação_3.lower() == "sim":
                pergunta_03 = input("Quer saber qual assunto ? \n (1) Idade Moderna \n (2) Revoluções Burguesas \n responda conforme numero desejado ")
                if pergunta_03 == "1":
                    print_digitado("Idade Moderna é o Período de transição com mudanças políticas, econômicas e culturais. \n Renascimento, Grandes Navegações, Absolutismo. \n 👉 Início do mundo moderno.")
                elif pergunta_03 == "2":
                    print_digitado("Revoluções Burguesas são Conflitos que consolidaram o poder da burguesia. \n Revolução Inglesa e Francesa. \n 👉 Queda da monarquia e avanço da democracia.")
        elif materia == "Geografia":
            print("Geopolítica")
            print("Industrialização")
            explicação_4 = input("Gostaria que explique algum assunto ? ")
            if explicação_4.lower() == "sim":
                pergunta_04 = input("Quer saber qual assunto ? \n (1) Geopolítica \n (2) Industrialização \n responda conforme numero desejado \n")
                if pergunta_04 == "1":
                    print_digitado("Geopolítica é o Estudo das relações de poder entre países. \n Guerras, blocos econômicos, disputas territoriais. \n 👉 Quem manda no mundo e por quê.")
                elif pergunta_04 == "2":
                    print_digitado("Industrialização é a Transformação com base em indústrias e máquinas. \n Revolução Industrial, países desenvolvidos e subdesenvolvidos. \n 👉 Mudança na economia e no espaço.")

    elif ano == "3º Ano":
        if materia == "Português":
            print("- Produção de texto dissertativo-argumentativo ")
            print("- Análise de textos multimodais ")
        elif materia == "Matemática":
            print("- Função Exponencial")
            print("- Probabilidade")
        elif materia == "Historia":
            print("Brasil Colônia ao Império")
            print("Brasil República")
            explicação_3 = input("Gostaria que explique algum assunto ? ")
            if explicação_3.lower() == "sim":
                pergunta_03 = input("Quer saber qual assunto ? \n (1) Brasil Colônia ao Império \n (2) Brasil República \n responda conforme numero desejado ")
                if pergunta_03 == "1":
                    print_digitado("Brasil Colônia ao Império é o Período da chegada dos portugueses até Dom Pedro II. \n Exploração, escravidão, independência. \n 👉 Formação do Brasil.")
                elif pergunta_03 == "2":
                    print_digitado("Brasil República vai de 1889 até hoje: golpes, ditaduras e democracia. \n República Velha, Vargas, Ditadura Militar, Nova República. \n 👉 Política e sociedade no Brasil atual.")
        elif materia == "Geografia":
            print("Meio ambiente e sustentabilidade")
            print("Agricultura e espaço rural")
            explicação_4 = input("Gostaria que explique algum assunto ? ")
            if explicação_4.lower() == "sim":
                pergunta_04 = input("Quer saber qual assunto ? \n (1) Meio ambiente e sustentabilidade \n (2) Agricultura e espaço rural \n responda conforme numero desejado \n")
                if pergunta_04 == "1":
                    print_digitado("Meio ambiente e sustentabilidade é a Relação entre o ser humano e a natureza. \n Desmatamento, poluição, aquecimento global. \n 👉 Preservar o planeta.")
                elif pergunta_04 == "2":
                    print_digitado("Agricultura e espaço rural é o Uso da terra no campo e produção de alimentos. \n Latifúndio, agronegócio, agricultura familiar. \n 👉 Campo e economia.")

# MENU PRINCIPAL
while True:
    print("\n=== Sistema de Revisão Escolar ===")
    print("📅 Escolha o ano que deseja revisar:")
    print("1 - 1º Ano")
    print("2 - 2º Ano")
    print("3 - 3º Ano")
    print("0 - Sair")
    escolha_ano = input("🔎 Digite o número do ano: ").strip()

    if escolha_ano == "1":
        ano = "1º Ano"
        print("\nMatérias disponíveis:")
        print("1 - Matemática 🔥")
        print("2 - Português  📖")
        print("3 - Historia   🌆")
        print("4 - Geografia  🌍 ")
        materia_escolha = input("Escolha a matéria: ").strip()
        if materia_escolha == "1":
            mostrar_conteudos(ano, "Matemática")
        elif materia_escolha == "2":
            mostrar_conteudos(ano, "Português")
        elif materia_escolha == "3":
            mostrar_conteudos(ano, "Historia")
        elif materia_escolha == "4":
            mostrar_conteudos(ano, "Geografia")

    elif escolha_ano == "2":
        ano = "2º Ano"
        print("\nMatérias disponíveis:")
        print("1 - Matemática")
        print("2 - Português")
        print("3 - Historia")
        print("4 - Geografia")
        materia_escolha = input("Escolha a matéria: ").strip()
        if materia_escolha == "1":
            mostrar_conteudos(ano, "Matemática")
        elif materia_escolha == "2":
            mostrar_conteudos(ano, "Português")
        elif materia_escolha == "3":
            mostrar_conteudos(ano, "Historia")
        elif materia_escolha == "4":
            mostrar_conteudos(ano, "Geografia")

    elif escolha_ano == "3":
        ano = "3º Ano"
        print("\nMatérias disponíveis:")
        print("1 - Matemática")
        print("2 - Português")
        print("3 - Historia")
        print("4 - Geografia")
        materia_escolha = input("Escolha a matéria: ").strip()
        if materia_escolha == "1":
            mostrar_conteudos(ano, "Matemática")
        elif materia_escolha == "2":
            mostrar_conteudos(ano, "Português")
        elif materia_escolha == "3":
            mostrar_conteudos(ano, "Historia")
        elif materia_escolha == "4":
            mostrar_conteudos(ano, "Geografia")

    elif escolha_ano == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")


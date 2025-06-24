import time      # para usar a função sleep() e simular espera


def progresso():
    print("Carregando", end="", flush=True)  # imprime "Carregando" sem quebrar a linha
    for _ in range(3):                       # executa o bloco 3 vezes
        time.sleep(0.7)                      # espera 0.7 segundo
        print(".", end="", flush=True)      # imprime um ponto a cada passo, sem pular linha
    print("\nConcluído!")                    # quebra linha e imprime "Concluído!"

progresso()
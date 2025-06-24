import tkinter as tk
from tkinter import messagebox
import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 20
        self.defesa = 10
        self.pocoes = 3

    def usar_pocao(self):
        if self.pocoes > 0:
            cura = random.randint(15, 40)
            self.vida += cura
            self.pocoes -= 1
            return f"{self.nome} usou uma poção e recuperou {cura} de vida!"
        else:
            return "Você não tem mais poções!"

    def atacar(self, inimigo):
        dano = max(0, self.ataque - inimigo.defesa)
        inimigo.vida -= dano
        return dano

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 50
        self.ataque = 15
        self.defesa = 5

    def atacar(self, jogador):
        dano = max(0, self.ataque - jogador.defesa)
        jogador.vida -= dano
        return dano

# Função para atualizar a interface
def atualizar_interface():
    vida_jogador_label.config(text=f"{jogador.nome} HP: {jogador.vida}")
    vida_inimigo_label.config(text=f"{inimigo.nome} HP: {inimigo.vida}")
    pocoes_label.config(text=f"Poções: {jogador.pocoes}")

# Função de ataque
def atacar():
    if jogador.vida <= 0:
        messagebox.showinfo("Game Over", "Você está sem vida!")
        return

    dano = jogador.atacar(inimigo)
    text_area.insert(tk.END, f"{jogador.nome} causou {dano} de dano!\n")

    if inimigo.vida <= 0:
        text_area.insert(tk.END, f"{inimigo.nome} foi derrotado!\n")
        atualizar_interface()
        return

    dano_inimigo = inimigo.atacar(jogador)
    text_area.insert(tk.END, f"{inimigo.nome} atacou e causou {dano_inimigo} de dano!\n")

    if jogador.vida <= 0:
        text_area.insert(tk.END, f"{jogador.nome} foi derrotado!\n")

    atualizar_interface()

# Função para usar poção
def usar_pocao():
    resultado = jogador.usar_pocao()
    text_area.insert(tk.END, resultado + "\n")
    atualizar_interface()

# Criação da Janela
janela = tk.Tk()
janela.title("RPG Legends - Batalha")

jogador = Jogador("Herói")
inimigo = Inimigo("Goblin")

vida_jogador_label = tk.Label(janela, text="")
vida_jogador_label.pack()

vida_inimigo_label = tk.Label(janela, text="")
vida_inimigo_label.pack()

pocoes_label = tk.Label(janela, text="")
pocoes_label.pack()

botao_ataque = tk.Button(janela, text="Atacar", command=atacar)
botao_ataque.pack()

botao_pocao = tk.Button(janela, text="Usar Poção", command=usar_pocao)
botao_pocao.pack()

text_area = tk.Text(janela, height=10, width=50)
text_area.pack()

atualizar_interface()
janela.mainloop()

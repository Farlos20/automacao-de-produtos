import random
import time

class Personagem:
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        return dano

    def esta_vivo(self):
        return self.vida > 0

class Jogador(Personagem):
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int, pocao: int):
        super().__init__(nome, vida, ataque, defesa)
        self.pocao = pocao

    def usar_pocao(self):
        if self.pocao > 0:
            cura = random.randint(15, 50)
            self.vida += cura
            self.pocao -= 1
            print(f"{self.nome} usou uma poção e recuperou {cura} de vida!")
        else:
            print("Você não tem poções restantes!")

class NPC(Personagem):
    pass

def batalhar(jogador: Jogador, npc: NPC):
    if jogador.vida <= 0:
        print("Você não pode batalhar, pois está sem vida. Use uma poção para recuperar.")
        return

    npc.vida = 15  # HP inicial do NPC

    while jogador.esta_vivo() and npc.esta_vivo():
        print(f"\n{jogador.nome} - Vida: {jogador.vida}, Poções: {jogador.pocao}")
        print(f"{npc.nome} - Vida: {npc.vida}")
        print("\nEscolha uma ação:")
        print("1. Atacar")
        print("2. Usar poção")
        escolha = input("> ")

        if escolha == "1":
            dano = jogador.atacar(npc)
            print(f"{jogador.nome} atacou {npc.nome} e causou {dano} de dano!")
        elif escolha == "2":
            jogador.usar_pocao()
        else:
            print("Escolha inválida!")

        if npc.esta_vivo():
            dano = npc.atacar(jogador)
            print(f"{npc.nome} atacou {jogador.nome} e causou {dano} de dano!")

        time.sleep(1)

    if jogador.esta_vivo():
        print(f"\n{jogador.nome} venceu a batalha!")
    else:
        print(f"\n{npc.nome} venceu a batalha...")

def main():
    nome_jogador = input("Digite o nome do seu personagem: ")
    jogador = Jogador(nome=nome_jogador, vida=100, ataque=20, defesa=10, pocao=3)
    npc = NPC(nome="Goblin", vida=50, ataque=15, defesa=5)

    while jogador.esta_vivo():
        print("\nVocê encontrou um inimigo!")
        batalhar(jogador, npc)
        if jogador.esta_vivo():
            continuar = input("Deseja continuar jogando? (s/n): ").lower()
            if continuar != "s":
                break
        else:
            print("Você foi derrotado...")
            break


#bibliotecas
import time
import random
import os
import sys


# Função para imprimir texto com efeito de digitação
def print_digitado(texto, velocidade=0.05):
    for caractere in texto:
        sys.stdout.write(caractere)  # Escreve um caractere sem pular linha
        sys.stdout.flush()  # Atualiza o terminal para exibir o caractere imediatamente
        time.sleep(velocidade)  # Controla a velocidade da digitação
    print()  # Pula uma linha no final

def limpar_tela():
    if os.name == "nt":
        os.system("cls")  # Windows
    elif os.name == "posix":
        os.system("clear")  # Linux/macOS
    else:
        print("\033c", end="")  # ANSI Escape (pode funcionar no celular)




jogador = input("Dgite seu nome de jogador \n  ")
#criação e dados iniciais do Jogador
class player :
    def __init__(self,nome,level,dano,HP,inventario=None,dinheiro=0,xp=0):
        self.nome = nome
        self.level = int(level)
        self.dano = int(dano) 
        self.HP_max = int(HP)
        self.HP = self.HP_max                 
        self.xp = int(xp)
        self.inventario = []
        self.xp_necessario = self.level * 10
        self.dinheiro = float(dinheiro)
    
    def ganhar_dinheiro(self,valor):
        self.dinheiro += valor
        print(f"{NPC_01.nome} so tinha algumas moedas:💸 {valor}\n")


    


    def ganhar_xp(self,quantidade):
        self.xp += quantidade
        print (f"{self.nome} ganhou {quantidade} de Xp ")
        if self.xp >= self.xp_necessario :
           self.subir_de_nivel()
        

    def subir_de_nivel(self):
        self.level += 1
        self.xp -= self.xp_necessario
        self.xp_necessario = self.level * 2
        self.HP_max += 5
        self.HP += 5 
        self.dano +=  3
        self.HP = self.HP_max
        self.dinheiro += 5
        print (f'Parabens {self.nome} você subiu para o level {self.level} 🌟 \n agora seu  ❤️Hp é de {self.HP} e seu 💣dano sera de {self.dano}')

    #Função para usar a porção
    def usar_pocao(self):
        cura = 30  
        self.HP += cura
        if self.HP > self.HP_max:  # Impede que o HP ultrapasse o máximo
            self.HP = self.HP_max
        print(f"{self.nome} usou uma poção e recuperou {cura} HP! Agora tem {self.HP}/{self.HP_max} de HP.")
        
    
  
  

    def inicio(self):
        print(f"Bem Vindo {self.nome} ao  RPG Dungeons.Legends ✨")
        time.sleep(2)
        print("O Jogo e baseado em ataques por turnos 🛡️ \n Torne-se o mais forte e vença esse mundo...🎖️\n")
        time.sleep(3)

    def atacar(self,outro):
         dano_causado = self.dano 
         outro.HP -= dano_causado
         return dano_causado
    
    def item_ganho(self):
        loot = [

    ("Poção de Cura", 50),
    ("Nenhum Item", 30),
    ("Espada Enferrujada",20),
    ("Escudo Velho", 20),
    ("Amuleto da Sorte", 10)

] 
        item, pesos = zip(*loot)
        item_ganho = random.choices(item, weights=pesos, k=1) [0]
        print(f"Ao derrotar o NPC você achou {item_ganho}")
        self.inventario.append(item_ganho)
        if item_ganho == "Nenhum Item" :
            print(f"{NPC_01.nome} Não dropu nenhum item")
            return None
        else :
            return item_ganho  

#Creditos Finais
def creditos() :
    print_digitado("⚖️Criador/Diretor = Carlos Eduardo\n 👨‍💻Programador Backend = Carlos Eduardo") 
    print_digitado("📄Roteirista = Carlos Eduardo")
    print_digitado("Obrigado por jogar RPG.Legends✨ ......")
    print_digitado("Parte 2 Em Breve .................🩸👑")
 






#criação e dados iniciais do NPC        
class NPC :
    def __init__(self,nome,level,dano,HP,loot=None):
        self.nome = nome
        self.level = int(level)
        self.dano = int(dano)
        self.HP = int(HP)
        self.loot = loot

       
     
#Sistema de Ataque        
    def atacar(self,outro):
        dano_causado = self.dano 
        outro.HP -= dano_causado
        if outro.HP < 0 :
            outro.HP = 0
        return dano_causado
    
#COGNITAS BASE CODE    
nao = ["n","nao","não"]
sim = ["s","sim"]
loot_explicado = False
objeto = None
dica_01 = False
sair = False

#Dados Perfil 
jogador_01 = player(jogador ,"1","10","20")
NPC_01 = NPC("Vergasvam","1","8","15")

#Inicio do Game
jogador_01.inicio()
print(f"{jogador} Vamos começar sua primeira batalha 🏹")
time.sleep(2)
#Batalha -----------------=======================================================================================
def batalhar(player,npc):
    global loot_explicado
    npc.HP = 15
    while  player.HP > 0 and npc.HP > 0 :
        if player.HP <= 0 :
            print("Você não pode batalhar, use uma porção")
            break
        dano_jogador = player.atacar(npc)
        print(f"{player.nome} Atacou {npc.nome} e Causou {dano_jogador} de Dano  🔥")
        time.sleep(1.5)
        dano_npc = npc.atacar(player)
        print(f"{npc.nome} Atacou {player.nome} e Causou {dano_npc} de Dano  🗡️")
        time.sleep(2)
        if player.HP <= 0:
            player.HP = 0
            print(f"{player.nome} Foi Derrotado por {NPC_01.nome} 👾")
            break
        if npc.HP <= 0:
            npc.HP = 0
            limpar_tela()
            print(f"{npc.nome} Foi Derrotado {player.nome} Venceu a Batalha ☠️ ")
            time.sleep(1)
            jogador_01.ganhar_xp(2)
            jogador_01.item_ganho()
            jogador_01.ganhar_dinheiro(2)
            print ("Você pode usar o seu item verificando no menu de seu inventario")
            '''if objeto == "Poção de vida" :
                jogador_01.usar_pocao()
            elif objeto == "Espada Enferrujada" :
                jogador_01.dano += 2
            elif objeto == "Escudo Velho" :
                jogador_01.HP += 5
            elif objeto == "Amuleto da Sorte" :
                jogador_01.dano += 2 
                jogador_01.HP += 3'''
           
            
            if not loot_explicado:
                inf_loot = input(f"{player.nome}, gostaria de saber mais sobre os loots? 💰 (S/N) ").strip().lower()
                if inf_loot in sim:
                    limpar_tela()
                    print(f"Ao derrotar NPCs, você pode ganhar os seguintes loots:\n")
                    print("🧪 Poção de Cura (50% de chance) → Recupera 30 de HP")
                    print("🗡 Espada enferrujada (20% de chance) → Aumenta dano em +2")
                    print("🛡️ Escudo velho (20% de chance) → Aumenta HP em +5")
                    print("💍 Amuleto da sorte (10% de chance) → +2 dano, +3 HP, +5% chance de itens raros")
                    p = input ("Continuar ?").lower().strip()
                    while p in nao:
                        print("Ok, quando estiver pronto digite sim")
                        p = input("Continuar ?").lower().strip()
                        limpar_tela()
                    loot_explicado = True  
                

            
           
                
                
                                                                      
batalhar(jogador_01,NPC_01)

print(f"Otimo {jogador} Você derrotou seu primeiro NPC\n")
time.sleep(1)
print(f"Agora você tem acesso ao menu do RPG, Mais a frente voçê tera mais eventos no Menu ⚙️\n")

time.sleep(1.5)

#Função MENU
def Menu():
    global sair
    while True :
        Opções = input(f"{jogador} O que deseja Selecionar no menu ? \n (1) 📋 Perfil e Dados do Jogador \n (2) 🎒Inventario Do jogador \n (3) 🗂️ Historia do jogo \n (4)⚔️ Proxima Batalha \n (5) 🎈 Loja \n (6) 🔌 Sair do Menu \n\n")
        limpar_tela()
        if Opções == "1" :
            print(f"IDENTIDADE DO JOGADOR: 📖 {jogador}🕹️")
            print(" ")
            print(f"🎤 LEVEL = {jogador_01.level}")
            print("   ")
            print(f"❤️ HP = {jogador_01.HP}")    
            print("  ")       
            print(f" 💣 DANO = {jogador_01.dano}")
            print("     ")
            print(f"💸 DINHEIRO = {jogador_01.dinheiro}")
            print("   ")
            print(f"✨ XP = {jogador_01.xp}")
            print("  ")
            print (f"📈 XP NECESSARIO = {jogador_01.xp_necessario}")

            time.sleep(3)

        elif Opções == "2":
            limpar_tela()
            if jogador_01.inventario:
                print(f"Itens que Possui: 💰 {', '.join(jogador_01.inventario)}")
            else:
                print("Seu inventário está vazio. 💰")
            time.sleep(1.5)
        
 

              
        elif Opções == "3" :
            limpar_tela()
            print_digitado("Lord Varnok – O Tirano da Sede Eterna 🩸👑\n\n")
            print_digitado("Nas profundezas do Castelo Sombrio , onde vive Lorde Varnok, o Tirano da Sede Eterna .\n")
            print_digitado("Antigamente, Varnok era um senhor respeitado, um guerreiro da noite cujo poder rivalizava até mesmo os deuses esquecidos.")
            print_digitado("No entanto, sua obsessão em encontrar uma maneira de nunca mais sentir sede o levou a Um fracasso absoluto.")
            print_digitado("A experiência corrompeu seu corpo e sua mente, e seus seguidores mais leais foram os primeiros a sofrer as consequências.\n")
            print_digitado("Eles se transformaram nos Vergasvam.\n\n\n")
            print_digitado(" A Lenda do Tirano 🩸👑\n\n ")
            print_digitado("Historia Bloqueada. a Historia sera desbloqueada conforme o progresso no jogo......\n")
            print_digitado(".......................................................................................")
            b = input("Voltar para o Menu ?").lower().strip()
            while b in nao :
                print("Ok quando estiver pronto digite sim")
                b = input("Voltar para o Menu ?").lower().strip()
            time.sleep(1)
            

        elif Opções == '4' :
            global dica_01
            limpar_tela()
            if jogador_01.HP == 0:
                print("Voce esta sem vida use a porção na loja")
                continue

            batalhar(jogador_01,NPC_01)
            if not dica_01 :
                print("(Dica/Tutorial)👨‍💻 Ao final de cada batalha você ganha um numero expecifico de xp\n Ao chegar a quantidade especifica de XP você evolui para o proximo nivel")
                dica_01 = True
            c = input("Voltar para o Menu ? ⚙️ ").lower().strip()
            while c in nao :
                print("Ok quando estiver pronto digite sim")
                c = input("Voltar para o Menu ? ⚙️ ").lower().strip()
            time.sleep(2)
        
        elif Opções == "5" :
            print("Esta é a Loja onde você pode trocar suas moedas por itens\n Esta é a tabela de itens:")
            time.sleep(1.5)
            print(f"{jogador_01.nome}, seu saldo de moeda é: 💰 {jogador_01.dinheiro}")
            time.sleep(1)
            print("(1) ❤️ Poção de Cura = 4 Moedas\n(2) ✨ Poção de XP = 8 Moedas\n(3) 🗡️ Espada Enferrujada = 10 Moedas\n(4) 🛡️ Escudo Velho = 10 Moedas\n\n(5) 🎤 Informações sobre os Itens\n(6) ⚙️ Voltar Para o Menu\n")          
            time.sleep(1.5)
            while True :
                escolha = input("Escolha um item para comprar: ").strip()
                if escolha == "1":
                    if jogador_01.dinheiro >= 4:
                        jogador_01.inventario.append("Poção de Cura")
                        jogador_01.dinheiro -= 4
                        print("Você comprou uma ❤️ Poção de Cura!")
                    else:
                        print("Você não tem moedas suficientes! 💰")
            
                elif escolha == "2":
                    if jogador_01.dinheiro >= 8:
                        jogador_01.inventario.append("Poção de XP")
                        jogador_01.dinheiro -= 8
                        print("Você comprou uma ✨ Poção de XP!")
                    else:
                        print("Você não tem moedas suficientes! 💰")
            
                elif escolha == "3":
                    if jogador_01.dinheiro >= 10:
                        jogador_01.inventario.append("Espada Enferrujada")
                        jogador_01.dinheiro -= 10
                        print("Você comprou uma 🗡️ Espada Enferrujada!")
                    else:
                        print("Você não tem moedas suficientes! 💰")
            
                elif escolha == "4":
                    if jogador_01.dinheiro >= 10:
                        jogador_01.inventario.append("Escudo Velho")
                        jogador_01.dinheiro -= 10
                        print("Você comprou um 🛡️ Escudo Velho!")
                    else:
                        print("Você não tem moedas suficientes! 💰")
            
                elif escolha == "5":
                    limpar_tela()
                    print("🧪 Poção de Cura → Recupera 30 de HP")
                    print("✨ Poção de XP → Concede +8 de XP ")
                    print("🗡 Espada enferrujada → Aumenta dano em +2")
                    print("🛡️ Escudo velho → Aumenta HP em +5")
                    time.sleep(3.5)
            
                elif escolha == "6":
                    print("Voltando ao menu...")
                    break

                else:
                    print("Opção inválida! Escolha um número de 1 a 6.")
            
                time.sleep(2)


        elif Opções == "6":
            print("Saindo do menu...")
            time.sleep(1)
            sair = True
            break 
            

Menu()
if sair == True :
    creditos()

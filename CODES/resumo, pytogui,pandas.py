import pyautogui
import pandas
import pandas as pd
import sklearn
# faz automaçoes python: import pyautogui
#pressiona uma tecla especifica: pyautogui.press("")
#pyautogui.click("#clica na posição inserida","clicks = 2 define qntd de clicks")
#pyautogui.position("#rode o codigo pra marcar a posição de seu mouse")
#pyautogui.write("#escreva oq quer q o codigo escreva")
#pyautogui.scroll("#adiciona o numero de scroll ")

tabela = pd.read_csv("produtos.csv")
print(tabela)
#codigo = tabela.loc[linha,"codigo"]#mudar linha para o numero como 0 inicial,  codigo pelo nome exato na tABELA (nao veridico)
#for linha in tabela.index:
    #fazer a repetição e preencher dados    
#tabela = tabela.drop(columns="CostumerID")= tirar uma coluna da bas de dados index= 1 linha   
#.dropna() = faz tirar dados vazios
#display(tabela[nome da coluna].value_count())
#display(tabela[nome da coluna].value_count(normalize=True)) = mostrar porcentagem
#import plotly.express as px
#grafico = px.histogram(tabela,x = "idade",color = "cancelou")


#TRATAMENTO DA BASE PARA A IA
#comentar os que n sao numeros, e sao textos para a IA
#tornar txtos em numeros para a IA
from sklearn.preprocessing import LabelEncoder  
codificador1 = LabelEncoder()
#profissão   >>>>> Substitui nomes por numeros para ia (TODOS TEM Q SER IGUAIS STR min ou maiusculas)
#cientista -> 1
#pedreiro -> 2
#professo -> 3
tabela = ["profissão"] = codificador1.fit_transform(["profissão"]) #serve para codificar altomatico para a ia
#mix_credito:
codificador2 = LabelEncoder()
tabela["mix_credito"] = codificador2.fit_transform(["mix_credito"])
#CRIAR UMA CODIFICAÇÂO PARA CADA INFORMAÇÂO NECESSARIA
#comportamento_pagamento
codificador3 = LabelEncoder()
tabela["comportamento_pagamento"] = codificador3.fit_transform(["comportamento_pagamento"])
#AGORA SEPARAR AS INFOR PARA A IA
#Y = TODA A COLUNA OU IDEIA CENTRAL Q DESEJA PREVIÇÂO,Q A IA ACERTE
#x = tODO O RESTO Q DARA PARA A IA APRENDER PARA PODER PREVER E RESPONDER
y =tabela["score_credito"]
# x =tabela["mes","pagamento" etc,etc,etc] ou x=tabela.drop[columns = "score_credito"] faz tirar esse apenas ( mais tecnico e rapido)
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y test_size=0.3)

#arvore de decisão -> RandomForest = gostei mais, é mais logico
#vizinhos proximos -> KNN = soença, so escolhe qm é o culpado

#importar o modelo
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

#cria o modelo
modelo_arvoredecisão = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()
#treina o modelo
modelo_arvoredecisão.fit(x_treino,y_treino)
modelo_knn.fit(x_treino,y_treino)

#X1 PRA VER QUAL È MELHOR
#Testes
teste_arvore = modelo_arvoredecisão.predict(x_teste)
teste_knn = modelo_knn.predict(x_teste)
#precisão, acuracia
from sklearn.metrics import accuracy_score
#display ou print
print(accuracy_score(y_teste,teste_arvore))
print(accuracy_score(y_teste,teste_knn))
#ganhador né pai
#apos isso passar usa a melhor caso tenha outro arquivo use o msm coamndos, mude apenas o nome do arquivo


#SITE, SISTEMA
import streamlit as st
st.write("Mensagem de bot")
mensagem_usurio = st.chat_input("escreva aqui")
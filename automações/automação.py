#bibliotecas
import time
import pyautogui
import pandas

#1 Passo: abrir o chrome

pyautogui.press("win")
time.sleep(3)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2.5)

#2 Passo: entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) 

#3 Passo: logar no site
pyautogui.click(x=729, y=366)
pyautogui.write("Caerlos234@.com.br")
pyautogui.press("tab")
pyautogui.write("Carlos4340s")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.press("enter")

#4 passo: preencher as informações
time.sleep(1.6)
print(pyautogui.position())


#importar informações
tabela = pandas.read_csv("produtos.csv")

#para cada linha na tabela um codigo diferente
for linha in tabela.index:
    pyautogui.click(x=635, y=249)
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    time.sleep(0.8)

    pyautogui.press("tab")
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    time.sleep(0.8)

    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    time.sleep(0.8)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    time.sleep(0.8)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    time.sleep(0.8)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    time.sleep(0.8)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
        time.sleep(0.8)

    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(10000)

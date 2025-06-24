#bibliotecas
import time
import pyautogui
import pandas

#1 Passo: abrir o chrome
while True:
    pyautogui.press("win")
    time.sleep(3.5)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2.8)

    #2 Passo: entrar no site
    pyautogui.write("https://discord.com/channels/1325923952652062720/1329959998935142521")
    pyautogui.press("enter")
    time.sleep(16)
    print(pyautogui.position())
    pyautogui.click(x=504, y=749)
    time.sleep(1.8)
    break

while True:
    time.sleep(3660)
    pyautogui.click(x=507, y=601)
    time.sleep(7)



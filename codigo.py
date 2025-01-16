#Passos: Abrir o sistema, fazer login, importar base de dados, cadastrar produtos,
# e repetir o passo de cadastro até o fim dos dados.

#pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5 #delay em segundos para todos os comandos pyautogui

# pyautogui.click  #Clicar
# pyautogui.press  #Precionar tecla
# pyautogui.write  #Escrever
# pyautogui.hotkey #Atalhos:
# pyautogui.hotkey("alt","tab") #("ctrl","shift","n")Mouse  1

pyautogui.press("win")
pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) #delay de execução apenas neste ponto, em segundos

pyautogui.click(x=883, y=476) # (x=-199, y=-1692, clicks=2) (x=-199, y=-1692, button=right) #auxiliarClick.py
pyautogui.write("python3@gmail.com")

pyautogui.press("tab")
pyautogui.write("senhapyautogui")

pyautogui.press("tab")
pyautogui.press("enter")

#-----------------------------------------------------------------------------------------------------------------#

import pandas

tabela = pandas.read_csv("produtos.csv")

time.sleep(2)
#for linha in tabela.collumns:
for linha in tabela.index: #Para cara linda da tabela faça isso:
    #linha++
    
    pyautogui.click(x=674, y=330)
    
    codigo = tabela.loc[linha,"codigo"] # [linha,coluna]
    pyautogui.write(str(codigo)) #str() converte para string
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000) #PgUp


# Step by step
# 1: Enter on application 
    
import pyautogui # type: ignore
import time
import os
from dotenv import load_dotenv

# pyautogui.write -> write a tpyautogui.press -> press 1 key
# pyautogui.click -> click some point of screen
# pyautogui.hotkey -> combination of keys
pyautogui.PAUSE = 0.3

# Load environment variables from .env file
load_dotenv()

# Access environment variables
application_url = os.getenv('APPLICATION_URL')

# open browser (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# enter the link 
pyautogui.write(application_url)
pyautogui.press("enter")
time.sleep(3)

# 2:  Login

pyautogui.click(x=698, y=437)
# type your email
pyautogui.write("someemail@gmail.com")
pyautogui.press("tab") # to next field
pyautogui.write("sua senha")

pyautogui.click(x=955, y=638) # click on login button
time.sleep(3)

# 3: Import products to register
import pandas as pd # type: ignore

tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4: Register a product
for linha in tabela.index:
    pyautogui.click(x=653, y=294)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # register the product (send button)
    # scroll up
    pyautogui.scroll(5000)
    # 5: Repeat until the end

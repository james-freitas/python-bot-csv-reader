import pyautogui # type: ignore
import webbrowser
import time
import pandas as pd # type: ignore
import os
from dotenv import load_dotenv

# 1. Configuration
# Waiting time between commands
pyautogui.PAUSE = 0.2

# Load environment variables from .env file
load_dotenv()

# Access environment variables
application_url = os.getenv('APPLICATION_URL')

webbrowser.open_new(application_url)
time.sleep(3)

# 2. Login on application
pyautogui.click(x=698, y=437)
pyautogui.write("somebody@gmail.com")
pyautogui.press("tab") # type tab to pass to the password field

pyautogui.write("some password")
pyautogui.press("tab") 
pyautogui.press("enter") # confirm login

time.sleep(3)

# 3. Read csv table
table = pd.read_csv("produtos_small.csv")
print(table)

# Passo 4: Register a product
for line in table.index:

    # click on code field
    pyautogui.click(x=759, y=325)

    # get from table table the field value to fill in the form
    codigo = table.loc[line, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = table.loc[line, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = table.loc[line, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # fill category field
    categoria = table.loc[line, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # fill unitary price field
    preco_unitario = table.loc[line, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # fill cost field
    custo = table.loc[line, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # fill obs field
    obs = table.loc[line, "obs"]
    if not pd.isna(obs):
      pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.press("tab")

    # click on send button
    pyautogui.press("enter")

    # scroll up
    pyautogui.scroll(5000)


# CSV Bot reader and form filler
Bot that reads CSV and inputs data on application form

## ✔️ Requirements
- Python 2 or greater

## 🍔 Stack
- Python

## 🐧 How to run locally on Ubuntu

1. Install the dependencies
```shell
pip install pyautogui
pip install webbrowser
pip install pandas
pip install python-dotenv
```
2. Create `.env` file and add the link of your application.  You will have to adapt the code
to your application.
```shell
APPLICATION_URL=https://dlp.hashtagtreinamentos.com/python/intensivao/login
```

3. Execute the application 
```shell
## run the application
python3 bot_ubuntu.py       
```
## 🪟 How to run locally on Windows

1. Install the dependencies
```shell
pip install pyautogui
pip install pandas
pip install python-dotenv
```
2. Create `.env` file and add the link of your application.  You will have to adapt the code
to your application.
```shell
APPLICATION_URL=https://dlp.hashtagtreinamentos.com/python/intensivao/login
```

3. Execute the application 
```shell
## run the application
python3 bot_windows.py       
```

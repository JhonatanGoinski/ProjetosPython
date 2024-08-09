import yfinance 
import pyautogui
import pyperclip
import webbrowser
import time

# Etapa 01
ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# Fim - Etapa 01


# Etapa 02

destinatario = "jhonatangoinski@gmail.com"
# --------
assunto = "Análise do Projeto - Python"
# --------
mensagem = f"""

Prezados gestor, 

Seguem as análises solicitadas da ação {ticker};

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Att!

"""

# abrir o navegador e ir para o gmail. 
webbrowser.open("www.gmail.com")
time.sleep(3)

# Configurando uma pausa de 3 seg
pyautogui.PAUSE = 3 

# Clicar no botão escrever. 
pyautogui.click(x=46, y=273)

# Digitar o e-mail dos destinatário e teclar tab
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar o assunto do e-mail
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar a assunto do e-mail
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão enviar. 
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

# fechar e-mail 
pyautogui.hotkey("ctrl", "f4")

print("E-mail enviado com sucesso!")

# Fim - Etapa 02
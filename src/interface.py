import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import time
from api import run_api, logs  # Importando a função da API

# Criando a interface
janela = tk.Tk()
janela.title("Monitor da API Flask")
janela.geometry("500x400")

# Criar um campo de texto grande para os logs
campo_logs = scrolledtext.ScrolledText(janela, width=60, height=15)
campo_logs.pack(pady=10)

# Status da conexão
status_label = tk.Label(janela, text="Checking...", font=("Arial", 12, "bold"))
status_label.pack()

# Função para atualizar os logs
def atualizar_logs():
    while True:
        campo_logs.delete("1.0", tk.END)
        for log in logs:
            campo_logs.insert(tk.END, log + "\n")
        campo_logs.yview(tk.END)
        time.sleep(1)

# Função para verificar o status da API
def verificar_conexao():
    while True:
        try:
            response = requests.get("http://127.0.0.1:5000/")
            if response.status_code == 200:
                status_label.config(text="Connection OK", fg="green")
            else:
                status_label.config(text="Connection Down", fg="red")
        except:
            status_label.config(text="Connection Down", fg="red")
        time.sleep(2)

# Rodar a API em uma thread separada
thread_api = threading.Thread(target=run_api, daemon=True)
thread_api.start()

# Rodar as funções de atualização em threads separadas
thread_logs = threading.Thread(target=atualizar_logs, daemon=True)
thread_logs.start()

thread_status = threading.Thread(target=verificar_conexao, daemon=True)
thread_status.start()

# Rodar a interface
janela.mainloop()

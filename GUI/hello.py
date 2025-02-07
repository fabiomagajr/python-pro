import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Tkinter com Tema")
janela.geometry("300x200")

# Criar um estilo
style = ttk.Style()
style.theme_use("clam")  # Outros temas: "alt", "default", "classic"

# Criar um botão estilizado
botao = ttk.Button(janela, text="Botão Estilizado")
botao.pack(pady=20)

janela.mainloop()

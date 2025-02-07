import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Tkinter Bonito")
janela.geometry("300x200")

# Aplicar um tema do ttkbootstrap
style = Style(theme="cyborg")  # Outros: "superhero", "flatly", "minty", etc.

# Criar um botão estilizado
botao = ttk.Button(janela, text="Clique Aqui", bootstyle="primary", command=lambda: messagebox.showinfo("Information","Informative message"))
botao.pack(pady=20)

janela.mainloop()

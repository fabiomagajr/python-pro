import tkinter as tk

janela = tk.Tk()
janela.title("Interface Organizada")
janela.geometry("300x200")

# Criando um frame para os elementos
frame = tk.Frame(janela)
frame.pack(pady=20)

# Adicionando widgets dentro do frame
label = tk.Label(frame, text="Nome:")
label.grid(row=0, column=0, padx=5, pady=5)

entrada = tk.Entry(frame)
entrada.grid(row=0, column=1, padx=5, pady=5)

botao = tk.Button(frame, text="OK", command=lambda: print("Nome digitado:", entrada.get()))
botao.grid(row=1, column=0, columnspan=2, pady=5)

janela.mainloop()

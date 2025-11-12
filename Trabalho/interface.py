import tkinter as tk

janela = tk.Tk()
janela.title("Busca feriado")

janela.geometry("500x200")

label_nome = tk.Label(janela, text="Digite o caminho do PDF:")
label_nome.grid(row=0, column=2, pady=5)

caixa_texto = tk.Entry(janela, width=40)
caixa_texto.grid(row=1, column=2, padx=5, pady=5)



botao = tk.Button(janela, text="Obter Texto")
botao.grid(row=1, column=4, padx=5)

janela.mainloop()

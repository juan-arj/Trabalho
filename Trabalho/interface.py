import tkinter as tk
import PyPDF2
import requests

url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    print(reader.pages[0].extract_text())
    

janela = tk.Tk()
janela.title("Busca feriado")

janela.geometry("500x200")


caminho_pdf_var = tk.StringVar()


label_nome = tk.Label(janela, text="Digite o caminho do PDF:")
label_nome.grid(row=0, column=2, pady=5)

caixa_texto = tk.Entry(janela, textvariable=caminho_pdf_var, width=40)
caixa_texto.grid(row=1, column=2, padx=5, pady=5)


botao = tk.Button(janela, text="Obter Texto", command=lambda: Get_text_from_PDFfiles_usingPyPDF2(caminho_pdf_var.get())
)
botao.grid(row=1, column=4, padx=5)



janela.mainloop()

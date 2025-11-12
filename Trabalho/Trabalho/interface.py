import tkinter as tk
import PyPDF2
import requests
feriados = ""
for i in ["2025", "2026"]:
    url = "https://date.nager.at/api/v3/PublicHolidays/"+i+"/BR"

    payload = {}
    headers = {
      'accept': 'application/json',
      'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
      }

    response = requests.request("GET", url, headers=headers, data=payload)

    feriados = feriados + response.text


def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    texto = reader.pages[0].extract_text()
    texto_limpo = texto.strip()
    texto_dividido = texto_limpo.split('\n')
    print(texto_dividido)

    for palavra in texto_dividido:
        if palavra.strip() in feriados:
            print(palavra)
            
    

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

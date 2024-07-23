import pyqrcode
import tkinter as tk
from ttkthemes import ThemedTk
import os


def verificao_nome(base_name, extension_name):
    counter = 1
    file_name = f"{base_name}.{extension_name}"
    while os.path.exists(file_name):
        file_name = f"{base_name}_{counter}.{extension_name}"
        counter += 1
    return file_name

def gerar_qrcode():
    qr = space.get()
    url = pyqrcode.create(qr)
    file_name = verificao_nome("qr", "png")
    url.png(file_name, scale=8)
    resultado_label.config(text="QrCode gerado com sucesso")

janela = tk.Tk()
janela.title("Gerador de QrCode")
janela.geometry("300x250")
label = tk.Label(janela, text="Digite a Url", font=("Arial", 18))
label.pack(pady=20)
space = tk.Entry(janela, font=("Arial", 14))
space.pack(pady=10)

botao = tk.Button(janela, text="Gerar QrCode", command=gerar_qrcode)
botao.pack(pady=10)

resultado_label = tk.Label(janela, text="", font=("Arial", 16))
resultado_label.pack(pady=10)

janela.mainloop()
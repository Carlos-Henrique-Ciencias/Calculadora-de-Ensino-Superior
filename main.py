import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

import fisica
import quimica
import estatistica
import calculos

def open_fisica():
    fisica.create_window()

def open_quimica():
    quimica.create_window()

def open_estatistica():
    estatistica.create_window()

def open_calculos():
    calculos.create_window()

root = tk.Tk()
root.title("Principal")
root.geometry("500x500")

titulo = tk.Label(root, text="Calculadora Superyor", font=("Arial", 24, "bold"), fg="#8b82eb", bg="#000")
titulo.place(relx=0.5, y=20, anchor="n")

# Ajustando o caminho da imagem
if getattr(sys, 'frozen', False):
    # O script está rodando como um executável
    base_path = sys._MEIPASS
else:
    # O script está rodando normalmente
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, "DALL·E 2023-12-23 16.03.42 - Create a full-screen design featuring symbols for mathematics, physics, and statistics, with the symbols filling the entire space without any margins.png")
background_image = Image.open(image_path)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()

estilo_botao = {"font": ("Arial", 16, "bold"), "fg": "white", "bg": "#2400ff"}

btn_fisica = tk.Button(root, text="Física", command=open_fisica, **estilo_botao)
btn_fisica.place(x=291, y=168, width=150, height=100)

btn_quimica = tk.Button(root, text="Química", command=open_quimica, **estilo_botao)
btn_quimica.place(x=61, y=324, width=150, height=100)

btn_estatistica = tk.Button(root, text="Estatística", command=open_estatistica, **estilo_botao)
btn_estatistica.place(x=291, y=324, width=150, height=100)

btn_calculos = tk.Button(root, text="Cálculos", command=open_calculos, **estilo_botao)
btn_calculos.place(x=61, y=168, width=150, height=100)

root.mainloop()

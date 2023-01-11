import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

def abrirNombre():
    filetypes = (
        ('png files', '*.png'),
        ('All files', '.')
    )

    filename = fd.askopenfilename(
        title='Elegí una imagen',
        initialdir='/',
        filetypes=filetypes)

    return filename

def abrirImagen(root):
    aux = abrirNombre()
    img = ImageTk.PhotoImage(Image.open(aux))
    imglabel = Label(root, image=img)
    imglabel.grid(row=3, column=1)
    imglabel.image = img


def ventanaPrincipal():
    root = tk.Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Cargue un archivo").grid(column=0, row=0)
    ttk.Button(frm, text="Cargar", command=abrirImagen(root)).grid(column=1,row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()
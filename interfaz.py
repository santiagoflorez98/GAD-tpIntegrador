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

def abrirImagen(var):
    aux = abrirNombre()
    img = ImageTk.PhotoImage(Image.open(aux))
    imglabel = Label(image=img)
    imglabel.grid(row=0,column=5)
    imglabel.image = img
    var.set(1)
    return var


def consultarImagen(var2):
    image1 = Image.open("C:/Users/Analiz/Desktop/mati/TestGad/70.png")
    resize_image1 = image1.resize((100, 100))
    img1 =ImageTk.PhotoImage(resize_image1)
    img1label= Label(image=img1)
    img1label.grid(row=3,column=0)
    img1label.image=img1


    image2 = Image.open("C:/Users/Analiz/Desktop/mati/TestGad/71.png")
    resize_image2= image2.resize((100, 100))
    img2 =ImageTk.PhotoImage(resize_image2)
    img2label= Label(image=img2)
    img2label.grid(row=4,column=0)
    img2label.image=img2

    image3 = Image.open("C:/Users/Analiz/Desktop/mati/TestGad/72.png")
    resize_image3 = image3.resize((100, 100))
    img3 = ImageTk.PhotoImage(resize_image3)
    img3label= Label(image=img3)
    img3label.grid(row=5,column=0)
    img3label.image=img3

    image4 = Image.open("C:/Users/Analiz/Desktop/mati/TestGad/273.png")
    resize_image4 = image4.resize((100, 100))
    img4 = ImageTk.PhotoImage(resize_image4)
    img4label= Label(image=img4)
    img4label.grid(row=6,column=0)
    img4label.image=img4

    image5 = Image.open("C:/Users/Analiz/Desktop/mati/TestGad/250.png")
    resize_image5 = image5.resize((100, 100))
    img5 = ImageTk.PhotoImage(resize_image5)
    img5label= Label(image=img5)
    img5label.grid(row=7,column=0)
    img5label.image=img5

    var2.set(1);

def ventanaPrincipal():
    root = tk.Tk()
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    ttk.Label(frm, text="Cargue una imagen").grid(pady=5,row=0,column=0)
    var = tk.IntVar()
    var2 = tk.IntVar()
    quitButton= ttk.Button(frm, text="Quit", command=root.destroy)
    quitButton.grid(pady=5,row=0,column=2)
    cargarButton = tk.Button(frm, text="Cargar", command=lambda:abrirImagen(var))
    cargarButton.grid(pady=5,row=0,column=1)
    lb1= ttk.Label(frm, text='Esperando a que se seleccione imagen')
    lb1.grid(pady=5,row=1,column=4)
    cargarButton.wait_variable(var)
    lb1.grid_remove()
    lb2= ttk.Label(frm, text='Imagen seleccionada: ')
    lb2.grid(pady=5,row=1,column=4)
    consultaButton=ttk.Button(frm, text='Consultar', command=lambda:consultarImagen(var2))
    consultaButton.grid(pady=5,row=0,column=3)
    lb3= ttk.Label(frm, text='Esperando a que se realize una consulta')
    lb3.grid(pady=5,row=2,column=0)
    consultaButton.wait_variable(var2)
    lb3.grid_remove()
    lb4= ttk.Label(frm, text='Consulta realizada, aguarde resultados')
    lb4.grid(pady=5,row=2,column=0)
    root.mainloop()


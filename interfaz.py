import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

import controlador

ruta=''
radio=''
def abrirNombre():
    filetypes = (
        ('png files', '*.png'),
        ('All files', '.')
    )

    filename = fd.askopenfilename(
        title='Elegí una imagen',
        initialdir='/',
        filetypes=filetypes)
    global ruta
    ruta=filename
    return filename

def abrirImagen(var):
    aux = abrirNombre()
    img = ImageTk.PhotoImage(Image.open(aux))
    imglabel = Label(image=img)
    imglabel.grid(row=0,column=5)
    imglabel.image = img
    var.set(1)
    return var,aux


def consultarImagen(var2):
    resultadoConsulta=controlador.consulta(radio,ruta);
    for idx,r in enumerate(resultadoConsulta):
        image = Image.open(r[2])
        resize_image = image.resize((100, 100))
        img1 = ImageTk.PhotoImage(resize_image)
        img1label = Label(image=img1)
        var = StringVar()
        distancelabel = Label(textvariable=var)
        var.set('Distancia: '+ str(r[1]))
        if (idx+3>7):
            img1label.grid(row=idx-3, column=6)
            distancelabel.grid(row=idx-3, column=7)
        else:
            img1label.grid(row=idx+2, column=4)
            distancelabel.grid(row=idx + 2, column=5)

        img1label.image = img1

    var2.set(1);

def confirmarRadio(rad,var3):
    global radio
    radio = rad.get()
    var3.set(1)

def ventanaPrincipal():
    root = tk.Tk()
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text="Cargue una imagen").grid(pady=5,row=0,column=0)
    var = tk.IntVar()
    var2 = tk.IntVar()
    var3= tk.IntVar()
    radio=tk.StringVar()
    quitButton= ttk.Button(frm, text="Quit", command=root.destroy)
    quitButton.grid(pady=5,row=0,column=2)
    cargarButton = tk.Button(frm, text="Cargar", command=lambda:abrirImagen(var))
    cargarButton.grid(pady=5,row=0,column=1)
    lbradio=ttk.Label(frm,text='Ingrese el radio para su consulta')
    lbradio.grid(row=2,column=0)
    entryradio=ttk.Entry(frm, textvariable=radio)
    entryradio.grid(row=2,column=1)
    entrybutton = ttk.Button(frm, text="Confirmar radio", command=lambda:confirmarRadio(radio,var3))
    entrybutton.grid(row=2, column=5)
    entrybutton.wait_variable(var3)
    lbradio.grid_remove()
    lbradio=ttk.Label(frm,text='¡Su radio es: ' + radio.get())
    lbradio.grid(row=2, column=0)

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
    lb4= ttk.Label(frm, text='¡Consulta realizada!')
    lb4.grid(pady=5,row=2,column=0)
    root.mainloop()


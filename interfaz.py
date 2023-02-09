import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.simpledialog import askfloat

from PIL import Image, ImageTk

import controlador

def abrirNombre():
    filetypes = (
        ('png files', '*.png'),
        ('All files', '.')
    )

    filename = fd.askopenfilename(
        title='Elegí una imagen',
        initialdir='/',
        filetypes=filetypes)
    global g_ruta
    g_ruta=filename
    return filename

def abrirImagen(ruta):
    aux = abrirNombre()
    ruta.set(aux)

    return ruta


def consultarImagen(radio,ruta):

    resultadoConsulta=controlador.consulta(radio.get(),ruta.get());
    for idx,r in enumerate(resultadoConsulta):
        image = Image.open(r[2])
        resize_image = image.resize((100, 100))
        img1 = ImageTk.PhotoImage(resize_image)
        img1label = Label(image=img1)
        var = StringVar()
        distancelabel = Label(textvariable=var)
        var.set(str(idx + 1) + ' - Distancia: '+ str(r[1]) +'\n Ruta: '+ str(r[2]))
        if (idx%2 == 0 ):
            img1label.grid(row=idx+2, column=0)
            distancelabel.grid(row=idx+2, column=1)
        else:
            img1label.grid(row=idx+1, column=2)
            distancelabel.grid(row=idx + 1, column=3)

        img1label.image = img1

def ingresarRadio(radio):
    radio_p=askfloat("","Ingrese su radio")
    radio.set(radio_p)
    return radio



def generar_labels(container,ruta,radio):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=5,pad=30)

    # Imagen label
    rutaActual = ruta.get()
    rutaSegmentada=rutaActual.split('/')
    ttk.Label(frame, text='Imagen:').grid(column=0, row=0, sticky=tk.N)
    if rutaActual== '':
        img_l= ttk.Label(frame,text='No hay imagen seleccionada')
        img_l.grid(column=1,row=0, sticky=tk.N)
    else:
        img_l=ttk.Label(frame, text=str(next(reversed(rutaSegmentada))))
        img_l.grid(column=1, row=0, sticky=tk.N)
        img = Image.open(ruta.get())
        resize_image= img.resize((200,200))
        img_r= ImageTk.PhotoImage(resize_image)
        imglabel = Label(image=img_r)
        imglabel.grid(row=0,column=3, sticky=tk.N,columnspan=4)
        imglabel.image = img_r

    # Radio label 2
    radioActual=radio.get()
    ttk.Label(frame, text='Radio:').grid(column=0, row=1, sticky=tk.N,)
    if (radioActual==''):
        radio_l = ttk.Label(frame,text='No ha sido ingresado el radio')
        radio_l.grid(column=1,row=1, sticky=tk.N)
    else:
        radio_l= ttk.Label(frame, text=radio.get())
        radio_l.grid(column=1, row=1, sticky=tk.N)

    #Espacio vacio
    ttk.Label(frame, text='').grid(column=0, row=2, sticky=tk.W)
    ttk.Label(frame, text='').grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def generar_botones(container,ruta,radio):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Cargar imagen',width=15,command=lambda:abrirImagen(ruta)).grid(column=0, row=0)
    ttk.Button(frame, text='Ingresar Radio',width=15, command=lambda:ingresarRadio(radio)).grid(column=0, row=1)
    ttk.Button(frame, text='Consultar',width=15, command=lambda:consultarImagen(ruta,radio)).grid(column=0, row=2)
    ttk.Button(frame, text='Quit',width=15,command=container.destroy).grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame,ruta,radio


def ventanaPrincipal():
    root = tk.Tk()
    root.title('Busqueda por similitud de escudos de futbol')
    root.resizable(0, 0)

    try:
        # solo windows (remover boton de minimizar/maximizar)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Funcion no disponible en tu sistema')

    ruta=tk.StringVar()
    ruta.set('')
    radio=tk.StringVar()
    radio.set('')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    #Generando Labels vacios
    labels_frame = generar_labels(root,ruta,radio)
    labels_frame.grid(column=0, row=0)

    botones_frame = generar_botones(root,ruta,radio)
    botones_frame[0].grid(column=1, row=0)



    #Esperando que se ingrese radio y ruta
    root.wait_variable(ruta)
    labels_frame.destroy()
    labels_frame=generar_labels(root,ruta,radio)
    labels_frame.grid(column=0, row=0)

    root.wait_variable(radio)
    labels_frame.destroy()
    labels_frame=generar_labels(root,ruta,radio)
    labels_frame.grid(column=0,row=0)







    root.mainloop()


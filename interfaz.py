import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

import controlador

g_ruta=''
g_radio=''
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
    img = ImageTk.PhotoImage(Image.open(aux))
    imglabel = Label(image=img)
    imglabel.grid(row=0,column=3)
    imglabel.image = img
    ruta.set(aux)

    return ruta


def consultarImagen():
    resultadoConsulta=controlador.consulta(g_radio,g_ruta);
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

def confirmarRadio():
    return 0


def generar_labels(container,ruta,radio):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=5)

    # Imagen
    ttk.Label(frame, text='Imagen:').grid(column=0, row=0, sticky=tk.N,)
    img= ttk.Label(frame,text='No hay imagen seleccionada')
    img.grid(column=1,row=0, sticky=tk.N)
    if(ruta.get()!=''):
        img.grid_remove()
        img=ttk.Label(frame, text=ruta.get())
        img.grid(column=1, row=0, sticky=tk.N)


    # Radio
    ttk.Label(frame, text='Ingrese su radio y confirme:').grid(column=0, row=1, sticky=tk.W)
    radio = ttk.Entry(frame, width=30)
    radio.grid(column=1, row=1, sticky=tk.W)

    # Radio2
    ttk.Label(frame, text='Radio:').grid(column=0, row=2, sticky=tk.N,)
    if (g_radio==''):
        ttk.Label(frame,text='No ha sido ingresado el radio').grid(column=1,row=2, sticky=tk.N)
    else:
        ttk.Label(frame, text=g_radio).grid(column=1, row=0, sticky=tk.N)

    #Espacio vacio
    #ttk.Label(frame, text='').grid(column=0, row=2, sticky=tk.W)
    ttk.Label(frame, text='').grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def generar_botones(container,ruta,radio):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Cargar imagen',width=15,command=lambda:abrirImagen(ruta)).grid(column=0, row=0)
    ttk.Button(frame, text='Confirmar Radio',width=15, command=confirmarRadio).grid(column=0, row=1)
    ttk.Button(frame, text='Consultar',width=15, command=consultarImagen).grid(column=0, row=2)
    ttk.Button(frame, text='Quit',width=15,command=container.destroy).grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame,ruta,radio


def ventanaPrincipal():
    root = tk.Tk()
    root.title('Busqueda por similitud de escudos de futbol')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    ruta=tk.StringVar()
    ruta.set('')
    radio=tk.StringVar()
    radio.set('')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    labels_frame = generar_labels(root,ruta,radio)
    labels_frame.grid(column=0, row=0)

    botones_frame = generar_botones(root,ruta,radio)
    botones_frame[0].grid(column=1, row=0)
    root.wait_variable(ruta)
    print('ruta es '+ruta.get())
    labels_frame=generar_labels(root,ruta,radio)
    labels_frame.grid(column=0, row=0)


    root.mainloop()


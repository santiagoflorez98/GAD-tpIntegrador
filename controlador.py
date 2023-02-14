from pathlib import Path
from PIL import Image
import vectorizacion as vec
import database as db
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
def cargarEnDb():
    base = db.database()
    directory = config['DEFAULT']['IMAGENES']
    files = Path(directory).glob('*')
    for file in files:
        act_vec = vec.get_vector(Image.open(file).convert('RGB'))
        base.consulta_cargar(act_vec.tolist(),str(file))
    base.desconectar_db()

def consulta(ruta, radio):
    base= db.database()
    vect= vec.get_vector(Image.open(ruta).convert('RGB'))
    resultado=base.consulta_db(vect.tolist(),radio)
    base.desconectar_db()
    return resultado

def PruebaPesos():
    vect= vec.get_vector(Image.open(config['DEFAULT']['COPIAS'] + '/47.png').convert('RGB'))
    print(vect)
def contarCoincidencias(ruta):
    coincidencia = False
    lugarCoincidencia = -1
    res = consulta(ruta,0.3)
    tamañoRes = len(res)
    i = 0
    resultadoEsperado=str(ruta).split('_')[1]
    while ((i < 5 | i < tamañoRes) & (~coincidencia)):
        if (res[i][2].split('\\')[-1] == resultadoEsperado):
            coincidencia = True
            lugarCoincidencia = i
        i += 1
    return coincidencia, lugarCoincidencia

def consultas():
    contadorPrimeraPosicion = 0
    contadorCoincidencia = 0
    directory = config['DEFAULT']['COPIAS']
    files = Path(directory).glob('*')
    for i in files:
        res = contarCoincidencias(i)
        if (res[0]):
            contadorCoincidencia += 1
            if (res[1] == 0):
                contadorPrimeraPosicion += 1
            print(f'Hubo coincidencia en la posicion {res[1]} para la imagen {i}')
        else:
            print(f'No hubo coincidencias para la imagen {i}')
    porcentajePrimeraPosicion = contadorPrimeraPosicion / 50 * 100
    porcentajeCoincidencias = contadorCoincidencia / 50 * 100
    return contadorPrimeraPosicion,contadorCoincidencia, porcentajePrimeraPosicion, porcentajeCoincidencias
from pathlib import Path
from PIL import Image
import vectorize as vec
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

def contarCoincidencias(rutaOr, rutaCopia):
    primeraCoincidencia = False
    coincidencias = 0
    resOriginal = consulta(rutaOr,0.3)
    resCopia = consulta(rutaCopia,0.3)
    tamañoOriginal = len(resOriginal)
    tamañoCopia = len(resCopia)
    i = 0
    while (i < 5 | i < tamañoOriginal):
        j = 0
        while ((resOriginal[i][2] != resCopia[j][2]) & (j<4 | j<tamañoCopia)):
            j += 1
        if resOriginal[i][2] == resCopia[j][2]:
            coincidencias +=1
            if (i == 0):
                primeraCoincidencia = True
        i += 1
    return coincidencias,primeraCoincidencia

def consultas():
    acumuladorCoincidencias = 0
    contadorPrimeraCoincidencia = 0
    for i in range(1,51):
        res = contarCoincidencias(f'C:/Users/santi/OneDrive/Escritorio/consultasOriginales/{i}.png'
                            ,f'C:/Users/santi/OneDrive/Escritorio/consultasOtras/{i}.png')
        print (f'Imagen {i} - numero de coincidencias: {res[0]}')
        acumuladorCoincidencias += res[0]
        if (res[1]):
            print('hubo coincidencia en la primera imagen')
            contadorPrimeraCoincidencia +=1
    porcentajePrimeraCoincidencia = (contadorPrimeraCoincidencia / 50) * 100
    porcentajeCoincidencias = (acumuladorCoincidencias / 250) * 100
    return porcentajeCoincidencias,porcentajePrimeraCoincidencia
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
    resOriginal = consulta(rutaOr,1)
    resCopia = consulta(rutaCopia,1)
    for i in range(0,5):
        j = 0
        while ((resOriginal[i][2] != resCopia[j][2]) & (j<4)):
            j += 1
        if resOriginal[i][2] == resCopia[j][2]:
            coincidencias +=1
            if (i == 0):
                primeraCoincidencia = True
    return coincidencias,primeraCoincidencia

def consultas():
    for i in range(1,51):
        res = contarCoincidencias(f'C:/Users/santi/OneDrive/Escritorio/consultasOriginales/{i}.png'
                            ,f'C:/Users/santi/OneDrive/Escritorio/consultasOtras/{i}.png')
        print (f'Imagen {i} - numero de coincidencias: {res[0]}')
        if (res[1]): print('hubo coincidencia en la primera imagen')
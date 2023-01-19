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

def consulta(radio, ruta):
    base= db.database()
    vect= vec.get_vector(Image.open(ruta).convert('RGB'))
    resultado=base.consulta_db(vect.tolist(),radio)
    base.desconectar_db()
    return resultado
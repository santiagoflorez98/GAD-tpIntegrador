from PIL import Image
from pathlib import Path
import vectorize as vec
import database as db
import interfaz
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

#interfaz.ventanaPrincipal()
cargarEnDb()
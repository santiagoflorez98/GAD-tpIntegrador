from PIL import Image
from pathlib import Path
import vectorize as vec
import database as db
import interfaz
def cargarEnDb():
    base = db.database()
    directory = 'C:/Users/santi/OneDrive/Escritorio/xd'
    files = Path(directory).glob('*')
    for file in files:
        act_vec = vec.get_vector(Image.open(file).convert('RGB'))
        base.consulta_cargar(act_vec.tolist(),str(file))
    base.desconectar_db()

#interfaz.ventanaPrincipal()
cargarEnDb()
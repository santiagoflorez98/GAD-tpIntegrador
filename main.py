from PIL import Image
from pathlib import Path
import vectorize as vec
import database as db
import interfaz
def cargarEnDb():
    directory = 'C:/Users/santi/OneDrive/Escritorio/TestGADRed'
    files = Path(directory).glob('*')
    for file in files:
        act_vec = vec.get_vector(Image.open(file).convert('RGB'))
        db.insertar_imagen(act_vec.tolist(),str(file))

interfaz.ventanaPrincipal()
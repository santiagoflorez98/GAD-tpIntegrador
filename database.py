import psycopg2
def insertar_imagen(vec,ruta):
    conn = psycopg2.connect("dbname= TPGAD user=postgres password=321")
    cur = conn.cursor()
    cur.execute("INSERT INTO vectores(vector,ruta) VALUES (%s, %s)", (vec,ruta))
    conn.commit()
    cur.close()
    conn.close()
def crear_tabla():
    conn = psycopg2.connect("dbname= TPGAD user=postgres password=321")
    cur = conn.cursor()
    cur.execute("CREATE TABLE vectores (id serial PRIMARY KEY, vector double precision[] , ruta varchar, idHoja bigint);")
    conn.commit()
    cur.close()
    conn.close()

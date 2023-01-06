import psycopg2
def insertar_imagen(vec,ruta):
    conn = psycopg2.connect("dbname=postgres user=postgres password=321")
    cur = conn.cursor()

    #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    #cur.execute("CREATE TABLE vectores (id serial PRIMARY KEY, vector varchar[] , route varchar);")
    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    cur.execute("INSERT INTO vectores(vector,route) VALUES (%s, %s)", (vec,ruta))
    """cur.execute("SELECT * FROM test;")
    records = cur.fetchall()
    print(records)"""

    conn.commit()

    cur.close()
    conn.close()
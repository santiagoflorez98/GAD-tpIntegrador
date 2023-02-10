import controlador
import interfaz

#interfaz.ventanaPrincipal()
#controlador.cargarEnDb()
resultado = controlador.consultas()
print(f'Porcentaje de acierto primera coincidencia: {resultado[0]}')
print(f'Porcentaje de acierto primeras 5 coincidencias: {resultado[1]}')

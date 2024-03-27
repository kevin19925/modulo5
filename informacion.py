# Función para agregar nombres y apellidos a la lista
from datetime import datetime
nombres_pacientes = []
edades= []
def agregar_nombre(info):
    datos= info.split(" ")
    if len(datos) == 3:
        nombres_pacientes.append(datos[0] +" "+datos[1])
    else:
         nombres_pacientes.append(datos[0]+" " +datos[2])
         




def agregar_edad(info):
    datos = info.split(" ")
    año_nacimiento = 0
    if len(datos) == 3:
        año_nacimiento = int(datos[2])
    else:
        año_nacimiento = int(datos[-1])
    edad_actual = (datetime.now()).year - año_nacimiento
    edades.append(edad_actual)

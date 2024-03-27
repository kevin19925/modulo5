
from informacion import agregar_edad, nombres_pacientes,edades,agregar_nombre
datos_pacientes = [
    "Antonio Moreno 2000",
    "Carmen Díaz 2001",
    "Fernando García 2003",
    "Teresa Rodríguez 2004",
    "José López 2005",
    "Miguel Ángel Ortiz 1999",
    "Lucía Gómez 2000",
    "Francisco Javier Sánchez 2001",
    "Beatriz Domínguez 2002",
    "Adrián López 2011",
    "Martina Pascual 2012",
    "Álvaro Torres 2013",
    "Berta Romero 2014"
]

for paciente in datos_pacientes:
    agregar_edad(paciente)
    agregar_nombre(paciente)


print(f"nombre de los pacientes {nombres_pacientes}")
print("******************************************")
print(f"edades de los pacientes {edades}")


mayor=edades.index(max(edades))
menor=edades.index(min(edades))

print("\nEl paciente mayor es:", nombres_pacientes[mayor], "con", edades[mayor], "años.")
print("El paciente menor es:", nombres_pacientes[menor], "con", edades[menor], "años.")
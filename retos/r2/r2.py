print("\nBienvenido a KrakeTravels\n")

pais = ""
print("Seleccione el país:")
print("1. Ecuador")
print("2. Colombia")
print("3. Perú")
pais_opcion = input("Ingrese el número correspondiente al país: ")

if pais_opcion == "1":
    pais = "ecuador"
elif pais_opcion == "2":
    pais = "colombia"
elif pais_opcion == "3":
    pais = "perú"
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")

print("\nSeleccione la zona:")
print("1. Urbana")
print("2. Rural")
print("3. Perimetral")
zona_opcion = input("Ingrese el número correspondiente a la zona: ")

if zona_opcion == "1":
    zona = "urbana"
elif zona_opcion == "2":
    zona = "rural"
elif zona_opcion == "3":
    zona = "p1erimetral"
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")

velocidad = float(input("Ingrese la velocidad del conductor en Km/h: "))

limite_min = 0
limite_max = 0
mensaje = ""

if pais == "ecuador":
    if zona == "urbana":
        limite_min = 10
        limite_max = 50
    elif zona== "rural":
        limite_min = 51
        limite_max = 70
    elif zona== "perimetral":
        limite_min = 71
        limite_max = 90
elif pais == "colombia":
    if zona== "urbana":
        limite_min = 10
        limite_max = 30
    elif zona == "rural":
        limite_min = 31
        limite_max = 80
    elif zona == "perimetral":
        limite_min = 81
        limite_max = 100
elif pais == "peru":
    if zona == "urbana":
        limite_min = 10
        limite_max = 40
    elif zona== "rural":
        limite_min = 41
        limite_max = 60
    elif zona == "perimetral":
        limite_min = 61
        limite_max = 120


if velocidad < limite_min:
    mensaje = "¡Velocidad  baja! Deberías aumentarla."
elif velocidad >= limite_min and velocidad  < limite_max:

    mensaje = "¡Velocidad  correcta! ."
else:
    mensaje = "¡Velocidad muy alta! Por favor, reduce la velocidad."

print("***************************")
print(f"tu velocidad en {pais} en la zona {zona} es de {velocidad} \n {mensaje}  ")

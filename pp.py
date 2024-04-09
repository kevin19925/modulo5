estatura = float (input("Ingrese su estatura en metros (por ejemplo, 1.76)"))
if estatura < 0 or estatura > 2.50:
    print("Estatura fuera de rango, ingrese una estatura válida.")
    exit( )
peso = float(input("Ingrese su peso en kilogramos (por ejemplo, 70.0): "))
if peso < 0 or peso > 300.0:
    print("Peso fuera de rango.")
    exit()
imc = peso / (estatura * estatura)
print(f"Su Índice de Masa Corporal es {imc}")
nombre = input ("Ingrese su nombre: ")
if imc < 18.5:
    mensaje - "bajo peso"
elif imc < 25:
    mensaje - "peso saludable"
elif imc < 30:
    mensaje - "sobrepeso"
else:
    mensaje = "obesidad"

print(f"{nombre}, usted tiene {mensaje}.")
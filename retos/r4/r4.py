datos =[]
cont= int(input("ingrese el numero de veces  "))
for i in range(cont):
    dato= input(f"ingrese dato {i+1} " )

    if dato.isdigit():
        print("entero")

        datos.append(int(dato))
    elif "," in dato or "." in dato :
        print("decimal")
        datos.append(float(dato))
    else:
        print("cadena")
        datos.append((dato))

print("La lista es:", datos)
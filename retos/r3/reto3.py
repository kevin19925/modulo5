
menu = ["Hamburguesa", "Pizza", "Ensalada", "Sopa", "Pasta"]

def mostrar_menu():
    if menu:
        print("\n--- Menú del Restaurante Segunda es Todo ---")
        for index in range(len(menu)):
         print(f"{index + 1}. {menu[index]}")
    else:
        print("\nEl menú está vacío.")

def agregar_plato():
    plato = input("Ingrese el nombre del plato a añadir: ")
    menu.append(plato)
    print(f"\n¡'{plato}' ha sido añadido al menú!")

def buscar_plato():
    plato = input("Ingrese el nombre del plato a buscar: ")
    if plato in menu:
        print(f"\n'{plato}' se encuentra en el menú.")
    else:
        print(f"\n'{plato}' no está en el menú.")

def eliminar_plato():
    plato = input("Ingrese el nombre del plato a eliminar: ")
    if plato in menu:
        menu.remove(plato)
        print(f"\n¡'{plato}' ha sido eliminado del menú!")
    else:
        print(f"\n'{plato}' no está en el menú, no se puede eliminar.")





while True:
    print("\n--- Menú del Restaurante Segunda es Todo ---")
    print("1. Añadir plato al menú")
    print("2. Buscar en el menú")
    print("3. Eliminar plato del menú")
    print("4. Mostrar platos del menú")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
       
        agregar_plato()
    elif opcion == "2":
      
        buscar_plato()
    elif opcion == "3":
   
        eliminar_plato()
    elif opcion == "4":
        mostrar_menu()
    elif opcion == "5":
        print("Gracias por utilizar el Menú del Restaurante Segunda es Todo. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
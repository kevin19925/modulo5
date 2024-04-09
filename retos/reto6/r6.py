class Auto:
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
            print(f"Se actualizó el kilometraje a {self.kilometraje}")
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Se realizó un viaje de {kilometros} km")
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

    @staticmethod
    def comparar(auto1, auto2):
        
        if auto1.kilometraje == auto2.kilometraje:
            print("Los kilómetros recorridos por ambos autos son iguales.")
        else:
            print("Los kilómetros recorridos por ambos autos son diferentes.")

    @classmethod
    def auto_Toyota(cls):
        marca = "Toyota"
        modelo = "hilux"
        anio = "2020"
        return cls(marca, modelo, anio)
    
    @staticmethod
    def mayor(auto1, auto2):
        
        if auto1.kilometraje > auto2.kilometraje:
            print(f" auto :{ auto1.marca } tiene mas kilometraje")
        else:
            print(f" auto :{ auto2.marca } tiene mas kilometraje")

    @classmethod
    def auto_mazda(cls):
        marca = "mazda"
        modelo = "cx3"
        anio = "2020"
        return cls(marca, modelo, anio)


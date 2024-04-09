
import random
class Laptop:
    def __init__(self, marca, procesador, memoria, costo=0, impuesto=0):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto

    def valor_descuento(self, descuento):
        return self.costo * (1 - descuento)
    def realizar_diagnostico_sistema(self):
            resultado = {
                "MARCA": self.marca,
                "PROCESADOR": self.procesador,
                "MEMORIA RAM": "OK" if self.memoria >= 8 else "Aumentar memoria RAM",
                "BATERIA": "OK" if random.choice([True, False]) else "Cambiar de batería"
            }
            return resultado
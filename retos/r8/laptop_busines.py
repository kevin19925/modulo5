from laptop import Laptop
import random
class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, disco, duracion_bateria ,costo=0, impuesto=0):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.disco = disco
        self.duracion_baterria=duracion_bateria
    def __str__(self):
        return f"Marca: {self.marca} \nProcesador: {self.procesador} \nMemoria: {self.memoria} \ndisco: {self.disco}  \nbateria: {self.duracion_baterria}  \nPrecio: {self.costo}\n ------------------------------------------ \n"

    def realizar_diagnostico_sistema(self):
        resultado_dianostico=super().realizar_diagnostico_sistema()
        resultado_conectividad=self.verificar_conectividad_red()
        resultado_dianostico["resultado conectividad"]=resultado_conectividad
        return resultado_dianostico
    
    def verificar_conectividad_red(self):
        pruebas=["disponibilidad de Wi-Fi", "el acceso a servidores empresariales","la latencia de la red"]
        resultados={}

        for result in  pruebas:
            resultados [result]= random.choice([True,False])
        return resultados



    pass
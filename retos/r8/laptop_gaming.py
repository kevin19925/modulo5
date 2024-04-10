from laptop import Laptop

class Laptop_Gaming (Laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_garfica ,costo=500, impuesto=0):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjeta_grafica=tarjeta_garfica
    def __str__(self):
        return f"Marca: {self.marca} \nProcesador: {self.procesador} \nMemoria: {self.memoria} \nTarjeta Gráfica: {self.tarjeta_grafica} \nPrecio: {self.costo}\n ------------------------------------------ \n"

    def realizar_diagnostico_sistema(self):
        resultado_dianostico=super().realizar_diagnostico_sistema()
        resultado_juego=self.diagnostico_juegos()
        resultado_dianostico["resultado juegos"]=resultado_juego
        return resultado_dianostico

    def diagnostico_juegos (self):
      
        juegos=["formite","juego 2","juego 3"]
        resultado={}
        for juego in juegos:
            
            fps_base=30
            if "rtx" in self.tarjeta_grafica:
                fps=fps_base*3
            if "gtx" in self.tarjeta_grafica:
                fps=fps_base*2
            else:
                fps=fps_base
            resultado[juego]=f"{fps} fps"
        return resultado
    pass
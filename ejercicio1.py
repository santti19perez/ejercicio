class Vehiculo:
    def _init_(self,Velocidad_maxima,Kilometraje):
        self.Velocidad_maxima:Velocidad_maxima
        self.Kilometraje:Kilometraje
    def mostrar_informacion(self):
        print(f"velocidad maxima:{self.Velocidad_maxima} km/h ")
        print(f"Kilometraje: {self.Kilometraje} km")

mi_auto = Vehiculo(200,50000)
mi_auto.mostrar_informacion()


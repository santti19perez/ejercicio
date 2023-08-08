import math


class Punto:
    def init(self, x, y):
        self.x = x
        self.y = y

    def str(self):
        return f'({self.x}, {self.y})'

    def mostrar_coordenadas(self):
        print(f'Coordenadas: ({self.x}, {self.y})')

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        print(f'Punto movido a ({self.x}, {self.y})')

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) * 2 + (self.y - otro_punto.y) * 2)
        return distancia


# Ejemplo de uso
punto1 = Punto(3, 4)
print(f'Coordenadas del punto 1: {punto1}')

punto1.mostrar_coordenadas()
punto1.mover(7, 2)
punto1.mostrar_coordenadas()

punto2 = Punto(1, 1)
distancia = punto1.calcular_distancia(punto2)
print(f'Distancia entre punto1 y punto2: {distancia}')
import math


class Circulo:
    def init(self, centro_x, centro_y, radio):
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, x, y):
        distancia_al_centro = math.sqrt((x - self.centro_x) * 2 + (y - self.centro_y) * 2)
        return distancia_al_centro <= self.radio


# Ejemplo de uso
circulo = Circulo(0, 0, 5)
print(f'Área del círculo: {circulo.calcular_area()}')
print(f'Perímetro del círculo: {circulo.calcular_perimetro()}')

x_punto = 2
y_punto = 3
if circulo.punto_pertenece(x_punto, y_punto):
    print(f'El punto ({x_punto}, {y_punto}) pertenece al círculo.')
else:
    print(f'El punto ({x_punto}, {y_punto}) no pertenece al círculo.')
class Punto:
    def init(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def init(self, esquina_superior_izquierda, esquina_inferior_derecha):
        self.esquina_superior_izquierda = esquina_superior_izquierda
        self.esquina_inferior_derecha = esquina_inferior_derecha

    def calcular_perímetro(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return 2 * (base + altura)

    def calcular_área(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_superior_izquierda.x - self.esquina_inferior_derecha.x)
        altura = abs(self.esquina_superior_izquierda.y - self.esquina_inferior_derecha.y)
        return base == altura

# Crear instancias de puntos
esquina_sup_izq = Punto(1, 5)
esquina_inf_der = Punto(6, 1)

# Crear un rectángulo
mi_rectángulo = Rectángulo(esquina_sup_izq, esquina_inf_der)

# Usar los métodos de la clase Rectángulo
print("Perímetro:", mi_rectángulo.calcular_perímetro())
print("Área:", mi_rectángulo.calcular_área())
print("Es cuadrado:", mi_rectángulo.es_cuadrado())
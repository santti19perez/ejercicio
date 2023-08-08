class punto:
    def _init_(self,x,y):
        self.x = x
        self.y = y

    def _str_(self):
        return f'({self.x}, {self.y})'

punto_1 = punto(3, 4)
print(f'coordenadas del punto 1: {punto_1}')
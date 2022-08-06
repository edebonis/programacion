class Puerta:
    ancho = 0
    alto = 0
    color = "Rojo"
    abierta = False
    
    def __init__(self, col="Rojo", alt=0, anc = 0):
        self.color = col
        self.alto = alt
        self.ancho = anc
        print("Creada puerta: " + self.__str__())
    
    def abrir(self):
        self.abierta = True
        return self.abierta
    
    def cerrar(self):
        self.abierta = False
        return self.abierta
    
    def cambiar_estado(self):
        self.abierta = not self.abierta
        return self.abierta
    
    def pintar(self, color):
        self.color = color
        return self.color
    
    def __str__(self):
        return self.color + " - " + str(self.alto) + "x" + str(self.ancho)


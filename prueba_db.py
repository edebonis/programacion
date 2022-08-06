import sqlite3

db = sqlite3.connect('/home/esteban/Descargas/Telegram Desktop/prueba.db')

c = db.cursor()

class Estudiante:
    ide = 0
    nombre = ""
    apellido = ""    
    def __init__(self,i=0):
        self.ide = i
        if self.ide == 0:
            mensaje = "Estudiante nuevo"
        else:
            print("Buscando Estudiante")
            self.buscar_estudiante()
            mensaje = self.nombre
        print(mensaje)
    
    def buscar_estudiante(self):
        c.execute("SELECT NOMBRE, APELLIDO FROM ESTUDIANTES WHERE ID = {}".format(self.ide))
        respuesta = c.fetchall()
        self.nombre = respuesta[0][0]
        self.apellido = respuesta[0][1]
        return True
    
    def __str__(self):
        return "Horacio"


e = Estudiante()

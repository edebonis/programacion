import sqlite3

bd = sqlite3.connect("/home/esteban/Documentos/base_de_datos/prod_inf.db")
c = bd.cursor()

class Articulos:
    
    def __init__(self, n="", f="", p=""):
        self.nombre = n
        fabricante = Fabricantes(nombre=f)
        self.id_fab = fabricante.obtener_id()
        self.precio = p
    
    def obtener(self, id):
        c.execute("SELECT * FROM ARTIUCULOS WHERE ID = {}".format(id))
        resp = c.fetchall()
        registro = resp[0]
        self.nombre = registro[1]
        self.precio = registro[2]
        self.id_fab = registro[3]
        print("Artículo {}, cargado. Nombre {}".format(id, self.nombre))
        return True
    
    def guardar(self):
        sql = 'INSERT INTO ARTICULOS(NOMBRE, PRECIO, ID_FAB) VALUES("{}",{},{});'
        c.execute(sql.format(self.nombre, self.precio, self.id_fab))
        bd.commit()
        return True
    
class Fabricantes:
    
    def __init__(self, nombre=""):
        sql = 'SELECT * FROM FABRICANTES WHERE NOMBRE = "{}";'
        resp = bd.execute(sql.format(nombre)).fetchall()
        if resp:
            self.nombre = resp[0][1]
            self.id = resp[0][0]
        else:
            self.nombre = nombre
            self.guardar()
    
    def obtener(self, id):
        c.execute("SELECT * FROM FABRICANTES WHERE ID = {}".format(id))
        resp = c.fetchall()
        registro = resp[0]
        self.nombre = registro[1]
        print("Fabricante {}, cargado. Nombre {}".format(id, self.nombre))
        return True
    
    def guardar(self):
        sql = 'INSERT INTO FABRICANTES(NOMBRE) VALUES("{}");'
        c.execute(sql.format(self.nombre))
        bd.commit()
        return True
    
    def obtener_id(self):
        sql = 'SELECT ID FROM FABRICANTES WHERE NOMBRE = "{}"'
        resp = bd.execute(sql.format(self.nombre)).fetchall()[0][0]
        return resp
    
    



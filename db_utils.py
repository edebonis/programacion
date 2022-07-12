import sqlite3


class Base:
    def __init__(self):
        self.db = sqlite3.connect("usuarios.db")
        self.c = self.db.cursor()

    def alta_usuario(self, nom, passw, nusr):
        if not self.existe_usuario(nusr):
            self.c.execute(f'INSERT INTO USUARIOS (NUSUARIO, CONTRASENIA, NOMBRE) VALUES ("{nusr}", "{passw}", "{nom}");')
            self.db.commit()
            return 0
        else:
            return 1

    def login(self, passw, nusr):
        self.c.execute(f'SELECT * FROM USUARIOS WHERE NUSUARIO ="{nusr}";')
        resp = self.c.fetchall()
        if resp:
            if resp[0][2] == passw:
                return 0
            else:
                return 1
        else:
            return 2

    def existe_usuario(self, nusr):
        self.c.execute(f'SELECT * FROM USUARIOS WHERE NUSUARIO ="{nusr}";')
        resp = self.c.fetchall()
        if resp:
            return True
        return False

    def cambiar_contrasenia(self, old_passw, new_passw, nusr):
        if self.login(old_passw, nusr) == 0:
            self.c.execute(f'UPDATE USUARIOS SET CONTRASENIA = {new_passw} WHERE NUSUARIO ="{nusr}";')
            self.db.commit()
        else:
            return 1
        return 0

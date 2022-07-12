from db_utils import Base


bd = Base()

respuestas_login = ["login ok", "Contraseña incorrecta", "No existe usuario"]
respuestas_contrasenia = ["cambio ok", "error old passw"]
resp = bd.cambiar_contrasenia("87654321", "445", "edebonis2")
print(respuestas_contrasenia[resp])

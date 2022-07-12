from db_utils import Base


bd = Base()


resp = bd.cambiar_contrasenia("87654321", "445", "edebonis2")
print(bd.respuestas_contrasenia[resp])

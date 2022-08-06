from db_utils import Base


bd = Base()

#print(bd.alta_usuario('Esteban', 'qvg802', 'edebonis'))

print(bd.login('qvg802', 'edebonis'))

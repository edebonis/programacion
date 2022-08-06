def prueba(*args):
    for i in args:
        print(i)
    
def pruebak(**kwargs):
    energia = kwargs.get('energia')
    poder = kwargs.get('poder',"hola")
    print(energia,poder)
    
    
pruebak(energia=1,podera=2)
def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):

            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator

@my_decorator_name('CodigoFácilito')
def suma(a, b):
    return a + b

print(suma(1,5))
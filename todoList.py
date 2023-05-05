''' Trabajo práctico N°1 - Laboratorio de Programación I - 4°B'''
from datetime import date, datetime

tarea = {"descripcion": None,
         "fecha": None,
         "completada": False}

tareas = []


def agregar_tarea():
    tarea_agregar = tarea.copy()
    tarea_agregar["descripcion"] = input("Ingrese descripción de la tarea:")
    tarea_agregar["fecha"] = datetime.now().date().isoformat()
    tareas.append(tarea_agregar)
    print('')
    listar_tareas()


def listar_tareas():
    print("Tareas:")
    a = 1
    for t in tareas:
        completada = "√" if t["completada"] else "X "
        print(str(a) + " - " + t["descripcion"] + " " + completada)
        a += 1

def listar_tareas_pendientes():
    print("Tareas pendientes:")
    a = 1
    for t in tareas:
        print(str(a) + " - " + t["descripcion"])
        a += 1

def eliminar_tarea():
    listar_tareas()
    eliminar = input("Elija qué tarea eliminar")
    tarea_eliminada = tareas.pop(int(eliminar) - 1)
    print("Tarea " + tarea_eliminada["descripcion"] + " eliminada con éxito")
    print('')


def completar_tarea():
    listar_tareas()
    completar = input("Elija qué tarea completar")
    tareas[int(completar) - 1]["completada"] = True
    print("Tarea " + tareas[int(completar) - 1]["descripcion"] + " eliminada con éxito")
    print('')

def salir():
    print("Hasta luego")
    return True

def menu():
    funciones = [agregar_tarea, listar_tareas, eliminar_tarea, completar_tarea, salir]
    print('')
    print('--------------------')
    print('1- Agregar tarea')
    print('2- Listar tareas')
    print('3- Eliminar tarea')
    print('4- Completar tarea')
    print('5- Salir')
    print('')
    eleccion = int(input("Seleccione opción: "))
    return funciones[eleccion - 1]()


def main():
    while not menu():
        pass


if __name__ == '__main__':
    main()

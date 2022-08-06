import datetime

def dias_vividos(anio, mes, dia):
    hoy = datetime.date.today()
    fecha_nacimiento = datetime.date(anio, mes, dia)
    return (hoy - fecha_nacimiento).days

print(dias_vividos(1982, 5, 4))
    
# importamos el modulo
import pywhatkit 
   
# utilizaremos controles de excepciones
try: 
     
  # enviando mensaje al receptor
  # usando pywhatkit 
  pywhatkit.sendwhatmsg("+5491130098326",  
                        "Hola desde Mi Diario Python",  
                        13, 24) 
  print("Envio Exitoso!") 
   
except: 
     
  # manejo de excepcion
  # e impresion del error
  print("Ha ocurrido un error!")
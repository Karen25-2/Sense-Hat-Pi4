
#Instituto Tecnologico de Tijuana
#Depto de Sistemas y Computación
#Ing. En Sistemas Computacionales
#Autor :Martinez Estrada Ana Karen @nickname karen25-2
#Repositorio:https:https://github.com/Karen25-2/Sense-Hat-Pi4
                         

from sense_hat import SenseHat
sense = SenseHat()
# Define los colores rojo y verde

rojo = (255, 0, 0)
verde = (0, 255, 0)

# Toma lecturas de los tres sensores

t = sense.get_temperature() # temperatura
p = sense.get_pressure() # presión
h = sense.get_humidity() # humedad

# Redondea los valores a un lugar decimal
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

# str() convierte el valor en una cadena de caracteres, para que pueda ser concatenado

message = "Temperatura: " + str(t) + " Presión: " + str(p) + "Humedad: " + str(h)
if t > 18.3 and h > 50 and p> 800:
   bg = verde
else:
 bg = rojo
 
# Muestra el mensaje
sense.show_message(message, scroll_speed=0.05, back_colour=bg) 

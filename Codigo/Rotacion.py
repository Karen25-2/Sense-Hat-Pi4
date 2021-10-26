
'''
Instituto Tecnologico de Tijuana
Depto de Sistemas y Computación
Ing. En Sistemas Computacionales

Autor :Martinez Estrada Ana Karen @nickname karen25-2
Repositorio:https:https://github.com/Karen25-2/Sense-Hat-Pi4

                         
'''


from sense_hat import SenseHat
import sys
import time

#Definir algunos colores

X = (255, 0, 0)
O = (255,255,255)


# Definimos donde mostrar cada color

question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, X, X, X, X, X, X, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
]

sense = SenseHat()

# Mostrar esos colores en la pantalla LED
    
sense.set_pixels(question_mark)

 # Se  utiliza el metodo set_rotacion para hacer que la figura que emos dibujado en la matrix de leds haga una rotacion esto con los valores definidos 
while True:
    for r in [0, 90, 180, 270]:
        sense.set_rotation(r)
        time.sleep(0.5)

'''
Instituto Tecnologico de Tijuana
Depto de Sistemas y Computación
Ing. En Sistemas Computacionales
Autor :Martinez Estrada Ana Karen @nickname karen25-2
Repositorio:https:https://github.com/Karen25-2/Sense-Hat-Pi4
                         
'''

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255,105, 180)
yellow = (255, 255, 0)

# Genera un color aleatorio
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

sense.show_letter("K", pick_random_colour())
sleep(1)
sense.show_letter("A", pick_random_colour())
sleep(1)
sense.show_letter("R", pick_random_colour())
sleep(1)
sense.show_letter("E", pick_random_colour())
sleep(1)
sense.show_letter("N", pick_random_colour())
sleep(1)

sense.clear()

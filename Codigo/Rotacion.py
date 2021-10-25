from sense_hat import SenseHat
import sys
import time

X = (255, 0, 0)
O = (255,255,255)
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

sense.set_pixels(question_mark)

while True:
    for r in [0, 90, 180, 270]:
        sense.set_rotation(r)
        time.sleep(0.5)

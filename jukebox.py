import machine
import utime

from melodias import *

buzzer = machine.PWM(machine.Pin(16))

button_1 = machine.Pin(13, machine.Pin.IN)
button_2 = machine.Pin(12, machine.Pin.IN)
button_3 = machine.Pin(11, machine.Pin.IN)
button_4 = machine.Pin(10, machine.Pin.IN)

while True:
    
    if (button_1.value() == 1):
        play(buzzer, musicas['harrypotter'])
        
    elif (button_2.value() == 1):
        play(buzzer, musicas['zeldatheme'])
    
    elif (button_3.value() == 1):
        play(buzzer, musicas['starwars'])
    
    elif (button_4.value() == 1):
        play(buzzer, musicas['pinkpanther'])
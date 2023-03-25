from pynput.keyboard import Controller
import pynput.mouse as pmouse 
import keyboard
from time import sleep

pnput_ms = pmouse.Controller()
pnput_kb = Controller()

running = False 

def run():
    pnput_ms.press(pmouse.Button.left)
    pnput_kb.press('a')
    sleep(20)
    pnput_kb.release('a')
    pnput_kb.press('s')
    sleep(20)
    pnput_kb.release('s')
    pnput_ms.release(pmouse.Button.left)

while True:
    if keyboard.is_pressed('m'):
        if running == False:
            running = True
    elif keyboard.is_pressed('n'):
        if running:
            running = False

    if running:
        run()
